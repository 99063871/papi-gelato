print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")

def papiGelatoFunc():
    global amount
    amount = input("Hoeveel bolletjes wilt u?")
    if amount <= "3":
        inWhat()
    elif amount >= "4" and amount <= "8":
        bakOfhoorn = 'bakje'
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
    elif another !="y" or another != "n":
        print("Sorry, dat snap ik niet...")
        orderMoreFunc()

def inWhat():
    global bakOfhoorn
    bakOfhoorn = input("Wilt u deze " + str(amount) + " bolletje(s) in \nA) een hoorntje of \nB) een bakje?")
    if bakOfhoorn != "a" and bakOfhoorn != "b":
        print("Sorry dat snap ik niet...")
        inWhat()
    else:
        if bakOfhoorn == "a":
            bakOfhoorn = "hoorntje"
        elif bakOfhoorn == "b":
            bakOfhoorn = 'bakje'
        orderMoreFunc()
        
papiGelatoFunc()