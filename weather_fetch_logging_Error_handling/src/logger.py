import logging

def get_logger(log_file: str = "weather.log"):
    logger = logging.getLogger("weather_fetcher")

    # prevent dulicate handlers 
    if logger.handlers:
        return logger
    
    logger.setLevel(logging.INFO)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
  
    # Create file handler -> write everything to weather.log
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # (Optional but recommended) Console output too
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger