#this module checks the file to see if any events coicide with the current day
import pandas as pd
from datetime import date

def checkDatabase():
    today_day = date.today().day
    today_month =date.today().month
    family_data = pd.read_csv('family_Data.csv')
    family_data = family_data[(family_data['Month'] == today_month) & (family_data['Day'] == today_day)]
    return family_data
    
if __name__ == "__main__":
    checkDatabase()
