import time

print("plz insert your card")
time.sleep(5)
spin = int(input("set your pin"))
time.sleep(2)
password = spin

pin = int(input("enter your pin"))

blance = 5000
if pin == password:
    while True:
        print("""
        1=blance
        2=withdraw blance
        3= exit
        """)

        try:
            option = int(input("please enter your choice"))
        except:
            print("wrong option")

        if option == 1:
            print(f"your blance is {blance}")
            time.sleep(5)

        if option == 2:
            wda = int(input("enter your withdraw amount"))
            time.sleep(2)
            if wda > blance:
                print("you have insaficiant blance")
                print("please try again")
                time.sleep(2)
            else:
                blance = blance - wda
                print(f"{wda}is debited from your account")
                print(f"your current blance is {blance}")
                time.sleep(2)

        if option == 3:
            break
else:
    print("invalite PIN")