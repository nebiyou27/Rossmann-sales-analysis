import logging

# Configure root logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Adjust logging level as needed

# Create a file handler for detailed logs
file_handler = logging.FileHandler('logs/app.log')
file_handler.setLevel(logging.DEBUG)  

# Create a console handler for concise output
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)