# -*- coding: utf-8 -*-
#封装log方法

import logging
import os
import time

LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}

logger = logging.getLogger()
level = 'default'

def create_file(filename):
    path = filename[0:filename.rfind('/')]
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.isfile(filename):
        fd = open(filename, mode='w', encoding='utf-8')
        fd.close()
    else:
        pass

def set_handler(levels):
    if levels == 'error':
        logger.addHandler(Log.err_handler)
    logger.addHandler(Log.handler)

def remove_handler(levels):
    if levels == 'error':
        logger.removeHandler(Log.err_handler)
    logger.removeHandler(Log.handler)
# def set_handler(levels):
#     if levels == 'error'or levels == 'warning':
#         logger.addHandler(Log.err_handler)
#     else:
#         logger.addHandler(Log.handler)
#
# def remove_handler(levels):
#     if levels == 'error' or levels == 'warning':
#         logger.removeHandler(Log.err_handler)
#     else:
#         logger.removeHandler(Log.handler)

def get_current_time():
    return time.strftime(Log.date, time.localtime(time.time()))

class Log:
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_file = path+'/log/{}-log.log'.format(time.strftime('%Y-%m-%d'))
    err_file = path+'/Log/{}-err.log'.format(time.strftime('%Y-%m-%d'))
    logger.setLevel(LEVELS.get(level, logging.NOTSET))
    create_file(log_file)
    create_file(err_file)
    date = '%Y-%m-%d %H:%M:%S'
    handler = logging.FileHandler(log_file, encoding='utf-8')
    err_handler = logging.FileHandler(err_file, encoding='utf-8')

    @staticmethod
    def debug(log_meg):
        set_handler('debug')
        logger.debug("[DEBUG " + get_current_time() + "]" + log_meg)
        remove_handler('debug')

    @staticmethod
    def info(log_meg):
        set_handler('info')
        logger.info("[INFO " + get_current_time() + "]" + log_meg)
        remove_handler('info')

    @staticmethod
    def warning(log_meg):
        set_handler('warning')
        logger.warning("[WARNING " + get_current_time() + "]" + log_meg)
        remove_handler('warning')

    @staticmethod
    def error(log_meg):
        set_handler('error')
        logger.error("[ERROR " + get_current_time() + "]" + log_meg)
        remove_handler('error')

    @staticmethod
    def critical(log_meg):
        set_handler('critical')
        logger.error("[CRITICAL " + get_current_time() + "]" + log_meg)
        remove_handler('critical')

if __name__ == "__main__":
    Log.debug("This is debug message")
    Log.info("This is info message")
    Log.warning("This is warning message")
    Log.error("This is error")
    Log.critical("This is critical message")