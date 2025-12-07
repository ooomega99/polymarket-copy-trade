from requests import Session, Response
from .models import EventDetail
from .models import MarketDetail


GAMMA_URL: str = "https://gamma-api.polymarket.com/"


class Gamma:
    def __init__(self, session: Session) -> None:
        self.session: Session = session

        self.event: _GammaEvent = _GammaEvent(self.session)
        self.market: _GammaMarket = _GammaMarket(self.session)


class _GammaEvent:
    def __init__(self, session: Session) -> None:
        self.session: Session = session

    def by_id(self, id: str) -> EventDetail:
        url: str = f"{GAMMA_URL}/events/{id}"
        response: Response = self.session.get(url)
        return EventDetail(**response.json())

    def by_slug(self, slug: str) -> EventDetail:
        url: str = f"{GAMMA_URL}/events/slug/{slug}"
        response: Response = self.session.get(url)
        return EventDetail(**response.json())


class _GammaMarket:
    def __init__(self, session: Session) -> None:
        self.session: Session = session

    def by_id(self, id: str) -> MarketDetail:
        url: str = f"{GAMMA_URL}/markets/{id}"
        response: Response = self.session.get(url)
        return MarketDetail(**response.json())

    def by_slug(self, slug: str) -> MarketDetail:
        url: str = f"{GAMMA_URL}/markets/slug/{slug}"
        response: Response = self.session.get(url)
        return MarketDetail(**response.json())
