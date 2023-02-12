import main
import aiogram

from loguru import logger

logger.info("__version__ = '0.1.0'")


if __name__ == '__main__':
    aiogram.executor.start_polling(main.dp, skip_updates=True)
