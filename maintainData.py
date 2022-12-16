#you can use this program to add records in your csv file, however i suggest that you enter you data manually in the CSV.
from WishingDate import WishingDate
import csv

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
        
if __name__== "__main__":
    add_to_Collection()
