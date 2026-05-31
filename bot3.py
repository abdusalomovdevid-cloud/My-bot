BOT_TOKEN = "8837285362:AAEdjIf-SGplFX__KfxXNvUXXWkDXlVu8Nw"
ADMIN_IDS = [1903749800, 768338132]
SERVER_IP = "stormside.uz"
SERVER_PORT = "25565"
DISCORD_LINK = ""

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

WELCOME = (
    "Stormside Minecraft Serveriga xush kelibsiz!\n\n"
    "Quyidagi bolimlardan birini tanlang:"
)

SERVER_INFO = (
    "Server Malumotlari\n\n"
    "IP: " + SERVER_IP + "\n"
    
    "Versiya: Java Edition 1.20.x\n"
    "Rejim: Anarchy\n\n"
    "Minecraft-ni oching va yuqoridagi IP-ni kiriting."
)

DONATE = (
    "DONATE - STORMSIDE\n\n"
    "RANKLAR (1 oy / 3 oy)\n"
    "--------------------------------\n"
    "ECLIPSE      7,000 / 20,000 UZS\n"
    "PHOENIX     12,000 / 30,000 UZS\n"
    "ORACLE      18,000 / 40,000 UZS\n"
    "VOYAGER     24,000 / 55,000 UZS\n"
    "CATALYST    34,000 / 69,000 UZS\n"
    "CELESTIAL   49,000 / 75,000 UZS\n"
    "AURORA      60,000 / 88,000 UZS\n"
    "IMMORTAL    85,000 / 105,000 UZS\n"
    "APEX        99,000 / 125,000 UZS\n"
    "LUMINARY   130,000 / 160,000 UZS\n"
    "GREAT      169,000 / 222,000 UZS\n\n"
    "VALES\n"
    "--------------------------------\n"
    "100 vales  = 10,000 UZS\n"
    "1000 vales = 100,000 UZS\n\n"
    "CASELAR\n"
    "--------------------------------\n"
    "Donate Case = 10,000 UZS\n"
    "Token Case  = 30,000 UZS\n"
    "Kit Case    = 10,000 UZS\n\n"
    "UNBAN = 15,000 UZS\n\n"
    "Tolovdan keyin adminlarga murojat qiling."
)

HISOB = (
    "HISOBNI TOLDIRISH\n\n"
    "Quyidagi rekvizitlarga pul otkazing:\n\n"
    "Click: Tez kunda\n"
    "Payme: Tez kunda\n\n"
    "Tolovdan keyin Minecraft nickname'ingizni\n"
    "va qancha pul otkazganingizni adminlarga yuboring."
)

RULES_1 = (
    "STORMSIDE QOIDALARI\n\n"
    "1. CHAT TARTIBI\n\n"
    "1.1 Spam, flood yoki ortiqcha CAPS - 30 daqiqa mute\n"
    "1.2 Oyinchilarni haqoratlash - 3 soat mute\n"
    "1.3 Oila azolariga tegish yoki ogir sokinish - 3 kun ban\n"
    "1.4 Serverga aloqasiz reklama - 20 kun ban\n"
    "1.5 Server haqida yolgon malumot tarqatish - 7 kun ban\n"
    "1.6 Admin yoki moderni haqoratlash - 20 kun ban\n"
    "1.7 Server obrosiga zarar yetkazuvchi gaplar - 15 kun ban\n"
    "1.8 Shaxsiy aloqa malumotlarini chatga tashlash - 5 soat mute\n\n"
    "2. TAQIQLANGAN DASTUR VA BAGLAR\n\n"
    "2.1 Chit, soft yoki auto mod ishlatish - 25 kun ban\n"
    "2.2 Topilgan bagni yashirish yoki ishlatish - 50 kun ban\n"
    "2.3 Bagni aytib ham foydalanish - 20 kun ban\n"
    "2.4 Chatda chit ishlatishni tan olish - 15 kun ban\n"
    "2.5 Chit ishlatuvchi bilan jamoa bolish - 25 kun ban"
)

RULES_2 = (
    "3. AKKAUNT VA PROFIL\n\n"
    "3.1 Haqoratli yoki aldovchi nik qoyish - 30 kun ban\n"
    "3.2 Akkauntni boshqaga berish - 40 kun ban\n"
    "3.3 Akkaunt yoki donat sotish - 50 kun ban\n\n"
    "4. OYIN JARAYONI\n\n"
    "4.1 Firibgarlik yoki aldash - umrbod ban\n"
    "4.2 Serverga ataylab zarar yetkazish - 50 kun ban\n"
    "4.3 Qoidabuzarga yordam berish - 20 kun ban\n"
    "4.4 Boshqalarni qoida buzishga undash - 5 kun ban\n\n"
    "5. TEKSHIRUV TARTIBI\n\n"
    "5.1 Moder korsatmalariga amal qilmaslik - 30 kun ban\n"
    "5.2 Tekshiruvni etiborsiz qoldirish - 15 kun ban\n"
    "5.3 Tekshiruvga halaqit berish - umrbod ban\n"
    "5.4 Tekshiruv vaqtida fayllarni ochirish - 50 kun ban\n"
    "5.5 Tekshiruv vaqtida oyindan chiqish - 30 kun ban\n\n"
    "6. DONAT VA IMTIYOZLAR\n\n"
    "6.1 Donat orqali bosim otkazish - 10 kun ban\n"
    "6.2 Sababsiz mute/ban/kick berish - 10 kun ban\n"
    "6.3 Soxta chek bilan donat olishga urinish - 50 kun ban\n"
    "6.4 Donatni qaytarish talab qilib aldashga urinish - 30 kun ban"
)

CONTACT = (
    "ADMINLARGA MUROJAT\n\n"
    "Savolingiz yoki muammongizni yozing.\n"
    "Admin imkon qadar tez javob beradi.\n\n"
    "Xabaringizni yuboring:"
)

def main_kb():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Server Malumotlari", callback_data="server")],
        [InlineKeyboardButton("Donate", callback_data="donate")],
        [InlineKeyboardButton("Hisobni Toldirish", callback_data="hisob")],
        [InlineKeyboardButton("Adminlarga Murojat", callback_data="contact")],
        [InlineKeyboardButton("Qoidalar", callback_data="rules")],
    ])

def back_kb():
    return InlineKeyboardMarkup([[InlineKeyboardButton("Orqaga", callback_data="menu")]])

def donate_kb():
    btns = []
    if DISCORD_LINK:
        btns.append([InlineKeyboardButton("Discord", url=DISCORD_LINK)])
    btns.append([InlineKeyboardButton("Hisobni Toldirish", callback_data="hisob")])
    btns.append([InlineKeyboardButton("Orqaga", callback_data="menu")])
    return InlineKeyboardMarkup(btns)

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME, reply_markup=main_kb())

async def button(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    if q.data == "menu":
        await q.edit_message_text(WELCOME, reply_markup=main_kb())
    elif q.data == "server":
        await q.edit_message_text(SERVER_INFO, reply_markup=back_kb())
    elif q.data == "donate":
        await q.edit_message_text(DONATE, reply_markup=donate_kb())
    elif q.data == "hisob":
        await q.edit_message_text(HISOB, reply_markup=back_kb())
    elif q.data == "rules":
        await q.edit_message_text(RULES_1, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Keyingisi >>", callback_data="rules2")],
            [InlineKeyboardButton("Orqaga", callback_data="menu")]
        ]))
    elif q.data == "rules2":
        await q.edit_message_text(RULES_2, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("<< Oldingisi", callback_data="rules")],
            [InlineKeyboardButton("Orqaga", callback_data="menu")]
        ]))
    elif q.data == "contact":
        ctx.user_data['wait'] = True
        await q.edit_message_text(
            CONTACT,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Bekor qilish", callback_data="menu")]])
        )

async def handle_message(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if not ctx.user_data.get('wait'):
        await update.message.reply_text(
            "Menyu uchun /start yuboring.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Bosh menyu", callback_data="menu")]])
        )
        return
    user = update.effective_user
    mention = f"@{user.username}" if user.username else f"{user.full_name} (ID: {user.id})"
    header = f"Yangi murojat!\n\nFoydalanuvchi: {mention}\nID: {user.id}\n\nXabar:"
    sent = False
    for aid in ADMIN_IDS:
        try:
            await ctx.bot.send_message(aid, header)
            await update.message.forward(aid)
            sent = True
        except Exception as e:
            logger.error(f"Admin {aid}: {e}")
    ctx.user_data['wait'] = False
    if sent:
        await update.message.reply_text(
            "Xabaringiz adminlarga yuborildi! Tez orada javob beriladi.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Bosh menyu", callback_data="menu")]])
        )
    else:
        await update.message.reply_text("Xatolik yuz berdi. Keyinroq urinib koring.", reply_markup=back_kb())

async def admin_reply(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ADMIN_IDS:
        return
    msg = update.message
    if msg.reply_to_message and msg.reply_to_message.forward_from:
        uid = msg.reply_to_message.forward_from.id
        try:
            await ctx.bot.send_message(uid, f"Admin javobi:\n\n{msg.text}")
            await msg.reply_text("Javob yuborildi!")
        except Exception as e:
            await msg.reply_text(f"Xato: {e}")

async def error(update: object, ctx: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Xato: {ctx.error}", exc_info=ctx.error)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.REPLY & filters.TEXT & ~filters.COMMAND, admin_reply))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_error_handler(error)
    logger.info("Stormside Bot ishga tushdi!")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
