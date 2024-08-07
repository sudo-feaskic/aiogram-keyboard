from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from app.misc import btn, placeholder # json formated dict

def get_reply_keyboard(buttons_data, lang: str):
    keyboard = []

    for button_info in buttons_data["buttons_info"]:
        button_row = []
        for text_key in button_info["text_keys"]:
            button_text = btn[text_key][lang]

            if button_info.get("request_contact", False):
                button_row.append(KeyboardButton(text=button_text, request_contact=True))
            elif button_info.get("request_location", False):
                button_row.append(KeyboardButton(text=button_text, request_location=True))
            else:
                button_row.append(KeyboardButton(text=button_text))
        keyboard.append(button_row)

    if not keyboard:
        raise ValueError("No valid buttons provided")
    
    reply_markup = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=keyboard)
    return reply_markup


def example_reply_keyboard(lang: str):
    buttons_data = {
        "buttons_info": [
            {"text_keys": ['lang_choice', 'follow', 'info']},
            {"text_keys": ['subscribed']}
        ]
    }
    return get_reply_keyboard(buttons_data, lang)
