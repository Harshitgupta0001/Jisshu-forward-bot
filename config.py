from os import environ 

class Config:
    API_ID = environ.get("API_ID", "11721551")
    API_HASH = environ.get("API_HASH", "9a19f18dfe587666c928ffa1479d2d9c")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7154942008:AAFIL0YA8wswsffOZyGr-ZKsX3psZRSPdQM") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://Siam100:qvaFsAtmPPkZfVkq@siam100.m0mbgod.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forwardbot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7154942008').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
