# This file is a part of FileStreamBot

from os import environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    MULTI_CLIENT = False
    API_ID = int(environ.get("API_ID", "10956858"))
    API_HASH = str(environ.get("API_HASH", "cceefd3382b44d4d85be2d83201102b7"))
    BOT_TOKEN = str(environ.get("BOT_TOKEN", "5962717194:AAEpOug66r8gHfjikLaAWGGKvNbIYBGvCbA"))
    SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))  # 1 minte
    WORKERS = int(environ.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    BIN_CHANNEL = int(
        environ.get("BIN_CHANNEL", "-1001621737126")
    )  # you NEED to use a CHANNEL when you're using MULTI_CLIENT
    PORT = int(environ.get("PORT", 8080))
    BIND_ADDRESS = str(environ.get("WEB_SERVER_BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    HAS_SSL = environ.get("HAS_SSL", None)
    HAS_SSL = "True"
    HAS_SSL = True if str(HAS_SSL).lower() == "true" else False
    NO_PORT = environ.get("NO_PORT", False)
    NO_PORT = True if str(NO_PORT).lower() == "true" else False
    if "DYNO" in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(environ.get('FQDN', BIND_ADDRESS)) if not ON_HEROKU or environ.get('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(environ.get('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)

    FQDN = "file-to-link-ds-botz.osc-fr1.scalingo.io"
    DATABASE_URL = str(environ.get('DATABASE_URL', "mongodb+srv://Irfan:786or786@cluster0.2jjhd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"))
    UPDATES_CHANNEL = str(environ.get('UPDATES_CHANNEL', "DS_Botz"))
    PAGE_LINK = environ.get('PAGE_LINK', None)
    OWNER_ID = int(environ.get('OWNER_ID', '1125671241'))
    SESSION_NAME = str(environ.get('SESSION_NAME', 'F2LxBot'))
    FORCE_UPDATES_CHANNEL = environ.get('FORCE_UPDATES_CHANNEL', False)
    FORCE_UPDATES_CHANNEL = True if str(FORCE_UPDATES_CHANNEL).lower() == "true" and UPDATES_CHANNEL != 'aredirect' else False

    BANNED_CHANNELS = list(set(int(x) for x in str(environ.get("BANNED_CHANNELS", "-1001296894100")).split()))
    FORCE_UPDATES_CHANNEL = "True"

