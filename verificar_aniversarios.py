from datetime import datetime
from app import db, Aniversario
import smtplib
from twilio.rest import Client

# Configurações do Twilio (SMS e WhatsApp)
TWILIO_ACCOUNT_SID = "your account sid"
TWILIO_AUTH_TOKEN = "your auth token"
TWILIO_PHONE_NUMBER = "your number"

# Configurações do e-mail
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USER = "your email"
EMAIL_PASSWORD = "your password"


# Função para enviar e-mail
def enviar_email(destinatario, mensagem):
    servidor = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    servidor.starttls()
    servidor.login(EMAIL_USER, EMAIL_PASSWORD)
    servidor.sendmail(EMAIL_USER, destinatario, mensagem)
    servidor.quit()


# Função para enviar SMS ou WhatsApp
def enviar_sms_whatsapp(destinatario, mensagem, usar_whatsapp=False):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    if usar_whatsapp:
        from_whatsapp = f"whatsapp:{TWILIO_PHONE_NUMBER}"
        to_whatsapp = f"whatsapp:{destinatario}"
        client.messages.create(body=mensagem, from_=from_whatsapp, to=to_whatsapp)
    else:
        client.messages.create(
            body=mensagem, from_=TWILIO_PHONE_NUMBER, to=destinatario
        )


# Função principal
def verificar_aniversarios():
    hoje = datetime.now().date()
    aniversarios = Aniversario.query.filter(Aniversario.data_aniversario == hoje).all()

    for aniversario in aniversarios:
        mensagem = f"Feliz aniversário, {aniversario.nome}!"

        # Envia e-mail
        if aniversario.email:
            enviar_email(aniversario.email, mensagem)

        if aniversario.telefone:
            enviar_sms_whatsapp(aniversario.telefone, mensagem, usar_whatsapp=True)

if __name__ == '__main__':
    verificar_aniversarios()