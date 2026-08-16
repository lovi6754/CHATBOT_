from pyrogram.types import InlineKeyboardButton
from config import SUPPORT_GRP, UPDATE_CHNL
from YUVICHATBOT import OWNER, YUVICHATBOT


START_BOT = [
    [
        InlineKeyboardButton(
            text="✙ ʌᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ✙",
            url=f"https://t.me/{YUVICHATBOT.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="˹ σᴡηєʀ ˼", url="https://t.me/x_yuvii"),
        InlineKeyboardButton(text="˹ sυᴘᴘσʀᴛ ˼", url=SUPPORT_GRP),
    ],
    [
        InlineKeyboardButton(text="˹ 𝐁ᴏᴛs ˼", url="https://t.me/yuvi_botes"),
    ],
    [
        InlineKeyboardButton(text="⌯  ʜєʟᴘ ᴄσϻϻᴧηᴅ ⌯ ", callback_data="HELP"),
    ],
]


DEV_OP = [
    [
        InlineKeyboardButton(
            text="✙ ʌᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ✙",
            url=f"https://t.me/{YUVICHATBOT.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="˹ σᴡηєʀ ˼", url="https://t.me/x_yuvii"),
        InlineKeyboardButton(text="˹ ᴧʙσυᴛ ˼", callback_data="ABOUT"),
    ],
    [
        InlineKeyboardButton(text="˹ 𝐁ᴏᴛs ˼", url="https://t.me/yuvi_botes"),
    ],
    [
        InlineKeyboardButton(text="⌯  ʜєʟᴘ ᴄσϻϻᴧηᴅ ⌯ ", callback_data="HELP"),
    ],
]


YUVI = [
    [
        InlineKeyboardButton(
            text="✙ ʌᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ✙",
            url=f"https://t.me/{YUVICHATBOT.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="˹ σᴡηєʀ ˼", url="https://t.me/x_yuvii"),
        InlineKeyboardButton(text="˹ ᴧʙσυᴛ ˼", callback_data="ABOUT"),
    ],
    [
        InlineKeyboardButton(text="⌯  ʜєʟᴘ ᴄσϻϻᴧηᴅ ⌯ ", callback_data="HELP"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="✙ ʌᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ✙",
            url=f"https://t.me/{YUVICHATBOT.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(
            text="⌯ ᴄʟσsє ⌯",
            callback_data="CLOSE",
        ),
    ],
]


BACK = [
    [
        InlineKeyboardButton(text="⌯ ʙᴧᴄᴋ ⌯", callback_data="BACK"),
    ],
]


HELP_BTN = [
    [
        InlineKeyboardButton(text="˹ ᴄʜᴧᴛʙσᴛ ˼", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="˹ ᴛσσʟs ˼", callback_data="TOOLS_DATA"),
    ],
    [
        InlineKeyboardButton(text="˹ ¢ʟσηє ˼", callback_data="ADMINS"),
        InlineKeyboardButton(text="˹ sᴘєᴄɪᴧʟ ˼", callback_data="MAIHUDON"),
    ],
    [
        InlineKeyboardButton(text="⌯ ʙᴧᴄᴋ ⌯", callback_data="BACK"),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="CLOSE"),
    ],
]


CHATBOT_ON = [
    [
        InlineKeyboardButton(text="˹ єηᴧʙʟє ˼", callback_data="enable_chatbot"),
        InlineKeyboardButton(text="˹ ᴅɪsᴧʙʟє ˼", callback_data="disable_chatbot"),
    ],
]


MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="˹ sσση ˼", callback_data=f"soom"),
    ],
]

S_BACK = [
    [
        InlineKeyboardButton(text="⌯ ʙᴧᴄᴋ ⌯", callback_data="SBACK"),
        InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="CLOSE"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="⌯ ʙᴧᴄᴋ ⌯", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="CLOSE"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="˹ ʜєʟᴘ ᴄσϻϻᴧηᴅ ˼", callback_data="HELP"),
        InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="CLOSE"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(
            text="˹ ʜєʟᴘ ᴄσϻϻᴧηᴅ ˼", url=f"https://t.me/{YUVICHATBOT.username}?start=help"
        ),
    ],     
    [
        InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="CLOSE"),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="˹ σᴡηєʀ ˼", url="https://t.me/x_yuvii"),
    ],    
    [
        InlineKeyboardButton(text="˹ sυᴘᴘσʀᴛ ˼", url=SUPPORT_GRP),
        InlineKeyboardButton(text="˹ υᴘᴅᴧᴛєs ˼", url=UPDATE_CHNL)],
    [
    InlineKeyboardButton(text="⌯ ʙᴧᴄᴋ ⌯", callback_data="BACK"),
    ],
]