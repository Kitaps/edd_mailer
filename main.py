
from reader import send_files

DIRECTIONS_PATH = "Alumnos.xlsx"
FILE_PATH = "./RI1"
DOCUMENT_TYPE = ".txt"
TITULO = "IIC2133 - Recorrección I1"
# BODY in mailer

send_files(DIRECTIONS_PATH, FILE_PATH, DOCUMENT_TYPE, TITULO)