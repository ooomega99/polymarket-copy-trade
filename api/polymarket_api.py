from requests import Session

from api.data import Data
from api.gamma import Gamma


class PolymarketApi:
    def __init__(self) -> None:
        self._session: Session = Session()

        self.gamma: Gamma = Gamma(self._session)
        self.data: Data = Data(self._session)
