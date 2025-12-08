from dataclasses import dataclass

@dataclass
class CopyTradeException(Exception):
    message: str

    def __str__(self) -> str:
        return self.message


@dataclass
class PredictException(Exception):
    message: str

    def __str__(self) -> str:
        return self.message


