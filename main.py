import metadata
import os 
import art
import time
from loading import load


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def home():
    print("1. Order Coffee")
    print("2. Resource Report ")
    print("3. Turn off machine ")
    
def show_report():
    print(metadata.resources)


def is_sufficient(item: str ):
    coffee= metadata.MENU[item]
    result= True
    
    for res in coffee["ingredients"]:
        
        if coffee["ingredients"][res]>metadata.resources[res]:
            result=False
      
    
    return result

def input_notes():
    note_100=int(input("enter the amount of notes of 100: "))
    note_50=int(input("enter the amount of notes of 50: "))
    note_20=int(input("enter the amount of notes of 20: "))
    note_10=int(input("enter the amount of notes of 10: "))
    note_5=int(input("enter the amount of notes of 5: "))
    
    taka= [note_100,note_50,note_20,note_10,note_5]
    return taka


def change_calcu(taka: int):
    total=taka
    ager_resource=metadata.resources["notes"]
    note_100=0
    while metadata.resources["notes"]["100"]!=0:
        if taka<100:
            break
        metadata.resources["notes"]["100"]-=1
        taka-=100
        note_100+=1
    note_50=0
    while metadata.resources["notes"]["50"]!=0:
        if taka<50:
            break
        metadata.resources["notes"]["50"]-=1
        taka-=50
        note_50+=1
        
    note_20=0
    while metadata.resources["notes"]["20"]!=0:
        if taka<20:
            break
        metadata.resources["notes"]["20"]-=1
        taka-=20
        note_20+=1
    
    note_10=0
    while metadata.resources["notes"]["10"]!=0:
        if taka<10:
            break
        metadata.resources["notes"]["10"]-=1
        taka-=10
        note_10+=1
    
    note_5=0
    while metadata.resources["notes"]["5"]!=0:
        if taka<5:
            break
        metadata.resources["notes"]["5"]-=1
        taka-=5
        note_5+=1
        
    if note_5*5+note_10*10+note_20*20+note_50*50+note_100*100 ==total:
        notes=[note_100,note_50,note_20,note_10,note_5]
        return notes
    else:
        metadata.resources["notes"]=ager_resource
        notes=[]
        return notes
    
    
def total_money(array:list):
    sum=int(array[0]*100+array[1]*50+array[2]*20+array[3]*10+array[4]*5)
    return sum
    
def is_money_enough(taka: list,item: str):
    price=metadata.MENU[item]["cost"]
    if price > total_money(taka):
        return False
    else:
        return True
    
def process_cash(peysa: list):
    metadata.resources["notes"]["100"]+=peysa[0]
    metadata.resources["notes"]["50"]+=peysa[1]
    metadata.resources["notes"]["20"]+=peysa[2]
    metadata.resources["notes"]["10"]+=peysa[3]
    metadata.resources["notes"]["5"]+=peysa[4]
    
    metadata.resources["cash"]+=total_money(peysa)
        
def make_coffee(item: str):
    
    load(item)
    
    coffee= metadata.MENU[item]
    for mal in coffee["ingredients"]:
        metadata.resources[mal]-=coffee["ingredients"][mal]
    clear_terminal()
    art.show_art()
    print(f"\nyour {item} is ready ✅")
    time.sleep(4)
    
    
    
def serve_coffee(item:str):
    clear_terminal()
    art.show_art()
    print(f"\nHere is your {item}. Enjoy!!!!!!!")
    time.sleep(5)
    



#main function starts here

machine_status= "ON"

while machine_status=="ON":
    clear_terminal()
    art.show_art()
    home()
    choice= input("Choice: ")
    if choice=="1":
        coffee= input("What would you like? (espresso/latte/cappuccino):").lower()

        if not is_sufficient(coffee):
            print("Sorry there is no enough resources in the machine!!!!!!\nTRY AGAIN LATER")
            time.sleep(7)
            continue
        price = metadata.MENU[coffee]["cost"]
        print(f"\nthe {coffee} will cost {price} taka\n")
        
        pay=input("do you want to make payment(y/n): ").upper()
        bills=None
        
        if pay=="Y":
            bills=input_notes()
        else:
            print("\norder failed\nTRY AGAIN")
            time.sleep(7)
            continue
        
        if is_money_enough(bills,coffee)==True:
            change= total_money(bills)-price
            
            if change >0:
                notes= change_calcu(change)
                if len(notes)==0:
                    print("\nnot enough bills for the changes. MONEY REFUNDED")
                    time.sleep(5)
                    continue
                else:
                    clear_terminal()
                    art.show_art()
                    print("\nHere is your change")
                    print(f"100 tk notes : {notes[0]}")
                    print(f"50 tk notes : {notes[1]}")
                    print(f"20 tk notes : {notes[2]}")
                    print(f"10 tk notes : {notes[3]}")
                    print(f"5 tk notes : {notes[4]}")
        
            make_coffee(coffee)
            serve_coffee(coffee)
            time.sleep(5)
            
    elif choice=="2":
        show_report()
        time.sleep(11)
        continue
    
    else:
        machine_status="OFF"
        clear_terminal()
        art.show_art()
        print("turning off the machine in ")
        
        for x in range(3):
            print(f"\r{3-x}",end="",flush=True)
            time.sleep(1)
            
        clear_terminal()
        art.bye()
        continue
    