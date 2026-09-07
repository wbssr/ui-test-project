import logging
import os

def get_logger():
    if not os.path.exists("logs"):
        os.makedirs("logs")

    logger = logging.getLogger("ui_test")
    logger.setLevel(logging.INFO)

    # 控制台输出
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    # 文件输出
    file_handler = logging.FileHandler("logs/ui_test.log", encoding="utf-8")
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(file_handler)

    return logger

logger = get_logger()