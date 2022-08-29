from telethon import TelegramClient

# Use your own values from my.telegram.org
api_id = 12321660
api_hash = ''
client = TelegramClient('anon', api_id, api_hash)


async def main():
    me = await client.get_me()

    messages = await client.get_messages(-1001407902266)
    last_message = messages[0].message
    print(last_message)

with client:
    client.loop.run_until_complete(main())