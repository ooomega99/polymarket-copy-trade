import yaml
from dataclasses import dataclass


@dataclass(frozen=True)
class ConfigTrader:
    address: str
    threshold: int
    purchase_amount: int
    slippage: int

    def __post_init__(self):
        # Validate address is a non-empty string
        if not isinstance(self.address, str) or not self.address:
            raise ValueError("address must be a non-empty string")

        # Validate threshold and purchase_amount are non-negative
        if self.threshold < 0:
            raise ValueError("threshold must be non-negative")
        if self.purchase_amount < 0:
            raise ValueError("purchase_amount must be non-negative")

        # Validate slippage is non-negative
        if self.slippage < 0:
            raise ValueError("slippage must be non-negative")


@dataclass(frozen=True)
class ConfigGrok:
    api_key: str
    model: str
    temperature: float


@dataclass(frozen=True)
class Config:
    private_key: str
    funder_address: str
    percent_sell: int
    traders: list[ConfigTrader]
    grok: ConfigGrok

    @staticmethod
    def load_yaml(file_path: str) -> 'Config':
        data: dict = yaml.safe_load(open(file_path, "r"))

        private_key: str = data.get("private_key", "")
        funder_address: str = data.get("funder_address", "")
        if not private_key:
            raise ValueError("private_key is required in configuration")
        if not funder_address:
            raise ValueError("funder_address is required in configuration")

        percent_sell: int = data.get("percent_sell", 0)
        # Validate percent_sell is between 0 and 100
        if not (0 <= percent_sell <= 100):
            raise ValueError("percent_sell must be between 0 and 100")

        traders: list = data.get("traders", [])
        if not traders:
            raise ValueError("No traders defined in configuration")

        return Config(
            private_key=private_key,
            funder_address=funder_address,
            percent_sell=percent_sell,
            traders=[ConfigTrader(**trader) for trader in traders],
            grok=ConfigGrok(**data.get("grok", {})),
        )
