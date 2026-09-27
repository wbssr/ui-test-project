import logging
import os
from datetime import datetime
def get_logger():
    log_dir="logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger("ui_test")
    logger.setLevel(logging.INFO)

    # 控制台输出
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    file_name=f"{log_dir}/test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    # 文件输出
    file_handler = logging.FileHandler(file_name, encoding="utf-8")
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(file_handler)

    return logger

logger = get_logger()