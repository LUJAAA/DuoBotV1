# !/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pyautogui # Controlar el raton, tomar ss 
import webbrowser  # Para abrir paginas web
from time import sleep # Detener la ejecicion
from datetime import date # Fecha
from datetime import datetime # Hora 
import administracionBaseDeDatos as BD # Base de .
from plyer import notification # Para mostrar notificaciones

from win32api import (GetModuleFileName, RegCloseKey, RegDeleteValue,
                      RegOpenKeyEx, RegSetValueEx, RegEnumValue)
from win32con import (HKEY_LOCAL_MACHINE, HKEY_CURRENT_USER, KEY_WRITE,
                      KEY_QUERY_VALUE, REG_SZ)
from winerror import ERROR_NO_MORE_ITEMS
import pywintypes


urlTemporal = "https://www.duolingo.com/stories/en-es-a-date?mode=read&practiceHubStory=library"
urlBotPerfil = "https://www.duolingo.com/profile/LUJAV21"
urlLujaPerfil = "https://www.duolingo.com/profile/LujaXD1"
tiempoInicio = ""
tiempoFinal = ""
tiempoInicioF = ""
tiempoFinalF = ""
ultimaSesion = 0

def titulo():
    duoAnsii = """                ⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⡟⠋⠋⠉⠉⠛⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣫⣅⣴⠛⣧⠀⠀⠀⠙⢷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠃⠙⠃⠀⠘⣷⡀⠀⠀⠀⠈⠉⠛⠛⠓⠒⢒⣶⣶⠒⠚⠛⠛⠛⠛⠛⠙⠛⠶⣤⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣟⠁⠀⠀⠀⠀⠀⠈⢷⡄⠀⠀⠀⠀⠀⢀⣠⡶⠛⠁⢹⡀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠻⣦⣀⣀⣠⡴⠛⠁⠀⠀⠀⠈⠁⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣦⠀⠀⠀⠀⠀⠀⠀⠀⣿⠆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡇⠀⠀⠀⠀⠀⠀⢰⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⢸⡇⠉⠙⢻⣷⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣷⠀⠀⠀⠀⠀⠀⣾⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡿⠿⣇⠀⠀⠈⠻⢿⣿⠟⠉⠙⠳⣦⣰⣿⠛⢻⣶⣦⣤⣄⣀⡀⠀⠀⢸⡇⠀⠀⠀⠀⠀⢠⡏⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣾⡟⢷⡀⠙⠷⣤⣀⣠⡼⣷⣄⣀⣀⣀⣼⣿⡇⠀⠘⢿⣿⣿⣿⡿⠛⣷⠀⣿⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀
⠀⠀⠀⠀⠀⢠⡾⠻⠉⠀⠈⠛⠶⣭⣔⣤⣤⠾⡻⣿⣿⣿⣿⢿⡀⠻⣄⠀⠀⠈⠉⠁⣠⡾⠁⣸⠇⠀⠀⠀⠀⠀⢠⡏⠀⠀⠀
⠀⠀⠀⠀⠀⣾⠇⠀⠀⠘⢿⣦⣀⣀⣀⣀⣀⠀⠀⠈⠉⠉⠁⠈⠻⣤⡈⢛⣲⠶⠶⠚⠋⢀⣴⠏⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀
⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠻⣾⣍⠉⠛⠛⠿⢷⣶⣤⣀⠀⠀⠀⠈⠛⠳⠶⠶⠶⠶⠞⠋⠁⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠈⠿⣧⡀⠀⠀⠀⠀⠉⠛⠿⣶⣤⣀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠹⣧⡀⠀⠀⠀⠀⠀⠀⠙⣿⣦⠀⠀⠀⠀⠀⠀⠀⠙⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠳⣄⡀⠀⠀⠀⠀⠀⠈⠻⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠹⣷⡶⢖⢶⣶⣶⠾⠷⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣄⢆⠀⠀⠀⠀⠀⠙⢿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣄⠂⠀⠀⠀⠀⠀⠈⠛⢿⣶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠻⠿⠿⠃⢀⣠⡴⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⢤⣤⣀⣀⣀⣀⣀⣀⣤⣤⠶⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣶⣶⣶⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠈⣩⣽⣿⣶⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⢛⣿⣿⠿⠿⢿⠿⣿⡁⠀⠀⠀⠀⠀⠀⢘⣿⡿⠿⠿⠿⠿⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     """
    salirMenu = False
    while salirMenu == False:
        os.system('cls')
        print("""DUOLINGO BOT V1.1""")
        print("[1] INGRESAR FECHA [1]")
        print("[2] HACER CUENTOS  [2]")
        opcion = int(input())
        if opcion == 1:
            ingresarFecha()
        if opcion == 2:
            salirMenu = True
    
def ingresarFecha():
    os.system('cls')
    print("INGRESAR NUEVA FECHA")
    fecha = "08/02/8332"#str(input("FECHA -> "))
    horaInicio = "12:55"#str(input("HORA INICIO -> "))
    horaFinal = "13:55"  # str(input("HORA FINAL -> "))
    finalizado = "NO"
    IdProgramacion = BD.obtenerlaUltimaProgramacion()
    BD.registrarNuevaFecha(IdProgramacion, fecha,
                           horaInicio, horaFinal, finalizado)

def obtenerPosicionRaton():
    if str(input()) == "p":
        print(pyautogui.position())   

# para resolver los problemas en cada cuento
def completaLaOracion(resolviendoProblema):
    while resolviendoProblema:
        pyautogui.moveTo(700, 370)
        pyautogui.click()
        pyautogui.moveTo(700, 420)
        pyautogui.click()
        pyautogui.moveTo(700, 490)
        pyautogui.click()
        if str(pyautogui.locateOnScreen("Imagenes\Continuar.png", grayscale=False, confidence=.7)) != "None":
            resolviendoProblema=False
def seleccionaLosPares():
    sleep(2)
    realizando = True
    while realizando:
        # Primera palabra
        pyautogui.moveTo(540, 280)
        pyautogui.click()
        pyautogui.moveTo(900, 280) # par
        pyautogui.click()
        pyautogui.moveTo(540, 280)
        pyautogui.click()
        pyautogui.moveTo(900, 340)  # par
        pyautogui.click()
        pyautogui.moveTo(540, 280)
        pyautogui.click()
        pyautogui.moveTo(900, 410)  # par
        pyautogui.click()
        pyautogui.moveTo(540, 280)
        pyautogui.click()
        pyautogui.moveTo(900, 480) # par
        pyautogui.click()
        pyautogui.moveTo(540, 280)
        pyautogui.click()
        pyautogui.moveTo(900, 530)  # par
        pyautogui.click()
        # Segunda palabra
        pyautogui.moveTo(540, 340)
        pyautogui.click()
        pyautogui.moveTo(900, 280)  # par
        pyautogui.click()
        pyautogui.moveTo(540, 340)
        pyautogui.click()
        pyautogui.moveTo(900, 340)  # par
        pyautogui.click()
        pyautogui.moveTo(540, 340)
        pyautogui.click()
        pyautogui.moveTo(900, 410)  # par
        pyautogui.click()
        pyautogui.moveTo(540, 340)
        pyautogui.click()
        pyautogui.moveTo(900, 480)  # par
        pyautogui.click()
        pyautogui.moveTo(540, 340)
        pyautogui.click()
        pyautogui.moveTo(900, 530)  # par
        pyautogui.click()
        # Tercera palabra
        pyautogui.moveTo(540, 410)
        pyautogui.click()
        pyautogui.moveTo(900, 280)  # par
        pyautogui.click()
        pyautogui.moveTo(540, 410)
        pyautogui.click()
        pyautogui.moveTo(900, 340)  # par
        pyautogui.click()
        pyautogui.moveTo(540, 410)
        pyautogui.click()
        pyautogui.moveTo(900, 410)  # par
        pyautogui.click()
        pyautogui.moveTo(540, 410)
        pyautogui.click()
        pyautogui.moveTo(900, 480)  # par
        pyautogui.click()
        pyautogui.moveTo(540, 410)
        pyautogui.click()
        pyautogui.moveTo(900, 530)  # par
        pyautogui.click()
        # Cuarta palabra
        pyautogui.moveTo(540, 480)
        pyautogui.click()
        pyautogui.moveTo(900, 280)  # par
        pyautogui.click()
        pyautogui.moveTo(540, 480)
        pyautogui.click()
        pyautogui.moveTo(900, 340)  # par
        pyautogui.click()
        pyautogui.moveTo(540, 480)
        pyautogui.click()
        pyautogui.moveTo(900, 410)  # par
        pyautogui.click()
        pyautogui.moveTo(540, 480)
        pyautogui.click()
        pyautogui.moveTo(900, 480)  # par
        pyautogui.click()
        pyautogui.moveTo(540, 480)
        pyautogui.click()
        pyautogui.moveTo(900, 530)  # par
        pyautogui.click()
        # Quinta palabra
        pyautogui.moveTo(540, 530)
        pyautogui.click()
        pyautogui.moveTo(900, 280)  # par
        pyautogui.click()
        pyautogui.moveTo(540, 530)
        pyautogui.click()
        pyautogui.moveTo(900, 340)  # par
        pyautogui.click()
        pyautogui.moveTo(540, 530)
        pyautogui.click()
        pyautogui.moveTo(900, 410)  # par
        pyautogui.click()
        pyautogui.moveTo(540, 530)
        pyautogui.click()
        pyautogui.moveTo(900, 480)  # par
        pyautogui.click()
        pyautogui.moveTo(540, 530)
        pyautogui.click()
        pyautogui.moveTo(900, 530)  # par
        pyautogui.click()
        if str(pyautogui.locateOnScreen("Imagenes\Continuar.png", grayscale=False,  confidence=.7)) != "None":
            realizando = False
            pyautogui.press("ENTER")
            sleep(5)
            finalizar()
            print("GUARDADO")
            sleep(1)
            pyautogui.hotkey("alt", "f4")
            pyautogui.press("ENTER")
            print("TERMINADO") 
            webbrowser.open(urlTemporal, new=2, autoraise=True)
            sleep(2)
            pyautogui.press("F11")
def formaLaOracion(resolviendoProblema):
    while resolviendoProblema:
        pyautogui.moveTo(400, 430)
        pyautogui.click()
        pyautogui.moveTo(450, 430)
        pyautogui.click()
        pyautogui.moveTo(500, 430)
        pyautogui.click()
        pyautogui.moveTo(550, 430)
        pyautogui.click()
        pyautogui.moveTo(600, 430)
        pyautogui.click()
        pyautogui.moveTo(650, 430)
        pyautogui.click()
        pyautogui.moveTo(700, 430)
        pyautogui.click()
        pyautogui.moveTo(750, 430)
        pyautogui.click()
        pyautogui.moveTo(800, 430)
        pyautogui.click()
        pyautogui.moveTo(850, 430)
        pyautogui.click()
        pyautogui.moveTo(900, 430)
        pyautogui.click()
        if str(pyautogui.locateOnScreen("Imagenes\Continuar.png", grayscale=False, confidence=.7)) != "None":
            resolviendoProblema = False

# Al incio de cada sesion
def inicioSesion():       
    # Obtengo la fecha
    fecha = date.today()
    fechaFormateada = fecha.strftime("%d%m%Y")
    # Obtengo la hora
    global tiempoInicioF
    global tiempoInicio
    tiempoInicio = datetime.now()
    tiempoInicioF = tiempoInicio.strftime("%H%M%S")
    global ultimaSesion
    ultimaSesion = BD.obtenerUltimaSesion()

    # Tomar ss del bot y de Luja 
    # abro microsoft edge porque ahi esta la cuenta de luja
    edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    webbrowser.register("edge", None, webbrowser.BackgroundBrowser(edge_path))
    webbrowser.get("edge").open_new_tab(urlLujaPerfil)
    sleep(10) 
    # tomo, guardo la ss y cierro la ventana
    ssBot = pyautogui.screenshot()
    ssBot.save("C:/DuoBot_Info/SsLuja/Sesion"+str(ultimaSesion) +
               "_"+str(fechaFormateada)+"_"+str(tiempoInicioF)+".png")
    pyautogui.hotkey("alt", "f4")
    sleep(1)
    # abro google porque ahi esta la cuenta del bot
    webbrowser.open(urlBotPerfil, new=2, autoraise=True) 
    sleep(10)
    # tomo, guardo la ss y cierro la ventana
    ssBot = pyautogui.screenshot()
    ssBot.save("C:/DuoBot_Info/SsBot/Sesion"+str(ultimaSesion) +
               "_"+str(fechaFormateada)+"_"+str(tiempoInicioF)+".png")
    pyautogui.hotkey("alt", "f4")
    sleep(1)
    # Abro la pagina del cuento
    webbrowser.open(urlTemporal, new=2, autoraise=True)
    sleep(1)
    pyautogui.press("F11")
def finalizar():
    # Obtengo la fecha
    fecha = date.today()
    fechaFormateada = fecha.strftime("%d/%m/%Y")
    
    # Obtengo la hora final
    tiempoFinal = datetime.now()
    tiempoFinalF = tiempoFinal.strftime("%H:%M:%S")
    tiempoInicioF = tiempoInicio.strftime("%H:%M:%S")
    IdCuento = BD.obtenerUltimoCuento()
    
    BD.registroActividad(IdCuento, ultimaSesion, "A DATE", tiempoInicioF,
                         tiempoFinalF, fechaFormateada, "200")

def principal():
    ResolviendoCuento = False
    resolviendoProblema = False
    bandera=False

    titulo()
                
    inicioSesion()
    while True:

        # Detectar inicio de cuento
        if str(pyautogui.locateOnScreen("Imagenes\DetectarEmpezarCuento.png", grayscale=False, confidence=.7)) != "None" and ResolviendoCuento == False:
            pyautogui.press("ENTER")
            ResolviendoCuento = True
            # Obtengo la hora
            global tiempoInicioF
            global tiempoInicio
            tiempoInicio = datetime.now()
            tiempoInicioF = tiempoInicio.strftime("%H:%M:%S")
        while ResolviendoCuento:
            #########################
            # RESOLVIENDO EL CUENTO #
            #########################

            # Detectar continuar
            
            if str(pyautogui.locateOnScreen("Imagenes\Continuar.png", grayscale=False, confidence=.7)) != "None":
                pyautogui.press("ENTER")
                resolviendoProblema = False
                bandera = False

            # Detectar "COMPLETA LA ORACION"
            if str(pyautogui.locateOnScreen("Imagenes\Completa.png", grayscale=False, confidence=.7)) != "None" and bandera == False:
                bandera=True
                resolviendoProblema=True
                completaLaOracion(resolviendoProblema)

            # Detectar "FORMA LA ORACION"
            if str(pyautogui.locateOnScreen("Imagenes\Forma.png", grayscale=False, confidence=.7)) != "None" and bandera == False:
                bandera = True
                resolviendoProblema = True
                formaLaOracion(resolviendoProblema)

            # Detectar "SELECCIONA LOS PARES"
            # seleccionar pares es quien hace el press enter final
            if str(pyautogui.locateOnScreen("Imagenes\Selecciona.png", grayscale=False, confidence=.7)) != "None" and bandera == False:
                bandera = True
                ResolviendoCuento=False
                seleccionaLosPares()
        
        
principal()
def notificacion():
    notification.notify(
    title='DUO BOT',
    message='Si cuenta',
    app_icon="Imagenes\DuoIco_1.ico")



def principalPrueba():
    notificacion()
   



#principalPrueba()
