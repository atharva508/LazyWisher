import pywhatkit
from datetime import datetime
def send_wish(grp_id,message):
    now_hour = datetime.now().hour
    now_minute = datetime.now().minute
    pywhatkit.sendwhatmsg_to_group("LfE5bH5JaFdF9roT4TZlzE",message,now_hour,now_minute+1)
