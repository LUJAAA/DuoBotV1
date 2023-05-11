import os
import sqlite3

def crearTablas():
    #os.mkdir('C:/DuoBot_Info')
    bd = sqlite3.connect("C:/DuoBot_Info/bdDuoBot")
    cursor = bd.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS actividad(IdCuento INT(255) ,Sesion INT(255),NombreCuento CHAR(255),HoraInicio CHAR(10),HoraFin CHAR(10),Fecha CHAR(10),Comentario CHAR(255), PRIMARY KEY (IdCuento))")
    cursor.execute("CREATE TABLE IF NOT EXISTS programacion(IdProgramacion INT(255) ,Fecha CHAR(15),HoraInicio CHAR(10),HoraFin CHAR(10),Finalizado CHAR(10), PRIMARY KEY (IDProgramacion))")


def registroActividad(IdCuento, Sesion, NombreCuento, HoraInicio, HoraFin, Fecha, Comentario):
    bd = sqlite3.connect("C:/DuoBot_Info/bdDuoBot")
    cursor = bd.cursor()
    sentencia = "INSERT INTO actividad(IdCuento,Sesion,NombreCuento,HoraInicio,HoraFin,Fecha,Comentario) VALUES (?,?,?,?,?,?,?)"
    valores = (IdCuento, Sesion, NombreCuento,
               HoraInicio, HoraFin, Fecha, Comentario)
    cursor.execute(sentencia, valores)
    bd.commit()

def obtenerUltimaSesion():
    bd = sqlite3.connect("C:/DuoBot_Info/bdDuoBot")
    cursor = bd.cursor()
    sentencia = "SELECT Sesion FROM actividad order by Sesion desc limit 1"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    if resultado != []:
        return int(resultado[0][0])+1
    else:
        return 0



def obtenerUltimoCuento():
    bd = sqlite3.connect("C:/DuoBot_Info/bdDuoBot")
    cursor = bd.cursor()
    sentencia = "SELECT IdCuento FROM actividad order by IdCuento desc limit 1"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    if resultado != []:
        return int(resultado[0][0])+1
    else:
        return 0


def obtenerlaUltimaProgramacion():
    bd = sqlite3.connect("C:/DuoBot_Info/bdDuoBot")
    cursor = bd.cursor()
    sentencia = "SELECT IdProgramacion FROM programacion order by IdProgramacion desc limit 1"
    cursor.execute(sentencia)
    resultado = cursor.fetchall()
    if resultado != []:
        return int(resultado[0][0])+1
    else:
        return 0

def registrarNuevaFecha(IdProgramacion, Fecha, HoraInicio, HoraFin, Finalizado):
    bd = sqlite3.connect("C:/DuoBot_Info/bdDuoBot")
    cursor = bd.cursor()
    sentencia = "INSERT INTO programacion(IdProgramacion,Fecha,HoraInicio,HoraFin,Finalizado) VALUES (?,?,?,?,?)"
    valores = (IdProgramacion, Fecha,HoraInicio, HoraFin, Finalizado)
    cursor.execute(sentencia, valores)
    bd.commit()


crearTablas()
