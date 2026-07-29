import os
import requests

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

mensagem = """
🦷 Monitor de Vagas

✅ O robô foi iniciado com sucesso!

Em breve ele começará a monitorar:
• Diários Oficiais
• Prefeituras
• Concursos
• Processos Seletivos
• Universidades
• Hospitais

Resumo diário às 20h.
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": mensagem
    }
)

print("Mensagem enviada!")
