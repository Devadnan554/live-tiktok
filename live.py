from datetime import datetime
from colorama import Fore, Back, Style
linux = 'clear'
windows = 'cls'
import sys , os 
from TikTokLive  import TikTokLiveClient
from TikTokLive.types.events import ConnectEvent,  ViewerUpdateEvent , CommentEvent, DisconnectEvent ,LikeEvent ,LiveEndEvent,JoinEvent,ShareEvent,FollowEvent,GiftEvent,EnvelopeEvent
def live(username):
    os.system([linux, windows][os.name == 'nt'])
    client: TikTokLiveClient = TikTokLiveClient(unique_id=f"@{username}")
    print("===================================== "+ str(username))
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