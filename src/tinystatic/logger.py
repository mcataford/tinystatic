import logging


def get_logger(step: str):
    logging.basicConfig(level=logging.DEBUG)

    logger = logging.getLogger(step)
    logger.propagate = False
    log_handler = logging.StreamHandler()
    step_name = f"[{step}]".ljust(25)

    log_handler.setFormatter(
        logging.Formatter(fmt=f"{step_name} :: %(levelname)-8s :: %(message)s")
    )
    logger.addHandler(log_handler)

    return logger
