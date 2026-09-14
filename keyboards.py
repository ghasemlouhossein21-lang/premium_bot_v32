"""
keyboards.py
تمام کیبوردهای Inline و Reply ربات. هیچ handlerای نباید خودش InlineKeyboardMarkup
بسازد؛ همه از این فایل صدا زده می‌شوند تا تغییر ظاهر منو در یک‌جا متمرکز باشد.
"""

from aiogram.types import (
InlineKeyboardMarkup,
InlineKeyboardButton as _RealInlineKeyboardButton,
ReplyKeyboardMarkup,
KeyboardButton as _RealKeyboardButton,
CopyTextButton,
)

import database as db
from text_catalog import text as t, TEXTS
import bot_info
import vpn_panel
import panels
_PANEL_MODULE = panels
from config import UNIQUEPAY_ENABLED, MARZBAN_ENABLED, PASARGAD_ENABLED, ONLINE_PAYMENT_MIN_AMOUNT

def _button_premium_emoji_kwargs(kwargs):
"""در صورت وجود Premium Emoji ذخیره‌شده برای متن دکمه، آن را به icon رسمی تلگرام وصل می‌کند.

🐛 تاریخچه‌ی این تابع (برای این‌که دوباره از اول باگ نسازیم):
۱) اول متنِ دکمه هنگام ساخت icon حذف می‌شد → با فشردن دکمه متنِ ناقص
   برمی‌گشت و هیچ فیلتری match نمی‌شد.
۲) بعد از این‌که متن را دست‌نخورده نگه داشتیم، مشخص شد خودِ تلگرام وقتی
   هم `text` (که با همان ایموجی شروع می‌شود) و هم `icon_custom_emoji_id`
   روی یک دکمه ست باشند، همان کاراکتر ابتدای متن را خودش حذف می‌کند تا
   ایموجی دوبار نمایش داده نشود؛ و باز هم متنِ برگشتی با متنِ ذخیره‌شده
