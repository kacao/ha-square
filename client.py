import aiohttp
import asyncio

class Client:

    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            'Authorization': 'Bearer %s' % config["api_key"],
            'Content-Type': 'application/json'
        }
 
    async def get(self, url, params):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers, params=params) as res:
                return await res.json()

    async def post(self, url, payload):
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=self.headers, data=payload) as res:
                return await res.json()
   
