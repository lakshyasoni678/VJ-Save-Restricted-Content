import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7415405703:AAGGGCgvldr3KIf6Agj9vituKJAz4gWM0H8")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29640188"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "e470abc84a3bc445997ee4ea5be87deb")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://syangshibo1:mongodbdatabase500@cluster0.vtkrte7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
