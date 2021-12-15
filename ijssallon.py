import zakelijk

bolletjes = 0
horrentje = 0
bakje = 0

bolletjesPrijs = 1.10
horrentjePrijs = 1.25
bakjePrijs = 0.75

toppingTotal = 0
toppingTotalPrice = 0
slagroomprice = 0.50
sprinkelsprice = 0.30

print("Welkom bij Papi Gelato.")
def whoFunc():
    who = input("Bent u 1) particulier of 2) zakelijk?")
    if who == "1":

        def welkeSmaakFunc():
            
            for a in range(1, int(amount) + 1):
                smaak = input("Welke smaak wilt u voor bolletje nummer "+ str(a) +"? A) Aardbei, C) Chocolade, M) Munt of V) Vanille?").lower()
                if smaak != 'a' and smaak != 'c' and smaak != 'm' and smaak != 'v':
                    print("Sorry dat snap ik niet...")
                    welkeSmaakFunc()

        def papiGelatoFunc():
            global amount
            global bolletjes
            global bakje
            global bakOfhoorn
            amount = input("Hoeveel bolletjes wilt u?")
            bolletjes += int(amount)
            welkeSmaakFunc()
            if amount <= "3":
                inWhat()
            elif amount >= "4" and amount <= "8":
                bakOfhoorn = 'bakje'
                bakje +=1
                toppingFunc()
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
                    toppingFunc()
                elif bakOfhoorn == "b":
                    bakOfhoorn = 'bakje'
                    bakje += 1
                    toppingFunc()
                orderMoreFunc()
                
        def toppingFunc():
            global toppingTotal
            global toppingTotalPrice
            topping = input("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?").lower()
            if topping != "a":
                if topping == "b":
                    toppingTotalPrice += slagroomprice
                    toppingTotal +=1
                elif topping == "c":
                    toppingTotalPrice += sprinkelsprice * bolletjes
                    toppingTotal +=1
                elif topping == "d":
                    toppingTotal +=1
                    if bakOfhoorn == "hoorntje":
                        toppingTotalPrice += 0.60
                    elif bakOfhoorn == "bakje":
                        toppingTotalPrice += 0.90
                else:
                    print("Sorry dat snap ik niet...")
                    toppingFunc()

        def bonnetje():
            if bolletjes != 0:
                bolletjesTotal = bolletjes*bolletjesPrijs
                horrentjeTotal = horrentje*horrentjePrijs
                bakjeTotal = bakje*bakjePrijs
                total = bolletjesTotal + horrentje + bakjeTotal
                print('---------["Papi Gelato"]---------\n')
                print('Bolletjes     ',bolletjes, ' x €1.10   =€',round(bolletjesTotal, 2))
                if horrentje != 0:
                    print('Horrentje     ',horrentje, ' x €1.25   =€',round(horrentjeTotal, 2))
                elif bakje != 0:
                    print('Bakje         ',bakje, ' x €1.10   =€',round(bakjeTotal, 2))
                if toppingTotal != 0:
                    print('Topping        1  x €', toppingTotalPrice,   '  =€',round(toppingTotalPrice, 2))
                    
                print('                           -------- +')
                print('Totaal                      =€',round(total, 2))

        papiGelatoFunc()

    elif who == "2":
        zakelijk.zakelijk()
    else:
        print("Sorry dat snap ik niet...")
        whoFunc()

whoFunc()