# Lee el excel como dataframe
# De este se puede obtener el nombre y mail a partir del nro de alumno
from os import listdir
import pandas
from mailer import mandar_mail
from time import sleep

def send_files(student_directions_path, student_files_path, doc_type, subject):

    # df = pandas.read_excel("Alumnos.xlsx")
    df = pandas.read_excel(student_directions_path)

    # print(df)

    # print(df.loc[df["Nombre"]=="AGUSTIN"])
    # alumno_aux = df.loc[df["N° Alumno"]=="13649256"]
    # alumno = alumno_aux.iloc[0]
    # print(alumno["Nombre"])
    # print(alumno["Mail"])
    # print(alumno["N° Alumno"])

    # print(type(alumno["Nombre"]))
    # print(type(alumno["Mail"]))

    dir_path = student_files_path

    documentos_names = listdir(dir_path)
    for document_name in documentos_names:
        # if ".pdf" in document_name:
        if doc_type in document_name:
            nro_alumno = document_name.replace(doc_type, "")
            # print(nro_alumno)
            alumno_aux = df.loc[df["N° Alumno"]==nro_alumno]
            # print(alumno_aux)
            alumno = alumno_aux.iloc[0]
            nombre = alumno["Nombre"]
            mail = alumno["Mail"]
            path = f"{dir_path}/{nro_alumno}{doc_type}"
            print("------------------------------------")
            print(f"Mandando un mail a {nombre}: {mail}")
            print(f"Subiendo documento en {path}...")
            try:
                mandar_mail(nro_alumno, mail, nombre, path, subject, doc_type)
                print("Mandado")
                sleep(1)
            except Exception as error:
                print(error)
                print(f"!!!NO SE HA MANDADO LA CORRECCION DE {nro_alumno}:{mail}!!!")
                with open("ERRORS.txt", "a") as err_file:
                    err_file.write("------------------------------------\n")
                    err_file.write(str(error))
                    err_file.write(f"\n!!!NO SE HA MANDADO LA CORRECCION DE {nro_alumno}:{mail}!!!\n")
                    err_file.write("------------------------------------\n")
            # print(document_name)
