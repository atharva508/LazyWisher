#This program combines all the other modules to check the database and send a generated wish through whatsapp
#the program checks for events every 24 hours
import pandas as pd
from WishGenerator import getWish
from CheckForWish import checkDatabase
from WishingDate import WishingDate
from what_message import send_wish
import time

def main():
    while(True):
        
        wishes = checkDatabase()
        if(wishes.empty):
            print("NO WISHES FOR THE DAY")
        else:
            for row in wishes.index:
                currWish = WishingDate(wishes['Relation'][row],wishes['Name'][row],wishes['Event'][row],wishes['Day'][row],wishes['Month'][row])
                wish = getWish(currWish)
                print(wish)
                id = wishes['ID'][row]
                send_wish(id,wish)
        time.sleep(86400)


if __name__ == "__main__":
    main()

