
import sys
from pathlib import Path
from loguru import logger

# Define project root directory
ROOT_DIR = Path(__file__).resolve().parent.parent

# Define log directory
LOG_DIR = ROOT_DIR / "logs"

# Create logs directory if not exists
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Define log file
LOG_FILE = LOG_DIR / "application.log"

# Remove default logger
logger.remove()

# Console logging
logger.add(
    sys.stdout,
    level="INFO",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level: <8}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
           "<level>{message}</level>"
)

# File logging
logger.add(
    LOG_FILE,
    level="DEBUG",
    rotation="10 MB",
    retention="10 days",
    compression="zip",
    enqueue=True,
    backtrace=True,
    diagnose=False,
    format="{time:YYYY-MM-DD HH:mm:ss} | "
           "{level: <8} | "
           "{name}:{function}:{line} | "
           "{message}"
)

