import os
import pyautogui # Controlar el raton, tomar ss 
import webbrowser  # Para abrir paginas web
import time
from time import sleep # Detener la ejecicion
from datetime import date # Fecha
from datetime import datetime # Hora 
import administracionBaseDeDatos as BD # Base de .
from plyer import notification # Para mostrar notificaciones

# https://www.duolingo.com/stories/en-es-at-the-supermarket?practiceHubStory=featured
urlTemporal = "https://www.duolingo.com/stories/en-es-a-date?mode=read&practiceHubStory=featured"
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
        print("""DUOLINGO BOT V1.2""")
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
def notificacionGenerica(mensaje):
    notification.notify(
        title='DUO BOT',
        message=mensaje,
        app_icon="Imagenes\DuoIco_1.ico")

# para resolver los problemas en cada cuento
def resuelvePuntosSupensivos(resolviendoProblema):
    while resolviendoProblema:
        pyautogui.moveTo(400, 370)
        pyautogui.click()
        pyautogui.moveTo(400, 420)
        pyautogui.click()
        pyautogui.moveTo(400, 490)
        pyautogui.click()
        if str(pyautogui.locateOnScreen("Imagenes\Continuar.png", grayscale=False, confidence=.7)) != "None":
            resolviendoProblema = False
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
    sleep(1)
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
            pyautogui.press("ENTER")
            finalizar("200")
            print("GUARDADO")  
            pyautogui.click()
            pyautogui.hotkey("alt", "f4")
            sleep(2)
            print("TERMINADO") 
            webbrowser.open(urlTemporal, new=2, autoraise=True)
            sleep(1)
            pyautogui.press("F11")
            # espero hasta detectar unos segundos hasta que se cargue la pagina
            unaVez = False
            tiempoInicial = time.time()
            while True:
                # espero 30 segundos maximo para que cargue la pagina
                if time.time()-tiempoInicial <= 30 and unaVez == False:
                    # una vez se ve el cuento, dejo de esperar
                    if str(pyautogui.locateOnScreen("Imagenes\DetectarEmpezarCuento.png", grayscale=False, confidence=.7)) != "None":
                        unaVez = True
                        notificacionGenerica("INICIO Tiempo: "+str(time.time()-tiempoInicial)+" segundos")
                        break
                elif time.time()-tiempoInicial > 30:
                    # cierro la ventana
                    notificacionGenerica("INICIO Tiempo de espera excedido")
                    pyautogui.click()
                    pyautogui.hotkey("alt", "f4")
                    sleep(1)
                    webbrowser.open(urlTemporal, new=2, autoraise=True)
                    sleep(2)
                    pyautogui.press("F11")
                    tiempoInicial = time.time()

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
    # inicio
    pyautogui.click()
    pyautogui.hotkey("alt", "space")
    pyautogui.press("n")
    notificacionGenerica("Empezando")
    sleep(2) 
    # Tomar ss del bot y de Luja 
    # abro microsoft edge porque ahi esta la cuenta de luja
    edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    webbrowser.register("edge", None, webbrowser.BackgroundBrowser(edge_path))
    webbrowser.get("edge").open_new_tab(urlLujaPerfil)
    tiempoInicial = time.time()
    # espero hasta detectar se carge la pagina
    unaVez=False
    while True:
        # espero 30 segundos maximo para que cargue la pagina
        if time.time()-tiempoInicial<=30 and unaVez==False:
            # una vez se ve el perfil, dejo de esperar
            if str(pyautogui.locateOnScreen("Imagenes\PerfilLuja.png", grayscale=False, confidence=.7)) != "None":
                unaVez = True
                notificacionGenerica("LUJA Tiempo: "+str(time.time()-tiempoInicial)+" segundos")
                break
        elif time.time()-tiempoInicial > 30:    
            # cierro la ventana       
            notificacionGenerica("LUJA Tiempo de espera excedido")
            pyautogui.click()
            pyautogui.hotkey("alt", "f4")
            sleep(1)
            # la vuelvo a abrir
            webbrowser.get("edge").open_new_tab(urlLujaPerfil)
            # NOTA: EN LUGAR DE BREAK DEBE REINICIARSE EL TIEMPO
            break
    sleep(1)
    # tomo, guardo la ss y cierro la ventana
    ssBot = pyautogui.screenshot()
    ssBot.save("C:/DuoBot_Info/SsLuja/Sesion"+str(ultimaSesion) +
               "_"+str(fechaFormateada)+"_"+str(tiempoInicioF)+".png")
    pyautogui.hotkey("alt", "f4")
    sleep(1)
    # abro google porque ahi esta la cuenta del bot
    webbrowser.open(urlBotPerfil, new=2, autoraise=True) 
    tiempoInicial = time.time()
    unaVez = False
    while True:
        # espero 30 segundos maximo para que cargue la pagina
        if time.time()-tiempoInicial <= 30 and unaVez == False:
            # una vez se ve el perfil, dejo de esperar
            if str(pyautogui.locateOnScreen("Imagenes\PerfilBot.png", grayscale=False, confidence=.7)) != "None":
                unaVez = True
                notificacionGenerica(
                    "BOT Tiempo: "+str(time.time()-tiempoInicial)+" segundos")
                break
        elif time.time()-tiempoInicial > 30:
            # cierro la ventana
            notificacionGenerica("BOT Tiempo de espera excedido")
            pyautogui.click()
            pyautogui.hotkey("alt", "f4")
            sleep(1)
            # la vuelvo a abrir
            webbrowser.open(urlBotPerfil, new=2, autoraise=True)
            break
    sleep(1)
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
    # espero hasta detectar unos segundos hasta que se cargue la pagina
    unaVez = False
    tiempoInicial = time.time()
    while True:
        # espero 30 segundos maximo para que cargue la pagina
        if time.time()-tiempoInicial <= 30 and unaVez == False:
            # una vez se ve el cuento, dejo de esperar
            if str(pyautogui.locateOnScreen("Imagenes\DetectarEmpezarCuento.png", grayscale=False, confidence=.7)) != "None":
                unaVez = True
                notificacionGenerica(
                    "INICIO Tiempo: "+str(time.time()-tiempoInicial)+" segundos")
                break
        elif time.time()-tiempoInicial > 30:
            # cierro la ventana
            notificacionGenerica("INICIO Tiempo de espera excedido")
            pyautogui.click()
            pyautogui.press("F5")
            sleep(1)
            tiempoInicial = time.time()
    

def finalizar(mensaje):
    # Obtengo la fecha
    fecha = date.today()
    fechaFormateada = fecha.strftime("%d/%m/%Y")
    
    # Obtengo la hora final
    tiempoFinal = datetime.now()
    tiempoFinalF = tiempoFinal.strftime("%H:%M:%S")
    tiempoInicioF = tiempoInicio.strftime("%H:%M:%S")
    IdCuento = BD.obtenerUltimoCuento()
    
    BD.registroActividad(IdCuento, ultimaSesion, "A DATE", tiempoInicioF,
                         tiempoFinalF, fechaFormateada, mensaje)
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
            # "SeleccionarLosPares()" es quien hace el press enter final
            if str(pyautogui.locateOnScreen("Imagenes\Selecciona.png", grayscale=False, confidence=.7)) != "None" and bandera == False:
                bandera = True
                ResolviendoCuento=False
                seleccionaLosPares()

            # Detectar "PUNTOS SUSPENSIVOS" y "¿QUE ACABA DE SUCEDER?"
            if str(pyautogui.locateOnScreen("Imagenes\puntosSuspensivos.png", grayscale=False, confidence=.7)) != "None" or str(pyautogui.locateOnScreen("Imagenes\QueAcabaDeSuceder.png", grayscale=False, confidence=.7)) != "None" and bandera == False:
                bandera = True
                resolviendoProblema = True
                resuelvePuntosSupensivos(resolviendoProblema)
            
principal()


   
