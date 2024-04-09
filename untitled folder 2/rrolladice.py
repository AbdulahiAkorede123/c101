import random
response="y"
while response=="y":
    num=random.randint(1,6)
    if(num==1):
        print("1")
    if(num==2):
        print("2")
    if(num==3):
        print("3")
    if(num==4):
        print("4")
    if(num==5):
        print("5")
    if(num==6):
        print("6")
    response=input("press y to continue")
    print("\n")