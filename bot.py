import os
import telebot

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)


n1 = ["админ гей", "админ лох", "админ лошара", "админ даун"]
n2 = ["поддержать", "задонатить"]
n3 = ["ебал", "мать", "отца", "отец", "пидор", "хуесос", "сын", "ебаная", "гнида", "уебище", "уёбище", "далбаеб", "долбаеб", "блядь", "блядина", "бляди", "блядины", "блядину"]

@bot.message_handler(commands=['pravila', 'Правила'])
def send_welcome(message):
    bot.reply_to(message, "Приветствую!\nНынешние правила:\n1) Запрещены любые оскорбления (кроме в сторону админа)\n2) Запрещена любая рекламная хуйня и т.д.\n3) Больше не придумал:(")

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    # Проверяем, что сообщение вообще текстовое (чтобы бот не ломался на стикерах/фото)
    if not message.text:
        return
        
    text = message.text.lower()

    if any(word in text for word in n1):
        gif_url = "https://media1.tenor.com/m/fcjgHGBswysAAAAC/fr-lie.gif"
        bot.send_animation(
            chat_id=message.chat.id,
            animation=gif_url,
            caption="🫣",
            reply_to_message_id=message.message_id
        )
    
    elif any(word in text for word in n2):
        # Исправлено с replay_to на reply_to
        bot.reply_to(message, "Ссылка на пожертвование - https://dalink.to/rnghuman\nP.S. Спасибо <3")

    elif any(word in text for word in n3):
        # Исправлено с replay_to на reply_to
        bot.reply_to(message, "@Nikita2015PRO , у нас тут придурок объявился!\n Возможна ошибка, заранее извиняюсь!")

if __name__ == '__main__':
    print("Идиот вышел на работу...")
    bot.infinity_polling()
