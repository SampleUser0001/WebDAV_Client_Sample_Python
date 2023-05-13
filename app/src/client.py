from logging import getLogger, config, StreamHandler, DEBUG
import os

from logutil import LogUtil
from typing import Dict, List

from webdav3.client import Client

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
LOG_CONFIG_FILE = ['config', 'log_config.json']

logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(os.path.join(PYTHON_APP_HOME, *LOG_CONFIG_FILE))
config.dictConfig(log_conf)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

class WebDAVClient:
    def __init__(self, options: Dict[str, str]):
        self.client = Client(options)
        self.client.verify = True
    
    def set_verify(self, is_verify:bool) -> None:
        self.client.verify = is_verify

    def get_items(self, remotepath:str) -> List[str]:
        try:
            if self.check(remotepath = remotepath):
                items = self.client.list()
                if items == None:
                    return []
                else:
                    return items
            else:
                return []
        except Exception as e:
            logger.error(e.__sta)
            raise e
    
    def check(self, remotepath:str) -> bool:
        return self.client.check(remotepath)