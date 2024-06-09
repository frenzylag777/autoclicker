import keyboard
import mouse
import time
import os

def change():
    global work
    work = not work

inputing = False
def changeinput():
    global inputing
    inputing = not inputing

interval = 0.1
interval2 = 0
def intervalchange():
    print("Текущая задержка:")
    print("Укажите задержку клика (в секундах)")
    global interval
    global interval2
    changeinput()
    interval2 = float(input(">>> "))
    if interval2 > 0:
        interval = interval2
    changeinput()

status = "AutoClicker by FrenzyLag v1.0-beta Статус: Не кликаем"
def printver():
    os.system('cls')
    print(status)
    print(" ")
    print("F6 - вкл/выкл автокликер")
    print("F7 - Указать задержку клика (БЕТА, НЕ НАЖИМАТЬ)")
    print(" ")
    print("Текущая задержка клика:", interval)
    print(" ")
    print(" ")
    print(" ")
    print("Может, всё таки лучше использовать другую альтернативу?")


work = False
keyboard.add_hotkey('f6', change)
keyboard.add_hotkey('f7', intervalchange)
printver()
while True:
    if inputing == False:
        if work:
            mouse.click(button='left')
            status = "AutoClicker by FrenzyLag v1.0-beta Статус: Кликаем"
        printver()
        status = "AutoClicker by FrenzyLag v1.0-beta Статус: Не кликаем"
        time.sleep(interval)

