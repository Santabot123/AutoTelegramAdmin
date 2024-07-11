import os
def Telegram_potser(channel_name: str, content: str, image_url: str) -> str:
    """ Publish blog post on the Telegram.
        :param channel_name: string, the name of the Telegram channel
        :param content: string, the content of the message.
        :param image_url:string, URL link to image.

        example:
        {
            "channel_name": "@name12345",
            "content": "Let's strt our conversation...."
            "image_url" : "https://example.com/pics/image.jpeg"
        }

    """
    import telebot
    BOT_TOKEN = os.environ.get('TELEGRAM_POSTER_TOKEN')

    bot = telebot.TeleBot(BOT_TOKEN)
    bot.send_photo(chat_id=channel_name, photo=image_url, caption=content)
    # bot.send_message(chat_id=channel_name, text=content,parse_mode= 'Markdown')

    return 'The provided content and images were successfully published on the specified Telegram channel. The work is finished.'