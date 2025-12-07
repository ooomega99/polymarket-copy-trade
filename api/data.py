from requests import Session, Response
from .models import Activity, Position


DATA_URL: str = "https://data-api.polymarket.com"


class Data:
    def __init__(self, session: Session) -> None:
        self.session: Session = session
        self.core: _DataCore = _DataCore(self.session)


class _DataCore:
    def __init__(self, session: Session) -> None:
        self.session: Session = session

    def activity(self, address: str, limit: int = 50, offset: int = 0, type: str="TRADE") -> list[Activity]:
        url: str = (f"{DATA_URL}/activity?user={address}"
                    f"&limit={limit}&offset={offset}&type={type}")
        response: Response = self.session.get(url)
        return [Activity(**activity) for activity in response.json()]

    def positions(
            self,
            address: str,
            sort_by: str = "CURRENT",
            sort_direction: str = "DESC",
            size_threshold: float = 0.1,
            limit: int = 100,
            offset: int = 0,
    ) -> list[Position]:
        url: str = (f"{DATA_URL}/positions?user={address}"
                    f"&sortBy={sort_by}&sortDirection={sort_direction}&sizeThreshold={size_threshold}"
                    f"&limit={limit}&offset={offset}")
        response: Response = self.session.get(url)
        return [Position(**position) for position in response.json()]
