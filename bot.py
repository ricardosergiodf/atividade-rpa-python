"""
Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.
"""

# Import for the Web Bot
from botcity.web import WebBot, Browser, By
from botcity.maestro import *
import logging
from datetime import datetime

# Configuração do logging para sobrescrever log.txt
logging.basicConfig(
    filename='log.txt',  # Nome do arquivo de log
    filemode='w',        # 'w' para sobrescrever a cada execução
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",  # Data - Nivel do log (INFO, WARNING, ERROR) - Mensagem
    datefmt="%d/%m/%Y %H:%M:%S"
)

BotMaestroSDK.RAISE_NOT_CONNECTED = False

# Função que realiza o login
def login(username, password, login_field, password_field, submit_btn, bot, maestro, execution, counter):
    logging.info(f"{counter}a tentativa de login.")
    try:
        login_field.send_keys(username)
        password_field.send_keys(password)
        submit_btn.click()
        successful_login = bot.find_element(".post-title", By.CSS_SELECTOR)
        if successful_login:
            bot.save_screenshot("resultados.png")
            logging.error(f"Login feito com sucesso. {username}, {password}")
            return True
        else:
            logging.error(f"Erro ao tentar realizar o login.")
            return False
    except Exception as e:
        logging.error(f"Erro fatal na execucao do login: {e}")
        if maestro:
            maestro.error(task_id=execution.task_id, exception=e)
        return False

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    if execution.task_id == 0:
        logging.info("Maestro desativado -> Executando localmente")
        maestro = None

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = r"C:\Users\ricar\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

    logging.info("Inicio - AP-1-RPA-Python")

    is_incorrect_login = execution.parameters.get("is_incorrect_login")
    # is_incorrect_login = "y"
    logging.info(f"Processo iniciado com {'Login Correto' if is_incorrect_login == 'n' else 'Login Incorreto'} como parametro.")

    url = "https://practicetestautomation.com/practice-test-login/"
    bot.browse(url)
    logging.info(f"Abrindo navegador no: {url}")

    if is_incorrect_login == "n":
        # Obtem o username e password corretos
        try:
            username = bot.find_element("/html[1]/body[1]/div[1]/div[1]/section[1]/section[1]/ul[1]/li[2]/b[1]", By.XPATH)
            password = bot.find_element("/html[1]/body[1]/div[1]/div[1]/section[1]/section[1]/ul[1]/li[2]/b[2]", By.XPATH)
            username = username.text
            password = password.text
            logging.info(f"Username e Password capturados.")
        except Exception as e:
            logging.error(error)
            if maestro:
                maestro.error(task_id=execution.task_id, exception=e)
    elif is_incorrect_login == "y":
        # Obtem o username incorreto e password
        try:
            username = bot.find_element("/html[1]/body[1]/div[1]/div[1]/section[1]/section[1]/ol[2]/li[2]/b[1]", By.XPATH)
            password = bot.find_element("/html[1]/body[1]/div[1]/div[1]/section[1]/section[1]/ul[1]/li[2]/b[2]", By.XPATH)
            username = username.text
            password = password.text
            logging.info(f"Username e Password capturados.")
        except Exception as e:
            logging.error(error)
            if maestro:
                maestro.error(task_id=execution.task_id, exception=e)
    else:
        error = "Incorrect Parameter"
        logging.error(error)
        if maestro:
            maestro.error(task_id=execution.task_id, exception=error)
            maestro.finish_task(
                task_id=execution.task_id,
                status=AutomationTaskFinishStatus.FAILED,
                message="Incorrect Parameter"
            )
        bot.stop_browser()
        return
        
    # print(username, password)

    # Obtem os campos de login field e password field
    try:
        login_field = bot.find_element("/html[1]/body[1]/div[1]/div[1]/section[1]/section[1]/div[1]/div[1]/input[1]", By.XPATH)
        password_field = bot.find_element("/html[1]/body[1]/div[1]/div[1]/section[1]/section[1]/div[1]/div[2]/input[1]", By.XPATH)
        logging.info(f"Campos de login field e password field capturados.")
    except Exception as e:
        logging.error(error)
        if maestro:
            maestro.error(task_id=execution.task_id, exception=e)

    # Obtem o botão de submit
    try:
        submit_btn = bot.find_element("/html[1]/body[1]/div[1]/div[1]/section[1]/section[1]/div[1]/button[1]", By.XPATH)
        logging.info(f"Botao de submit capturado.")
    except Exception as e:
        logging.error(error)
        if maestro:
            maestro.error(task_id=execution.task_id, exception=e)

    # Obtem o botão de Logout
    # try:
    #     bot.wait(3000)
    #     logout_btn = bot.find_element(".wp-block-button__link.has-text-color.has-background.has-very-dark-gray-background-color", By.CSS_SELECTOR)
    #     logout_btn.click()
    #     print("Logout foi clicado")
    # except Exception as e:
    #     print(e)
    #     maestro.error(task_id=execution.task_id, exception=e)

    # Alerta de início
    if maestro:
        maestro.alert(
            task_id=execution.task_id,
            title="Process Started",
            message=f"Started with Username: {username}, Password: {password} -> Using {'Correct Login' if is_incorrect_login == 'n' else 'Incorrect Login'}",
            alert_type=AlertType.INFO
        )

    # Lógica para realizar o login e tentar 3x caso tenha erro
    for counter in range(1, 4):
        login_field.clear()
        password_field.clear()
        result = login(username, password, login_field, password_field, submit_btn, bot, maestro, execution, counter)
        logging.info(f"Resultado da tentativa {counter}: {'Login feito com sucesso' if result else 'Login falhou'}")
        if maestro:
            maestro.alert(
            task_id=execution.task_id,
            title=f"Attempt {counter}",
            message=f"Started attempt {counter}.",
            alert_type=AlertType.INFO
            )
        if result:
            if maestro:
                maestro.post_artifact(
                    task_id=execution.task_id,
                    artifact_name=f"Successful Login.",
                    filepath="resultados.png"
                )
                maestro.finish_task(
                    task_id=execution.task_id,
                    status=AutomationTaskFinishStatus.SUCCESS,
                    message="Task Finished OK."
                )
            break
        else:
            # Obtem o erro
            error = bot.find_element("#error", By.CSS_SELECTOR)
            logging.info("Elemento de erro do login capturado.")
            if maestro:
                maestro.alert(
                    task_id=execution.task_id,
                    title=f"Invalid Login",
                    message=f"{error.text}",
                    alert_type=AlertType.WARN
                )
        if counter == 3:
            logging.warning("Todas as tentativas de login falharam.")
            if maestro:
                maestro.finish_task(
                    task_id=execution.task_id,
                    status=AutomationTaskFinishStatus.SUCCESS,
                    message="All login attempts failed."
                )
            bot.stop_browser()
        
    maestro.alert(
            task_id=execution.task_id,
            title=f"Process Ended",
            message=f"Process Ended - Success AP-1-RPA-Python.",
            alert_type=AlertType.INFO
    )
    logging.info("Processo Finalizado - Sucesso AP-1-RPA-Python.")
    bot.stop_browser()


def not_found(label):

    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
