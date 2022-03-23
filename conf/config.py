import logging


BACKEND = 'SlackV3'  # Errbot will start in text mode (console only mode) and will answer commands from there.

BOT_IDENTITY = {
        'token': 'your bot user auth token' }
BOT_DATA_DIR = r'/opt/errbot/data'
BOT_EXTRA_PLUGIN_DIR = r'/opt/errbot/plugins'
BOT_EXTRA_BACKEND_DIR="/opt/errbot/backend"

BOT_LOG_FILE = r'/opt/errbot/errbot.log'
BOT_LOG_LEVEL = logging.DEBUG

BOT_ADMINS = ('@yourslackadminusername', )  # !! provide a username which want to be a admin of this bot