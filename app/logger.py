import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

def setup_logger(name: str):
    logger = logging.getLogger(name)
    log_path = Path('logs')
    info_log_path = f'{name}_info.log'
    error_log_path = f'{name}_error.log'

    log_path.mkdir(parents=True, exist_ok=True)
    logger.setLevel(logging.DEBUG)

    # 日志格式
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # ERROR 文件 handler
    error_handler = TimedRotatingFileHandler(f'{log_path}/{error_log_path}', when="midnight", backupCount=7,
                                             encoding="utf-8")
    error_handler.setLevel(logging.ERROR)
    error_handler.addFilter(lambda record: record.levelno == logging.ERROR)
    error_handler.setFormatter(formatter)

    # INFO 文件 handler
    info_handler = TimedRotatingFileHandler(f'{log_path}/{info_log_path}', when="midnight", backupCount=7,
                                            encoding="utf-8")
    info_handler.setLevel(logging.INFO)
    info_handler.addFilter(lambda record: record.levelno == logging.INFO)
    info_handler.setFormatter(formatter)

    # 控制台 handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # 控制台只显示 INFO 及以上
    console_handler.setFormatter(formatter)

    # 添加 handlers
    logger.addHandler(error_handler)
    logger.addHandler(info_handler)
    logger.addHandler(console_handler)
    return logger
