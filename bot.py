import os
import random
import telebot

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

n1 = ["админ гей", "админ лох", "админ лошара", "админ даун"]
n2 = ["поддержать", "донат", "пожертв"]
n3 = [
    "ебал",
    "пидор",
    "хуесос",
    "бляд",
    "гнида",
    "далбаеб",
    "долбаеб",
    "петух",
    "уеб",
    "уёб",
    "ганд",
    "гонд",
    "пидр",
    "пидор",
    "ебан",
]
n4 = [
    "всем привет",
    "всем здарова",
    "всем салам",
    "здрасте",
    "здрасьте",
    "здравствуйте",
    "привет парни",
    "пацаны привет",
    "привет пацаны",
    "пацаны привет",
    "привет парни",
]
ADMIN_ID = 1475257511


@bot.message_handler(commands=["pravila", "Правила"])
def send_welcome(message):
    bot.reply_to(
        message,
        "Приветствую!\nНынешние правила:\n1) Запрещены любые оскорбления (кроме"
        " в сторону админа)\n2) Запрещена любая рекламная хуйня и т.д.\n3) Больше"
        " не придумал:(",
    )


@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    if not message.text:
        return

    text = message.text.lower()
    user_id = message.from_user.id

    if user_id != ADMIN_ID:
        #if any(word in text for word in n1):
            gif_url = "0"
            bot.reply_to(message, gif_url)

    elif any(word in text for word in n2):
        bot.reply_to(
            message,
            "Ссылка на пожертвование - https://dalink.to/rnghuman\nСпасибо <3",
        )

    elif any(word in text for word in n3):
        bot.reply_to(
            message,
            "@Nikita2015PRO , у нас тут придурок объявился!\n Возможна ошибка,"
            " заранее извиняюсь!",
        )

    elif text == "котик":
        variant = [
            "https://media.tenor.com/lfDATg4Bhc0AAAAM/happy-cat.gif",
            "https://media.tenor.com/l8lnhRNnlMwAAAAM/cat-cat-meme.gif",
            (
                "https://media.tenor.com/cRTQk6N_FxMAAAAM/swag-cat-swagbilli-cutecat-cats-cat-swag-ok-yooo-yo.gif"
            ),
            "https://media.tenor.com/OOj-QK2NxUkAAAAM/cat-kitty.gif",
            "https://media.tenor.com/QSEW0tZz4OUAAAAM/cat.gif",
            "https://media.tenor.com/FWYFkElU8UIAAAAM/7tv-cat-meme.gif",
            "https://media.tenor.com/TqNG5XNntroAAAAM/so-tuff.gif",
            "https://media.tenor.com/WVTEnkzM9_UAAAAM/cat-cat-smile.gif",
            "https://media.tenor.com/omBQ2kB8A_oAAAAM/kattus-ultrus-fetus.gif",
            "https://media.tenor.com/onFHdpJsiKUAAAAm/zazu-burger.webp",
            "https://media.tenor.com/t8RTOfWcIYUAAAAM/appetite-hungry.gif",
            "https://media.tenor.com/kKeM0-othPUAAAAm/fat-long-cat.webp",
            "https://media.tenor.com/pdX9YTI4_eoAAAA1/cat-cat-with-tongue.webp",
            "https://media.tenor.com/wcDBzYCQyOgAAAAM/ice-cream-cat.gif",
            "https://media.tenor.com/298Aly2LzQwAAAAM/smiling-cat-happy-cat.gif",
            "https://media.tenor.com/tNr8zcDCyoYAAAAM/cat.webp",
        ]
        bot.reply_to(message, random.choice(variant))

    elif any(word in text for word in n4):
        bot.reply_to(message, "Привет!")
    # Если пишет АДМИН (вы)
    else:
        if text == "привет, идиот.":
            bot.reply_to(message, "Привет @Nikita2015PRO, Как дела?")
        elif text == "все супер,как сам?.":
            bot.reply_to(
            message,
            "Прекрасно,работаю за бесплатно.\nПоэтому,будь добр,не отвлекай меня"
            " от работы...",
            )
        elif text == "извини((.":
            bot.reply_to(message, "...")
        else:
        # На любые другие ваши сообщения бот может просто кидать подтверждение или молчать
            pass


if __name__ == "__main__":
    print("Идиот вышел на работу...")
    bot.infinity_polling()
