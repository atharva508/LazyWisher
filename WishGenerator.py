import emoji
import random
def getWish(event_details):
    wish = "Happy "
    wish+= event_details.event
    wish+= " "
    wish+= event_details.name
    wish+= " "
    wish+=event_details.relation
    wish+=randomEmojis()
    return wish

def randomEmojis():
    emojiList = []
    '''
    emojiList.append(emoji.emojize(":smiling_face_with_heart-eyes:"))
    emojiList.append(emoji.emojize(":partying_face:"))
    emojiList.append(emoji.emojize(":red_heart:"))
    emojiList.append(emoji.emojize(":yellow_heart:"))
    emojiList.append(emoji.emojize(":rose:"))
    emojiList.append(emoji.emojize(":confetti_ball:"))
    emojiList.append(emoji.emojize(":party_popper:"))
    '''
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