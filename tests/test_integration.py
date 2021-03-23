import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from utils import helper
import unittest

# Your API ID, hash and session string here
api_id = int(os.environ["TELEGRAM_APP_ID"])
api_hash = os.environ["TELEGRAM_APP_HASH"]
client = TelegramClient('anon2', api_id, api_hash)

async def get_bot_response_help():
    async with client.conversation('ongabot', timeout=10) as conv:
        _ = await conv.send_message('/help')
        response = await conv.get_response()
    return response.message


class IntegrationTest(unittest.TestCase):
    def test_help(self):
        with client:
            response = client.loop.run_until_complete(get_bot_response_help())
        assert response == helper.create_help_text()[:-1]

    def test_help2(self):
        with client:
            response = client.loop.run_until_complete(get_bot_response_help())
        assert response == helper.create_help_text()[:-1]


if __name__ == "__main__":
    unittest.main()
