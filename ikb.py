from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.misc import btn


def get_inline_keyboard(buttons_data, lang: str):
    buttons = []

    for button_info in buttons_data["buttons_info"]:
        text_key = button_info.get("text_key")
        callback_data = button_info.get("callback_data")
        url = button_info.get("url")

        if not text_key:
            raise ValueError("Missing 'text_key' in button_info")

        button_text = btn[text_key][lang]

        if url or callback_data:
            button_row = []
            if url:
                button_row.append(InlineKeyboardButton(text=button_text, url=url))
            if callback_data:
                button_row.append(
                    InlineKeyboardButton(text=button_text, callback_data=callback_data))
            buttons.append(button_row)

    if not buttons:
        raise ValueError("No valid buttons provided")

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard



def subscribe(lang: str):

    buttons_data = {
        "buttons_info": [
            {"text_key": 'follow', "url": 'https://t.me/channel'},
            {"text_key": 'subscribed', "callback_data": "check_follow"}
        ]
    }
    return get_inline_keyboard(buttons_data, lang)
