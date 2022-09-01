from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
 أهلا بك في بوت أستخراج روابط الميديا 🖤.
    """

    # Help Message
    HELP = """
**اقرأ أدناه لتعرف كيف تستعملني.**

راجع "أنواع الوسائط المدعومة" بالنقر فوق الزر ذي الصلة أدناه.

**كيف تستعملني هنا؟**

فقط أرسل وسائل الإعلام واترك الراحة على عاتقي.
    """

    # About Message
    ABOUT = """
**About This Bot** 

السورس : @CR_T2

المطور : @BK_ZT
    """

    SUPPORTED_MEDIA_TYPES = """
**أرسل لي**

1) صورة
2) ملصق
3) صورة متحركة
4) فيديو
5) ملاحظة فيديو
6) مستند (فيديو / صورة / صورة متحركة)
7) ملاحظة : أن لا يبلغ حجم المستند 5 ميجا
   
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("❲ ⁨⁩𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐄𝐋𝐄𝐆𝐎𝐃 ❳", url="https://t.me/cr_t2")],
        [InlineKeyboardButton("أنواع الوسائط المدعومة", callback_data="supported_media_types")],
        [InlineKeyboardButton("أغلاق", callback_data="close")],
        [InlineKeyboardButton(text="رجوع", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("❲ ⁨⁩𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐄𝐋𝐄𝐆𝐎𝐃 ❳", url="https://t.me/cr_t2")
        ],
        [InlineKeyboardButton("أنواع الوسائط المدعومة", callback_data="supported_media_types")],
        [
            InlineKeyboardButton("كيف يستخدم", callback_data="help"),
            InlineKeyboardButton("حول", callback_data="about")
        ],
        [InlineKeyboardButton("أغلاق", callback_data="close")]
    ]

    # Supported Media Buttons
    supported_media_buttons = [
        [InlineKeyboardButton("❲ ⁨⁩𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐄𝐋𝐄𝐆𝐎𝐃 ❳", url="https://t.me/CR_t2")],
        [InlineKeyboardButton("أغلاق", callback_data="close")],
        [InlineKeyboardButton(text="رجوع", callback_data="home")]
    ]
