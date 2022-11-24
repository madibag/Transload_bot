import os

class Config(object):
	token = os.environ.get("TG_BOT_TOKEN", "") # Telegram Bot Token like >> "1116352147:AAFCW2thgkhzv0NutrkNDTByuAU6Q88RkUGzIg"
	TR_URL = os.environ.get("TR_URL","") # Transloader Url like >> https://five.rapidleech.gq/, https://aws.rapidleech.gq/
