from telethon import TelegramClient, events
import asyncio

# Конфиг
API_ID = 23168299                   # Ваш API ID (получаем на my.telegram.org)
API_HASH = "152406673f64cacca83d4276d128f555"           # Ваш API HASH
PHONE = "+17282161417"              # Номер телефона аккаунта

AUTO_REPLY_TEXT = "Вы колонизированны!"

client = TelegramClient('session_name', API_ID, API_HASH)

@client.on(events.NewMessage(incoming=True))
async def handle_message(event):
    """Отвечает на любое входящее сообщение фиксированным текстом."""
    if event.is_private:  
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