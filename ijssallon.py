bolletjes = 0
horrentje = 0
bakje = 0

bolletjesPrijs = 1.10
horrentjePrijs = 1.25
bakjePrijs = 0.75

print("Welkom bij Papi Gelato.")

def welkeSmaakFunc():
    a=1
    for a in range(int(amount)):
        smaak = input("Welke smaak wilt u voor bolletje nummer "+ str(a) +"? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?").lower()
        if smaak != 'a' and smaak != 'c' and smaak != 'm' and smaak != 'v':
            print("Sorry dat snap ik niet...")
            welkeSmaakFunc()

def papiGelatoFunc():
    global amount
    global bolletjes
    global bakje
    amount = input("Hoeveel bolletjes wilt u?")
    bolletjes += int(amount)
    welkeSmaakFunc()
    if amount <= "3":
        inWhat()
    elif amount >= "4" and amount <= "8":
        bakOfhoorn = 'bakje'
        bakje +=1
        orderMoreFunc()
    elif amount > "8" and amount == int:
        print("Sorry, zulke grote bakken hebben we niet")
        papiGelatoFunc()
    else:
        print("Sorry dat snap ik niet...")
        papiGelatoFunc()

def orderMoreFunc():
    another = input("Hier is uw " + bakOfhoorn + " met " + amount + " bolletje(s). Wilt u nog meer bestellen? (Y/N)")
    if another == "y":
        papiGelatoFunc()
    elif another == "n":
        print("Bedankt en tot ziens!")
        bonnetje()
    elif another !="y" or another != "n":
        print("Sorry, dat snap ik niet...")
        orderMoreFunc()

def inWhat():
    global bakOfhoorn
    global horrentje
    global bakje
    bakOfhoorn = input("Wilt u deze " + str(amount) + " bolletje(s) in \nA) een hoorntje of \nB) een bakje?")
    if bakOfhoorn != "a" and bakOfhoorn != "b":
        print("Sorry dat snap ik niet...")
        inWhat()
    else:
        if bakOfhoorn == "a":
            bakOfhoorn = "hoorntje"
            horrentje += 1
        elif bakOfhoorn == "b":
            bakOfhoorn = 'bakje'
            bakje += 1
        orderMoreFunc()
        

def bonnetje():
    if bolletjes != 0:
        bolletjesTotal = bolletjes*bolletjesPrijs
        horrentjeTotal = horrentje*horrentjePrijs
        bakjeTotal = bakje*bakjePrijs
        total = bolletjesTotal + horrentje + bakjeTotal
        print('---------["Papi Gelato"]---------\n')
        print('Bolletjes     ',bolletjes, ' x €1.10   =€',bolletjesTotal)
        if horrentje != 0:
            print('horrentje     ',horrentje, ' x €1.25   =€',horrentjeTotal)
        elif bakje != 0:
            print('bakje         ',bakje, ' x €1.10   =€',bakjeTotal)
        print('                           -------- +')
        print('Totaal                      =€',total)
papiGelatoFunc()