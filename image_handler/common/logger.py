import logging


def get_logger(logger_name, logging_level):
    """logger function"""
    try:
        if logging_level.lower() == "debug":
            level = logging.DEBUG
        elif logging_level.lower() == "info":
            level = logging.INFO
        elif logging_level.lower() == "warning":
            level = logging.WARNING
        else:
            level = logging.ERROR
        logger = logging.getLogger(logger_name)
        logger.setLevel(level)
        console = logging.StreamHandler()
        console.setLevel(level=level)
        formatter = logging.Formatter('%(levelname)s : %(message)s')
        console.setFormatter(formatter)
        logger.addHandler(console)
        return logger
    except Exception as e:
        print(f'Error occured in common.logger.get_logger: {e}')
        return None
