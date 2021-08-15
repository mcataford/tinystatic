import logging


def get_logger(step: str):
    logging.basicConfig(level=logging.DEBUG)

    logger = logging.getLogger(step)
    logger.propagate = False
    logHandler = logging.StreamHandler()
    step_name = f"[{step}]".ljust(25)

    logHandler.setFormatter(
        logging.Formatter(fmt=f"{step_name} :: %(levelname)-8s :: %(message)s")
    )
    logger.addHandler(logHandler)

    return logger
