errorMessages = "Sorry dat is geen optie die we aanbieden..."

def zakelijk():
    global liter
    liter = input("Hoeveel liter(s) wilt u?")
    welkeSmaakFunc()
    bonnetje()
    
def welkeSmaakFunc():
    for a in range(1, int(liter) + 1):
        smaak = input("Welke smaak wilt u voor liter nummer "+ str(a) +"? A) Aardbei, C) Chocolade of V) Vanille?").lower()
        if smaak != 'a' and smaak != 'c' and smaak != 'm' and smaak != 'v':
            print(errorMessages)
            welkeSmaakFunc()

def bonnetje():
    price = int(liter)*9.80
    btw = price/109*9
    print('---------["Papi Gelato"]---------\n')
    print('Liter     ',liter, ' x €9.80   =€',round(price, 2))
    print('                           -------- +')
    print('Totaal                  = €',round(price ,2))
    print('BTW (9%)                = €',round(btw, 2))