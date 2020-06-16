# Este le manda un mail al nro de alumno
# En este mail agrega el link & el nombre
# Luego lo manda

from credentials import MAIL, PASSWORD
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# nro_alumno = "14620820"
# nombre = "ASD"

def mandar_mail(nro_alumno, mail, nombre, file_path):
    titulo = "IIC2133 - Corrección I2"
    body = f"Hola {nombre},\nEsperamos que les haya ido muy bien en su I2.\nAdjunto viene tu I2 corregida.\nRecuerda que el plazo para recorregir es hasta el lunes 29 de junio a las 23.59, mediante el cuestionario disponible en Siding.\n\nDisculpa el atraso,\nPatrick"

    # Hacemos el mail
    msg = MIMEMultipart()
    msg["From"] = MAIL
    msg["To"] = mail
    msg["Subject"] = titulo
    msg.attach(MIMEText(body, 'plain'))

    filename = f"{nro_alumno}.pdf"
    attachment = open(file_path, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={filename}" )

    msg.attach(part)
    text = msg.as_string()


    # Nos conectamos al gmail
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(MAIL, PASSWORD)
    # print(body)
    server.sendmail(MAIL, mail, text)
    server.quit()
    attachment.close()

if __name__ == "__main__":
    mandar_mail(14620820, "paliedtke@uc.cl", "Patrick")
