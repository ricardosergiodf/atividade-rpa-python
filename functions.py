import logging
import datetime
from botcity.web import WebBot, Browser, By
from botcity.maestro import *
import os

def setup_logging():
    log_path = "C:/Users/ricar/Desktop/-/Compass/atividades-praticas-compass/ativ-pratica-1-rpa-python/resources/logfiles"
    # Verifica se a pasta "logfiles" existe, se não, cria-a
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    data_atual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo_log = f"{log_path}/logfile-{data_atual}.txt"

    logging.basicConfig(
        filename=nome_arquivo_log,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%d/%m/%Y %H:%M:%S"
    )

def login(username, password, login_field, password_field, submit_btn, bot, maestro, execution, counter):
    logging.info(f"{counter}a tentativa de login.")
    try:
        login_field.send_keys(username)
        password_field.send_keys(password)
        submit_btn.click()
        successful_login = bot.find_element(".post-title", By.CSS_SELECTOR)
        if successful_login:
            bot.save_screenshot("resultados.png")
            logging.info(f"Login feito com sucesso. Username: {username}, Password: {password}.")
            return True
        else:
            logging.error(f"Erro ao tentar realizar o login. Username: {username}, Password: {password}")
            return False
    except Exception as e:
        logging.error(f"Erro fatal na execucao do login: {e}")
        if maestro:
            maestro.error(task_id=execution.task_id, exception=e)
        return False
