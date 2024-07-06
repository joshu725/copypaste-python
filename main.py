# Librerías
import pyautogui, time, clipboard

# Se abre el archivo en modo lectura
f = open("texto.txt", "r", encoding="utf8")
# Tiempo de espera para colocar el puntero e iniciar
time.sleep(3)

# Bucle principal
for word in f:
    # Se copia una linea del archivo de texto
    clipboard.copy(word)
    # Se pega el texto
    pyautogui.hotkey('ctrl', 'v')
    # Tiempo de espera
    time.sleep(2)
    # Se envía
    pyautogui.press("enter")