
from WishingDate import WishingDate
import csv
from WishGenerator import getWish

def add_to_Collection():
    answer = "yes"
    filename = 'family_Data.csv'
    header = ["Name","Relation","Event","Month","Day"]
    data = []
    while(answer!="no"):
        event = input("Enter Event : ")
        name  = input("Enter name : ")
        relation  = input("Enter relation : ")
        month  = int(input("Enter event month : "))
        day  = int(input("Enter event day : "))
        answer = input("do you wish to enter any dates: ")

    with open(filename, 'a', newline="") as file:
        csvwriter = csv.writer(file) 
        csvwriter.writerows(data) 
        
