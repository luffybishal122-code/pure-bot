from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    CallbackQueryHandler,
    filters
)

# ==================================================
# BOT TOKEN
# ==================================================
# Put your NEW token from @BotFather here.
# Do NOT use the token you previously exposed.


import os

BOT_TOKEN = os.environ["8762734302:AAGALCwyhEN3jftgoSipbN6WWbHYH5xPry8"]


# ==================================================
# ADMIN USERNAME
# ==================================================

ADMIN_USERNAME = "alyaaismad"


# ==================================================
# QR IMAGE
# ==================================================

QR_IMAGE = "qr.png"


# ==================================================
# GROUP / BUSINESS NAME
# ==================================================

GROUP_NAME = "PURE NEPALI KANDA"


# ==================================================
# START MENU
# ==================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [

        [
            InlineKeyboardButton(
                "🇳🇵 NEPALI RANDOM KANDA GROUPS",
                callback_data="category_nepali"
            )
        ],

        [
            InlineKeyboardButton(
                "👩 MODEL KANDA GROUPS",
                callback_data="category_model"
            )
        ],

        [
            InlineKeyboardButton(
                "👑 ALL TYPES OF PREMIUM GROUPS",
                callback_data="category_premium"
            )
        ],

        [
            InlineKeyboardButton(
                "💰 SASTO MA RAMRO GROUPS",
                callback_data="category_sasto"
            )
        ]

    ]

    await update.message.reply_text(
        "🔥 WELCOME TO PURE NEPALI KANDA 🔥\n\n"
        "💎 PREMIUM GROUPS AVAILABLE\n\n"
        "👇 CHOOSE YOUR GROUP TYPE 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ==================================================
# CATEGORY MENU
# ==================================================

async def category_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    # ==================================================
    # NEPALI RANDOM
    # ==================================================

    if query.data == "category_nepali":

        category_name = "🇳🇵 NEPALI RANDOM KANDA GROUPS"

        keyboard = [

            [
                InlineKeyboardButton(
                    "💎 2 GROUPS - Rs. 1000",
                    callback_data="plan1000"
                )
            ],

            [
                InlineKeyboardButton(
                    "👑 3 GROUPS - Rs. 2000",
                    callback_data="plan2000"
                )
            ],

            [
                InlineKeyboardButton(
                    "🔙 BACK",
                    callback_data="back_categories"
                )
            ]

        ]

    # ==================================================
    # MODEL
    # ==================================================

    elif query.data == "category_model":

        category_name = "👩 MODEL KANDA GROUPS"

        keyboard = [

            [
                InlineKeyboardButton(
                    "💎 2 GROUPS - Rs. 1000",
                    callback_data="plan1000"
                )
            ],

            [
                InlineKeyboardButton(
                    "👑 3 GROUPS - Rs. 2000",
                    callback_data="plan2000"
                )
            ],

            [
                InlineKeyboardButton(
                    "🔙 BACK",
                    callback_data="back_categories"
                )
            ]

        ]

    # ==================================================
    # ALL PREMIUM
    # ==================================================

    elif query.data == "category_premium":

        category_name = "👑 ALL TYPES OF PREMIUM GROUPS"

        keyboard = [

            [
                InlineKeyboardButton(
                    "💎 2 GROUPS - Rs. 1000",
                    callback_data="plan1000"
                )
            ],

            [
                InlineKeyboardButton(
                    "👑 3 GROUPS - Rs. 2000",
                    callback_data="plan2000"
                )
            ],

            [
                InlineKeyboardButton(
                    "🔙 BACK",
                    callback_data="back_categories"
                )
            ]

        ]

    # ==================================================
    # SASTO MA RAMRO
    # ==================================================

    elif query.data == "category_sasto":

        category_name = "💰 SASTO MA RAMRO GROUPS"

        keyboard = [

            [
                InlineKeyboardButton(
                    "💵 1 GROUP - Rs. 500",
                    callback_data="plan500"
                )
            ],

            [
                InlineKeyboardButton(
                    "💎 2 GROUPS - Rs. 800",
                    callback_data="plan800"
                )
            ],

            [
                InlineKeyboardButton(
                    "🔙 BACK",
                    callback_data="back_categories"
                )
            ]

        ]

    else:

        return


    await query.edit_message_text(
        f"{category_name}\n\n"
        "💰 CHOOSE YOUR PREMIUM PLAN 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ==================================================
# PAYMENT PAGE
# ==================================================

async def show_payment_page(
    update: Update,
    plan_name: str,
    plan_details: str
):

    query = update.callback_query
    await query.answer()

    keyboard = [

        [
            InlineKeyboardButton(
                "💬 MESSAGE @alyaaismad",
                url=f"https://t.me/{ADMIN_USERNAME}"
            )
        ],

        [
            InlineKeyboardButton(
                "🔙 CHOOSE ANOTHER PLAN",
                callback_data="back_plans"
            )
        ]

    ]

    try:

        with open(QR_IMAGE, "rb") as photo:

            await query.message.reply_photo(

                photo=photo,

                caption=(
                    f"💎 {plan_name}\n\n"

                    f"✅ {plan_details}\n\n"

                    "💳 PAY YOUR PLAN FOR PREMIUM\n\n"

                    "📲 Scan the QR code above and "
                    "make your payment.\n\n"

                    "📸 AFTER PAYMENT\n\n"

                    "Click the button below to message "
                    "the admin directly.\n\n"

                    "📤 SEND YOUR PAYMENT SCREENSHOT "
                    "(SS) DIRECTLY TO ADMIN.\n\n"

                    "🔥 After payment verification, "
                    "admin will provide your PREMIUM "
                    "GROUP LINK."
                ),

                reply_markup=InlineKeyboardMarkup(keyboard)
            )

    except FileNotFoundError:

        await query.message.reply_text(

            "❌ QR IMAGE NOT FOUND!\n\n"

            "Make sure your QR file is named:\n"
            "qr.png\n\n"

            "And put it in the same folder as bot.py."
        )


# ==================================================
# RS. 500
# ==================================================

async def plan_500(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await show_payment_page(
        update,
        "RS. 500 PLAN",
        "1 PREMIUM GROUP"
    )


# ==================================================
# RS. 800
# ==================================================

async def plan_800(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await show_payment_page(
        update,
        "RS. 800 PLAN",
        "2 PREMIUM GROUPS"
    )


# ==================================================
# RS. 1000
# ==================================================

async def plan_1000(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await show_payment_page(
        update,
        "RS. 1000 PLAN",
        "2 PREMIUM GROUPS"
    )


# ==================================================
# RS. 2000
# ==================================================

async def plan_2000(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await show_payment_page(
        update,
        "RS. 2000 PLAN",
        "3 PREMIUM GROUPS"
    )


# ==================================================
# BACK TO GROUP CATEGORIES
# ==================================================

async def back_categories(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query
    await query.answer()

    keyboard = [

        [
            InlineKeyboardButton(
                "🇳🇵 NEPALI RANDOM KANDA GROUPS",
                callback_data="category_nepali"
            )
        ],

        [
            InlineKeyboardButton(
                "👩 MODEL KANDA GROUPS",
                callback_data="category_model"
            )
        ],

        [
            InlineKeyboardButton(
                "👑 ALL TYPES OF PREMIUM GROUPS",
                callback_data="category_premium"
            )
        ],

        [
            InlineKeyboardButton(
                "💰 SASTO MA RAMRO GROUPS",
                callback_data="category_sasto"
            )
        ]

    ]

    await query.edit_message_text(

        "🔥 PURE NEPALI KANDA 🔥\n\n"

        "💎 PREMIUM GROUPS AVAILABLE\n\n"

        "👇 CHOOSE YOUR GROUP TYPE 👇",

        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ==================================================
# BACK TO PLANS
# ==================================================

async def back_plans(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query
    await query.answer()

    keyboard = [

        [
            InlineKeyboardButton(
                "💵 1 GROUP - Rs. 500",
                callback_data="plan500"
            )
        ],

        [
            InlineKeyboardButton(
                "💎 2 GROUPS - Rs. 800",
                callback_data="plan800"
            )
        ],

        [
            InlineKeyboardButton(
                "💎 2 GROUPS - Rs. 1000",
                callback_data="plan1000"
            )
        ],

        [
            InlineKeyboardButton(
                "👑 3 GROUPS - Rs. 2000",
                callback_data="plan2000"
            )
        ],

        [
            InlineKeyboardButton(
                "🔙 BACK TO GROUP TYPES",
                callback_data="back_categories"
            )
        ]

    ]

    await query.edit_message_text(

        "💰 CHOOSE YOUR PREMIUM PLAN 👇",

        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ==================================================
# NORMAL TEXT MESSAGES
# ==================================================

async def auto_reply(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    message = update.message.text.lower()

    # ==================================================
    # HELLO / HI
    # ==================================================

    if "hello" in message or "hi" in message:

        await update.message.reply_text(

            "👋 HELLO!\n\n"

            "🔥 Welcome to PURE NEPALI KANDA!\n\n"

            "Type /start to see our premium groups."
        )

    # ==================================================
    # PRICE
    # ==================================================

    elif "price" in message or "cost" in message:

        await update.message.reply_text(

            "💰 PREMIUM PLANS\n\n"

            "💵 Sasto - 1 Group: Rs. 500\n"
            "💎 Sasto - 2 Groups: Rs. 800\n\n"

            "💎 Premium - 2 Groups: Rs. 1000\n"
            "👑 Premium - 3 Groups: Rs. 2000\n\n"

            "👇 Type /start to choose."
        )

    # ==================================================
    # HELP
    # ==================================================

    elif "help" in message:

        keyboard = [

            [
                InlineKeyboardButton(
                    "💬 MESSAGE @alyaaismad",
                    url=f"https://t.me/{ADMIN_USERNAME}"
                )
            ]

        ]

        await update.message.reply_text(

            "🆘 NEED HELP?\n\n"

            "Contact admin directly 👇",

            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ==================================================
    # OTHER
    # ==================================================

    else:

        await update.message.reply_text(

            "👋 Welcome to PURE NEPALI KANDA!\n\n"

            "Type /start to see premium groups."
        )


# ==================================================
# CREATE BOT
# ==================================================

app = Application.builder().token(BOT_TOKEN).build()


# ==================================================
# START COMMAND
# ==================================================

app.add_handler(
    CommandHandler(
        "start",
        start
    )
)


# ==================================================
# CATEGORY HANDLER
# ==================================================

app.add_handler(
    CallbackQueryHandler(
        category_menu,
        pattern="^category_"
    )
)


# ==================================================
# PLAN HANDLERS
# ==================================================

app.add_handler(
    CallbackQueryHandler(
        plan_500,
        pattern="^plan500$"
    )
)

app.add_handler(
    CallbackQueryHandler(
        plan_800,
        pattern="^plan800$"
    )
)

app.add_handler(
    CallbackQueryHandler(
        plan_1000,
        pattern="^plan1000$"
    )
)

app.add_handler(
    CallbackQueryHandler(
        plan_2000,
        pattern="^plan2000$"
    )
)


# ==================================================
# BACK HANDLERS
# ==================================================

app.add_handler(
    CallbackQueryHandler(
        back_categories,
        pattern="^back_categories$"
    )
)

app.add_handler(
    CallbackQueryHandler(
        back_plans,
        pattern="^back_plans$"
    )
)


# ==================================================
# NORMAL TEXT HANDLER
# ==================================================

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        auto_reply
    )
)


# ==================================================
# RUN BOT
# ==================================================

print("🤖 PURE NEPALI KANDA BOT IS RUNNING...")

app.run_polling()