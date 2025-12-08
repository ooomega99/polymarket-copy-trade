from typing import List

from requests import Session, Response

from api.data import Data
from api.gamma import Gamma
from api.models import PageEvent, PolymarketNewResponse


class PolymarketApi:
    def __init__(self) -> None:
        self._session: Session = Session()

        self.gamma: Gamma = Gamma(self._session)
        self.data: Data = Data(self._session)

    def new(self) -> List[PageEvent]:
        url: str = "https://polymarket.com/_next/data/P9DlsQYEXrOnpTSzhF8sO/new.json?category=new"
        response: Response = self._session.get(url)

        print(response.text)

        new: PolymarketNewResponse = PolymarketNewResponse(**response.json())
        return new.page_props.dehydrated_state.queries[0].state.data.pages[0].events
