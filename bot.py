from telethon import TelegramClient, events
import asyncio
from config import API_ID, API_HASH, PHONE, AUTO_REPLY_TEXT

# Инициализация клиента Telegram
client = TelegramClient('session_name', API_ID, API_HASH)

@client.on(events.NewMessage(incoming=True))
async def handle_message(event):
    """Отвечает на любое входящее сообщение фиксированным текстом."""
    if event.is_private:  # Отвечаем только в личных чатах
        print(f"Получено сообщение от {event.sender_id}: {event.text}")
        await event.reply(AUTO_REPLY_TEXT)
        print("Отправлен автоответ.")

async def main():
    """Запуск бота."""
    await client.start(PHONE)
    print("Бот запущен и слушает сообщения...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
