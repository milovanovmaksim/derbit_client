from datetime import datetime
from typing import Any, Optional
from aiohttp import ClientSession
from asyncio import gather, create_task, Task


class ListIndexName:
    def __init__(self, index_names: list[str]):
        self.index_names = index_names

    def _generate_url(self, index_name) -> str:
        url = f"https://test.deribit.com/api/v2/public/get_index_price?index_name={index_name}"
        return url

    async def _call_api(self, url, index_name) -> Optional[dict[str, Any]]:
        async with ClientSession() as session:
            async with session.get(url=url) as response:
                if response.status != 200:
                    return
                json_response = await response.json()
        result = json_response.get("result")
        timestamp = int(datetime.now().timestamp())
        return {"ticker": index_name,
                "price": result.get("index_price"),
                "timestamp": timestamp}

    async def run(self):
        tasks: list[Task] = []
        for index_name in self.index_names:
            url = self._generate_url(index_name)
            task = create_task(self._call_api(url=url, index_name=index_name))
            tasks.append(task)
        result = await gather(*tasks)
        return result
