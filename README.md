Telegram Auto-Reply Bot

Установка:
1. Установите зависимости:
   pip install telethon asyncio

2. Откройте файл config.py и укажите в нем:
   - API_ID и API_HASH с my.telegram.org
   - Номер телефона аккаунта
   - Текст автоответа
   - Имя сессии (опционально)

Запуск:
python main.py

Особенности:
- Автоответы только в личных сообщениях
- Логирование в консоль
- Все настройки в одном файле config.py

Важно:
- Никому не передавайте данные из config.py
- Для остановки: Ctrl+C
- При 2FA потребуется ввод пароля




Copyright (C) [Год] [WorldOpenFreeCod]  

This program is free software: you can redistribute it and/or modify  
it under the terms of the GNU General Public License as published by  
the Free Software Foundation, either version 3 of the License, or  
(at your option) any later version.  

This program is distributed in the hope that it will be useful,  
but WITHOUT ANY WARRANTY; without even the implied warranty of  
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
GNU General Public License for more details.  

You should have received a copy of the GNU General Public License  
along with this program. If not, see <https://www.gnu.org/licenses/>.  
