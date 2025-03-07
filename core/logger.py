import logging
from datetime import datetime

def setup_logger():
    """Konfiguriert das Logging-System für das Framework"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.FileHandler("worm_simulator.log"),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger("WormSimulator")
    return logger

# Erstelle den Logger beim Import
logger = setup_logger()