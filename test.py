import logging
from time import sleep

from py_clob_client.client import ClobClient
from py_clob_client.constants import POLYGON

from config import Config
from database import Base, engine, Session
from predict import PolymarketPredict
from utils import setup_logging

setup_logging(log_file="data/predict.log", max_bytes=5 * 1024 * 1024, backup_count=5)
logger = logging.getLogger(__name__)

config: Config = Config.load_yaml("data/config.yaml")

Base.metadata.create_all(engine)
db_session = Session()

clob_client: ClobClient = ClobClient(
    host="https://clob.polymarket.com",
    chain_id=POLYGON,
    signature_type=1,
    key=config.private_key,
    funder=config.funder_address,
)
predict: PolymarketPredict = PolymarketPredict(
    db=db_session,
    grok=config.grok,
    clob_client=clob_client,
)

while True:
    predict.new()
    sleep(5)
