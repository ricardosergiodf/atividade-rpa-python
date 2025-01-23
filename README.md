# Projeto de Automação de Login 🚀

Este projeto automatiza o processo de login em um site de teste, utilizando o framework BotCity para controle de navegador e o BotMaestro para gerenciamento de tarefas.

## 📋 Requisitos

Certifique-se de instalar as dependências do projeto executando:
```bash
pip install --upgrade -r requirements.txt
```

## 🛠️ Tecnologias Utilizadas

- **Python** 🐍
- **BotCity** 🤖
- **Selenium WebDriver** 🌐
- **BotMaestro SDK** 📊
- **Logging** 📝

## 📂 Estrutura do Projeto

- `bot.py`: Código principal que executa a automação.
- `requirements.txt`: Lista de dependências necessárias.
- `log.txt`: Arquivo de log gerado automaticamente.
- `resultados.png`: Captura de tela após o login bem-sucedido.

## 🚀 Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-repositorio.git
   ```
2. Instale as dependências:
   ```bash
   pip install --upgrade -r requirements.txt
   ```
3. Execute o script Python:
   ```bash
   python main.py
   ```

## ⚙️ Configuração

Antes de executar, certifique-se de ajustar o caminho do WebDriver no código:
```python
bot.driver_path = r"C:\\Users\\ricar\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
```

## 📝 Logs

Os logs da execução são armazenados no arquivo `log.txt`, com as seguintes informações:
- Data e hora 📅
- Nível do log (INFO, WARNING, ERROR) ⚠️
- Mensagem de execução 📩

## 📷 Captura de Tela

Caso o login seja bem-sucedido, uma captura de tela será salva automaticamente como `resultados.png`.

## 🧪 Testando Diferentes Cenários

Para testar logins corretos ou incorretos, ajuste o parâmetro `is_incorrect_login` no código.
- `is_incorrect_login = "n"` → Testa login correto ✅
- `is_incorrect_login = "y"` → Testa login incorreto ❌

## 🛑 Encerramento

Após três tentativas de login malsucedidas, o navegador será fechado automaticamente e o processo finalizado.

## 📬 Contato

Desenvolvido por Ricardo Duarte. ✉️ ricardosergiodf@gmail.com

---

README.me feito por IA (poupar tempo é sempre bom)
Enjoy coding! 💻

