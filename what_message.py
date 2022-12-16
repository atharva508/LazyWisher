#This file handles the process of sending the message to whatsapp using the groupID/phoneNo. and the generated message
import pywhatkit
from datetime import datetime
def send_wish(grp_id,message):
    now_hour = datetime.now().hour
    now_minute = datetime.now().minute
    pywhatkit.sendwhatmsg_to_group(grp_id,message,now_hour,now_minute+2,15,True,5)
