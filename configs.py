# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "24928579"))
    API_HASH = getenv("API_HASH", "4e8991e8a9ae7aa37d6952d5b7ded2c5")
    BOT_TOKEN = getenv("BOT_TOKEN", "6959433815:AAElB7ZGDcq9MlAo-CZzxRnN3YWe06sUh0I")
    FSUB = getenv("FSUB", "mallu_x_videoz")
    CHID = int(getenv("CHID", "-1002078989135"))
    SUDO = list(map(int, getenv("SUDO", "6518276139").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://gunda1430:aYMUQOH4OS4QcQZO@cluster0.l5pmwpf.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
