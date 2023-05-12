from pyrogram import Client , filters 
from pyrogram.types import Message ; from pyrogram.enums import MessageMediaType
import os  , shutil

Acc = Client("Account"  , "Api id" , "Api Hash")



@Acc.on_message()
def All(Client , m:Message):
    if m.media :
        if m.media == MessageMediaType.PHOTO and m.photo.ttl_seconds :
            try:fileid = m.photo.file_id;Acc.download_media(fileid , "Temp/");dir_list = os.listdir("Temp");Acc.send_photo("me" , f"Temp/{dir_list[0]}" )
            except:pass
            finally :shutil.rmtree("Temp")
        if m.media == MessageMediaType.VIDEO and m.video.ttl_seconds :
            try:fileid = m.video.file_id;Acc.download_media(fileid , "Temp/");dir_list = os.listdir("Temp");Acc.send_video ("me" , f"Temp/{dir_list[0]}" )
            except:pass
            finally :shutil.rmtree("Temp")
            
Acc.run()