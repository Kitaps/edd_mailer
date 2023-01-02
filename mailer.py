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

def mandar_mail(nro_alumno, mail, nombre, file_path, subject, doc_type):
    # titulo = "IIC2133 - Corrección I2"
    body = f"Hola {nombre},\nEspero que estes bien.\nHola, adjunto te mando los comentarios de la recorreccion de la I3. Cualquier duda, favor contactar al corrector correspondiente (disponible en el archivo) durante el día de hoy.\n\nExito con el fin de semestre,\nPatrick"

    # Hacemos el mail
    msg = MIMEMultipart()
    msg["From"] = MAIL
    msg["To"] = mail
    msg["Subject"] = subject
    msg.attach(MIMEText(body, 'plain'))

    filename = f"{nro_alumno}{doc_type}"
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


