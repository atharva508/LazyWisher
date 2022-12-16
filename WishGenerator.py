#This module generates a wish for the event and adds a random assortment of emojis
import emoji
import random
#Takes in a WishingDate object as a parameter and generates a wish
def getWish(event_details):
    wish = "Happy "
    if(isinstance(event_details.event,str) or (not math.isnan(event_details.event))):
        wish+= event_details.event
        wish+= " "
    if(isinstance(event_details.name,str) or (not math.isnan(event_details.name))):
        wish+= event_details.name
        wish+= " "
    if(isinstance(event_details.relation,str) or (not math.isnan(event_details.relation))):
        wish+= event_details.relation
    wish+=randomEmojis()
    return wish

# selects 2 emojis out of a list of 7 emojis appropriate for birthdays and anniversaries
def randomEmojis():
    emojiList = []
    emojiList.append("\U0001F618")
    emojiList.append("\U0001F973")
    emojiList.append("\U00002764")
    emojiList.append("\U0001F49B")
    emojiList.append("\U0001F339")
    emojiList.append("\U0001F389")
    emojiList.append("\U0001F38A")
    rand1 = random.randint(0,6)
    rand2 = rand1
    while(rand2==rand1):
        rand2 = random.randint(0,6)
    emojies = emojiList[rand1]+emojiList[rand1]+emojiList[rand2]+emojiList[rand2]
    return emojies
