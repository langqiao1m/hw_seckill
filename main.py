# -*- coding: utf-8 -*-
# !/usr/bin/python
import os
import signal

from selenium.common import WebDriverException, NoSuchWindowException

import constants
from huawei import HuaWei
from loguru import logger

from tools.my_logger import setup_logger


def main():
    huawei = HuaWei()
    try:
        huawei.start_process()
        huawei.stop_process()
    except NoSuchWindowException:
        logger.info("已关闭浏览器窗口，程序自动退出")
    except WebDriverException as we:
        logger.error("程序执行异常：except: {}", we)
    finally:
        if os.path.exists(constants.COOKIES_FILE):
            os.remove(constants.COOKIES_FILE)


if __name__ == '__main__':
    banner = """
        ooooo   ooooo                           .oooooo..o                     oooo    oooo  o8o  oooo  oooo  
        `888'   `888'                          d8P'    `Y8                     `888   .8P'   `"'  `888  `888  
         888     888  oooo oooo    ooo         Y88bo.       .ooooo.   .ooooo.   888  d8'    oooo   888   888  
         888ooooo888   `88. `88.  .8'           `"Y8888o.  d88' `88b d88' `"Y8  88888[      `888   888   888  
         888     888    `88..]88..8'   8888888      `"Y88b 888ooo888 888        888`88b.     888   888   888  
         888     888     `888'`888'            oo     .d8P 888    .o 888   .o8  888  `88b.   888   888   888  
        o888o   o888o     `8'  `8'             8""88888P'  `Y8bod8P' `Y8bod8P' o888o  o888o o888o o888o o888o                                                                                                                                                                             
    """
    setup_logger()
    logger.info(banner)
    try:
        main()
    except KeyboardInterrupt:
        logger.info("程序正常退出")
        exit(0)
