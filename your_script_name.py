from telethon import TelegramClient, events
import asyncio

api_id = "26844873"
api_hash = "26e6889686e35fc2288442a5b01f551a"

client = TelegramClient('monad_alert_session', api_id, api_hash)

KEYWORDS = ['monad']
CHANNEL_USERNAME = 'sageairdrops'  # No @

@client.on(events.NewMessage(chats=CHANNEL_USERNAME))
async def monad_checker(event):
    message_text = event.message.message
    if any(k in message_text.lower() for k in KEYWORDS):
        alert_msg = f"🚨 MONAD ALERT from @{CHANNEL_USERNAME}:\n\n{message_text}"
        me = await client.get_me()
        await client.send_message('@imransihab0', alert_msg)
        print("✅ Sent alert to @imransihab0.")

async def main():
    print("🔍 Watching @sageairdrops...")
    await client.run_until_disconnected()

client.start()
client.loop.run_until_complete(main())
