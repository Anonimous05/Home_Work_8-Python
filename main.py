from colorama import Fore, Back, Style

while True:
    try:
        gp_Or_ap = input(Style.NORMAL + Back.BLACK + Fore.LIGHTGREEN_EX + "введите: \nгп - для выбора Геометрической прогрессии \nап - для выбора Арифметической прогрессии\n")

        if gp_Or_ap.lower() != "гп" and gp_Or_ap.lower() != "ап":
            print("Такой операции нет!")
            break

        b = int(input(Style.BRIGHT + "Введите B1: "))
        bn = int(input(Style.BRIGHT + "Введите Bn: "))
        q = int(input(Style.BRIGHT + "Введите q: "))

        mass = [b]

        for i in range(bn - 1):
            if gp_Or_ap.lower() == "гп":
                mass.append(mass[len(mass) - 1] * q)
            elif gp_Or_ap.lower() == "ап":
                mass.append(mass[len(mass) - 1] + q)
        for j in range(len(mass)):
            print(Back.WHITE + Fore.BLACK + f"B{j + 1} - {mass[j]}")
        continueOperation = input(Back.BLACK + Fore.WHITE + "\n Еще раз? (нет) - n или N: ")
        if continueOperation.lower() == "n":
            print("Пока!")
            break

    except ValueError:
        print("Введите число а не букву или слово!")