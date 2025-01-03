import logging
import os

def setup_logger(name="root", log_file="logs/app.log", level=logging.INFO):
    """
    Configures a logger with both file and console handlers.

    Args:
        name (str): Name of the logger.
        log_file (str): Path to the log file.
        level (int): Logging level (e.g., logging.INFO, logging.DEBUG).

    Returns:
        logging.Logger: Configured logger instance.
    """
    # Ensure the logs directory exists
    log_dir = os.path.dirname(log_file)
    os.makedirs(log_dir, exist_ok=True)

    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Check if handlers already exist to avoid duplicate logs
    if not logger.handlers:
        # File handler for detailed logs
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)  # File logs capture DEBUG and above

        # Console handler for concise logs
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)  # Console logs capture INFO and above

        # Formatter for log messages
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

# Example usage
if __name__ == "__main__":
    logger = setup_logger(name="RossmannLogger", log_file="logs/rossmann_analysis.log", level=logging.DEBUG)
    logger.info("Logger setup complete.")
    logger.debug("This is a debug message.")
    logger.error("This is an error message.")