from banner import banner
from colorama import Fore, Back, Style
import sys , os 
from datetime import datetime
from users import users
from TikTokLive  import TikTokLiveClient
from TikTokLive.types.events import ConnectEvent,  ViewerUpdateEvent , CommentEvent, DisconnectEvent ,LikeEvent ,LiveEndEvent,JoinEvent,ShareEvent,FollowEvent,GiftEvent,EnvelopeEvent
from add import add
from delete import deluser
linux = 'clear'
windows = 'cls'
banner()
do = int(input(Fore.BLUE+'''
Hi How Are You ? 
What You Want To Do ?
'''+Fore.RED+'''[ 1 ] '''+Fore.BLUE+'''Use Old Users 
'''+Fore.RED+'''[ 2 ] '''+Fore.BLUE+'''Add new User 
'''+Fore.RED+'''[ 3 ] '''+Fore.BLUE+'''Delete User
'''+Fore.RED+'''[ 4 ] '''+Fore.BLUE+'''Exit    \n==> '''))     
print("\n")
if do == 1:
    os.system([linux, windows][os.name == 'nt'])
    try:
        users()
    except FileNotFoundError:
        print("You have to add some users")
        exit()
    user = input("\nWhat is the user you want ? "+Fore.YELLOW+"( Write The User You Want )"+Fore.BLUE+"\n ==> ")
    with open("users.txt","r") as f:
         lines = f.readlines()
    with open("users.txt","r") as f:
        for line in lines:
            if line.strip("\n") == user:
                    client: TikTokLiveClient = TikTokLiveClient(unique_id=f"@{user}")
                    @client.on("connect")
                    async def on_connect(_: ConnectEvent):
                        now = datetime.now()
                        current_time = now.strftime("%I:%M:%S")
                        print(Fore.BLUE+"["+current_time+"] "+ Fore.GREEN  +"["+" ================== Connect For id room ================== ] ",client.room_id)
                    async def on_comment(event: CommentEvent): 
                        now = datetime.now()
                        current_time = now.strftime("%I:%M:%S")
                        print(Fore.BLUE+"["+current_time+"] "+"[ 🗯️ Comment from ] "+f"{event.user.unique_id}"+" | "+f"{event.user.nickname}-->  "+Fore.WHITE +f" {event.comment}")
                        client.add_listener("comment", on_comment)
                    @client.on("disconnect")
                    async def on_disconnect(event: DisconnectEvent):
                        now = datetime.now()
                        current_time = now.strftime("%I:%M:%S")
                        print(Fore.RED+"Disconnected")
                    @client.on("like")
                    async def on_like(event: LikeEvent):
                        now = datetime.now()
                        current_time = now.strftime("%I:%M:%S")
                        print(Fore.BLUE+"["+current_time+"] "+"[ 😍 Like from ] "+Fore.WHITE +f"{event.user.unique_id}"+" | "+f"{event.user.nickname}")
                    @client.on("live_end")
                    async def on_connect(event: LiveEndEvent):
                        print(f"Ended Live :(")
                    @client.on("join")
                    async def on_join(event: JoinEvent):
                        now = datetime.now()
                        current_time = now.strftime("%I:%M:%S")
                        print(Fore.BLUE+"["+current_time+"] "+"[ 🏃‍♂️ join ] "+Fore.WHITE +f"{event.user.unique_id}"+" | "+f"{event.user.nickname}")
                    @client.on("share")
                    async def on_share(event: ShareEvent):
                        now = datetime.now()
                        current_time = now.strftime("%I:%M:%S")
                        print(Fore.BLUE+"["+current_time+"] "+"[ 🚀 Shareing ] "+Fore.WHITE +f"{event.user.unique_id}"+" | "+f"{event.user.nickname}")
                    @client.on("follow")
                    async def on_follow(event: FollowEvent):
                        now = datetime.now()
                        current_time = now.strftime("%I:%M:%S")
                        print(Fore.BLUE+"["+current_time+"] "+"[  🫂  Add ] "+Fore.WHITE +f"{event.user.unique_id}"+" | "+f"{event.user.nickname}")
                    @client.on("gift")
                    async def on_gift(event: GiftEvent):
                        if event.gift.info.type <= 1:
                            now = datetime.now()
                            current_time = now.strftime("%I:%M:%S")
                            print(Fore.BLUE+"["+current_time+"] "+"[  🎁 Sent Gift ] "+Fore.WHITE +f"{event.user.unique_id}"+" | "+f"{event.user.nickname} --> {event.gift.info.name}")    
                    @client.on("viewer_update")
                    async def on_connect(event: ViewerUpdateEvent):
                        now = datetime.now()
                        current_time = now.strftime("%I:%M:%S")
                        print(Fore.BLUE+"["+current_time+"] [  👀  Viewer ] "+ Fore.WHITE, event.viewer_count)
                    if __name__ == '__main__':
                        client.run()
                        print(Style.RESET_ALL)
    print(Fore.RED+"The User You Write Not In list"+Style.RESET_ALL)
    exit()

elif do == 2:
    os.system([linux, windows][os.name == 'nt'])
    newuser = input("What is the new user you want ?\n==> ")
    add(newuser)
elif do == 3:
    os.system([linux, windows][os.name == 'nt'])
    users()
    user_del = input("\nWhat is the user you want delete ?\n==> ")
    deluser(user_del)
elif do == 4:
    os.system([linux, windows][os.name == 'nt'])
    banner()
    exit()