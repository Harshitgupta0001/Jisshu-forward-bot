from os import environ 

class Config:
    API_ID = environ.get("API_ID", "21551881")
    API_HASH = environ.get("API_HASH", "6e83e9e1aee5accd4868dc29aa59ebaa")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7092980872:AAFBjX87iiFT_KpUher6vEslGeTxOKY_ZGg") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://david:surya@cluster0.s7o0tyw.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forwardbot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7137515870').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
