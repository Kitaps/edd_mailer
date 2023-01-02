
from reader import send_files

DIRECTIONS_PATH = "Alumnos.xlsx"
FILE_PATH = "./RI3"
DOCUMENT_TYPE = ".txt"
TITULO = "[IIC2133] Recorreccion I3"
# BODY in mailer

send_files(DIRECTIONS_PATH, FILE_PATH, DOCUMENT_TYPE, TITULO)