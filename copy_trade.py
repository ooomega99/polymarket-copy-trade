import logging
from time import sleep

from config import Config
from copy_trade import PolymarketCopyTrade
from database import Base, engine, Session
from utils import setup_logging


setup_logging(log_file="data/log.log", max_bytes=5 * 1024 * 1024, backup_count=5)
logger = logging.getLogger(__name__)


def main():
    config: Config = Config.load_yaml("data/config.yaml")

    Base.metadata.create_all(engine)
    db_session = Session()

    copy_trade: PolymarketCopyTrade = PolymarketCopyTrade(
        db=db_session,
        private_key=config.private_key,
        funder_address=config.funder_address,
        percent_sell=config.percent_sell,
        traders=config.traders,
    )

    logger.info("Starting worker loop...")

    while True:
        try:
            copy_trade.run()
        except Exception as e:
            logger.exception("Error running fetch(): %s", e)

        sleep(5) # Sleep for 5 seconds before the next iteration


if __name__ == "__main__":
    main()

