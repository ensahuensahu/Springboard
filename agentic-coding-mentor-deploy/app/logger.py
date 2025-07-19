import logging

def setup_logger():
    logger = logging.getLogger("agentic_logger")
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler("agentic_app.log")
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger
