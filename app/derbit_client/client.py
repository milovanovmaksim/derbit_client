from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from derbit_client.ticker.ticker import StorageTicker


class Client:
    def __init__(self, ticker: "StorageTicker"):
        self.ticker = ticker

    async def run(self):
        await self.ticker.run()
