import os
import time

numSanOption = [1,2,3,4,5]
numSanMenu = [1,2,3,4,5,6,7]
listahanSanOrders = [] ###variable kon diin i store an orders ###also known as "CART"
totalNaBaraydan = 0
gcashNumber = 9999999999
nameSanFile = "C:\\Python\\CASE\\feel_ko_pinaka_final\\revised\\resiboo.txt"

#for colors lang ini 
GREEN = "\033[0;32m"
RED = "\033[0;31m"
UNDERLINE = "\033[4m"
BOLD = "\033[1m"
LIGHT_CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
BLUE = "\033[0;34m"
BROWN = "\033[0;33m"
CYAN = "\033[0;36m"
PURPLE = "\033[0;35m"
BLINK = "\033[5m"
END = "\033[0m"

        ###lista san mga paninda###
listaSanPaninda = [
###numSanItem### ###pangaranSanItem###  ###presyo###
    ["1.", "SAGING NA UNIQUE", 10.00],
    ["2.", "PAN NA MAY PALAMAN", 15.00],
    ["3.", "KANGKONG CHIPS", 20.00],
    ["4.", "SAGING NA HILAW", 10.00],
    ["5.", "CHOKOLIT NA MANAMIT", 25.00],
    ["6.", "PANCAKE NA DILI MAINIT\b\b", 15.00],
    ["7.", "MATAM-IS NA KAMATIS", 10.00]
]


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def uloLawasTiil():
                                    ###ULO###
    print(GREEN + "\t ========================================================================")
    print("\t||" + UNDERLINE + BOLD + "\t\t\tSIMPLE SARI SARI STORE" + "\t\t\t\t" + "||")
    print(GREEN + "\t||\t\tDEVELOPERS: KEITH\tEZHAY\tYANESA\t\t\t||")
    print("\t||----------------------------------------------------------------------||" + END)
                                    ###LAWAS###
    for numSanItem, pangaranSanItem, presyo in listaSanPaninda:
        print(GREEN + "\t||" + BROWN + BOLD + f"\t\t{numSanItem} {pangaranSanItem}\t\t\t ₱{presyo:.2f}\t\t" + END + GREEN + "||") #f string, para makabutang san {} inside string
                                    ###TIIL###
    print("\t ========================================================================" + END)

   ###MAIN MENU###
def mainMenuOpsyon():
    print(LIGHT_CYAN + "\t\t\t ----------------------------------- ")
    print("\t\t\t**\t1. Mag Add to Cart\t\t\b\b\b\b\b**")
    print("\t\t\t**\t2. Mag Delete san Order\t\t\b\b\b\b\b**")
    print("\t\t\t**\t3. Kitaon an Cart\t\t\b\b\b\b\b**")
    print("\t\t\t**\t4. Mag bayad\t\t\t\b\b\b\b\b**")
    print("\t\t\t**\t5. I exit\t\t\t\b\b\b\b\b**")
    print("\t\t\t ----------------------------------" + END)

clearScreen()
start = input(RED + "\t\tpindota an ENTER para mag start.\n\n")
clearScreen()
time.sleep(3)
clearScreen()
uloLawasTiil()

while True:
    mainMenuOpsyon()
    opsyon = input(BROWN + "Nano an gusto mo?: ")
    if not opsyon.isdigit():
        print("number la an ibutang")
        continue

    else:
        opsyon = int(opsyon)
    
        if opsyon not in numSanOption:
            print("1-5 la po tabi")
            continue
                        
                        ### amo inin mangyayare kon pilion mo siya, este an number 1 ###
        if opsyon == 1:
            clearScreen()
            uloLawasTiil()
            order = int(input(GREEN + "Nano an gusto mo bakalon?: " + END))
            if order not in numSanMenu:
                print("1-7 lang tabi an ibutang. salamat")
                continue
            else:
                quantity = int(input("Pira kabilog an imo bakalon?: "))
                if quantity < 1:
                    print(RED + "\t\t\tPAG ORDER SAN TADONG." + END)
                    continue
                else:
                    ###hanapon an kon nano na item an gin bakal base sa order number na makikita sa list "listahanSanOrders"
                    aytem_na_gin_pili = listaSanPaninda[order -1]
                    pangaranSanItem = aytem_na_gin_pili[1] ###kaya 1 kay nasa index 1 sa listahanSanOrders makikita an name san item
                    presyo = aytem_na_gin_pili[2] ###kaya 2 kay para makuha an price sa listahanSanrders
                    listahanSanOrders.append((pangaranSanItem, quantity, presyo)) ###add sa cart

                    clearScreen()
                    print(YELLOW + " \t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print(f"\t\t||{pangaranSanItem} ({quantity} PC/S) naibutang na sa cart. ||") #fstring para makabutang san variables inside "" gamit an {}
                    print(" \t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + END)

                    file = open(nameSanFile, 'a')
                    if file.tell() == 0: #ina check kon may sulod na ba an txt file
                        file.write("===================================RESIBO===================================\n" + "\t\tITEM NAME" + " \t\t\t||\t" + "  QUANTITY" + "\t||\t PRICE" + "\t||\tSUBTOTAL" + "\n") #kon wara i pi print ini na header sa resibo txt file
                    aytemNumber = 1
                    subTotalNaBaraydan = quantity * presyo ###formula para ma compute an total na baraydan
                    totalNaBaraydan = totalNaBaraydan + subTotalNaBaraydan
                    file.write("\t" + pangaranSanItem + " \t\t||\t\t" + str(quantity) + "PC/S " + "\t||\tPHP" + str(presyo) + "\t||\t Php" + str(subTotalNaBaraydan) + "\n") #iprint sa resiboo.txt file 
                    file.close()
                    aytemNumber = aytemNumber + 1   

                        ### amo inin mangyayare kon pilion an option 2###
        elif opsyon == 2:
            if len(listahanSanOrders) == 0: #ina check kon may sulod na an list which is an listahansanorder na var, kon wara ipi print ini
                print(RED + "Wara kapa man san gin order." + END)
                continue
            else:
                orderNumber = 1
                for aytems in listahanSanOrders:
                    pangaranSanItem, quantity, presyo = aytems
                    print(str(orderNumber) + ". " + pangaranSanItem + " " + str(quantity) + " " + str(presyo))
                    orderNumber = orderNumber + 1 #increment by 1
                anIdedelete = int(input(RED + "Nano an idedelete? " + END)) - 1
            
                if anIdedelete < 0 or anIdedelete >= len(listahanSanOrders):
                    print(RED + "WARA SA LISTAHAN" + END)
                else:
                    deletedAytem = listahanSanOrders.pop(anIdedelete)
                    print(RED + "Deleted na an " + str(pangaranSanItem) + ". Salamat nala." + END)

                    file = open(nameSanFile, 'w')
                    if file.tell() == 0: 
                        file.write("===================================RESIBO===================================\n" + "\t\tITEM NAME" + " \t\t\t||\t" + "  QUANTITY" + "\t||\t PRICE" + "\t||\tSUBTOTAL" + "\n") # Header
                    for pangaranSanItem, quantity, presyo in listahanSanOrders:
                        totalNaBaraydan = quantity * presyo
                        file.write("\t" + pangaranSanItem + " \t\t||\t\t" + str(quantity) + "PC/S " + "\t||\tPHP" + str(presyo) + "\t||\t Php" + str(totalNaBaraydan) + "\n")
                    file.close()
                        
                        ### amo inin mangyayare kon pilion an option 3###
        elif opsyon == 3:
            clearScreen()
            if len(listahanSanOrders) == 0:
                print(RED + "\tWARA KA PA SAN MAY GIN BAKAL, PAG ADD TO CART ANAY." + END)
                continue
            else:
                clearScreen()
                print(BOLD + "\t\t\b\b\b\b================================CART==============================" + END)
                print(PURPLE + UNDERLINE + "\t\t\b\b\b\b\b\b\b/__________ITEM NAME__________________\b\b_QUANTITY_______________PRICE____\\" + END)
                for pangaranSanItem, quantity, presyo in listahanSanOrders:
                    print(GREEN + "\t||\t" + pangaranSanItem + " \t||\t" + str(quantity) + "PC/S " + "\t\t||\tPHP" + str(presyo) + "\t||\t" + END)
                print(YELLOW + "\t==========================================================================" + END)  
                        
                        ### amo inin mangyayare kon pilion an option 4###
        elif opsyon == 4:
            clearScreen()
            print(BLUE + BOLD + "\t\t !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("\t\t||\t\tPLS PAY Php" + str(totalNaBaraydan) + " to:  \t\t||")
            print(f"\t\t||\t\tGCASH: {gcashNumber}  \t\t||")
            print("\t\t ***********************************************" + END)
            refNum = input(YELLOW + "Ibutang an Reference Number: ")
            clearScreen()
            print("Salamat!")
            time.sleep(2)
            clearScreen()
            print("Wait la.")
            time.sleep(1)
            clearScreen()
            print("Wait la...")
            time.sleep(2)
            clearScreen()
            print("Wait la.......")
            time.sleep(1)
            clearScreen()
            print(GREEN + BOLD + "\t\tBAYAD KANA! HULATA NALA AN ORDER MO. SALAMAT!" + END)

                        ### amo inin mangyayare kon pilion an option 5###
        elif opsyon == 5:
            clearScreen()
            print(GREEN + BOLD + "Salamat sa Pagbakal!" + END)
            time.sleep(3)
            print(RED + "miss u" + END)
            exit()

    ###<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        #salamat chatgpt na ada kon kinahanglan namon haha
        #last update: april 28, 2024, 4: 26 PM