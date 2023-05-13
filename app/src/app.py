# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG
import os

from logutil import LogUtil
from importenv import ImportEnvKeyEnum

from client import WebDAVClient

from util.sample import Util

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

if __name__ == '__main__':
    # 起動引数の取得
    # args = sys.argv
    # args[0]はpythonのファイル名。
    # 実際の引数はargs[1]から。

    options = {
        'webdav_hostname': ImportEnvKeyEnum.WEBDAV_URL.value,
        'webdav_login':    ImportEnvKeyEnum.WEBDAV_ID.value,
        'webdav_password': ImportEnvKeyEnum.WEBDAV_KEY.value
    }
    logger.debug(f'key : webdav_hostname , value : {options["webdav_hostname"]}')
    logger.debug(f'key : webdav_login , value : {options["webdav_login"]}')

    client = WebDAVClient(options)
    remotepath = ''
    logger.info(f'remotepath : {remotepath}, {client.check(remotepath)}')
    for v in client.get_items(remotepath):
        logger.info(f'item : {v}')
        
