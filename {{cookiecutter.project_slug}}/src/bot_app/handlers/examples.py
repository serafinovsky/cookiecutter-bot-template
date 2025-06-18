__all__ = [
    "TestCommandHandler",
    "TestMessageHandler",
    "TestCallbackHandler",
    "Step1Handler",
    "Step2Handler",
    "Step3Handler",
    "FinishConversationHandler",
    "FallbackHandler",
]

import re

from telegram import (
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Update,
)
from telegram.constants import ParseMode
from telegram.ext import ContextTypes, filters

from {{cookiecutter.project_slug}}.bot_config import (
    CB_TEST,
    CB_SEP,
    TEST_CB_BUTTON,
    TEST_CONVERSATION_BUTTON,
    STEP1_STATE,
    STEP2_STATE,
    STEP3_STATE,
    END_STATE
)
from {{cookiecutter.project_slug}}.handlers.base import (
    Callback,
    Message,
    Command,
    TelegramMessageHandler,
    TelegramCallbackHandler,
    TelegramCommandHandler
)
from {{cookiecutter.project_slug}}.utils import decode_callback, make_inline_kbb, render_message


class StartMessage(Command):
    @classmethod
    def command(cls):
        return "start"

    @classmethod
    async def handler(cls, update: Update, context: ContextTypes.DEFAULT_TYPE):
        reply_keyboard = [[TEST_CB_BUTTON], [TEST_CONVERSATION_BUTTON]]
        await update.message.reply_text(
            render_message("start.html"),
            parse_mode=ParseMode.HTML,
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard,
                one_time_keyboard=True,
                input_field_placeholder="Select action:",
            ),
        )


class TestMessage(Message):
    @classmethod
    def filters(cls):
        return filters.Regex(f"^({TEST_CB_BUTTON})$")

    @classmethod
    async def handler(cls, update: Update, context: ContextTypes.DEFAULT_TYPE):
        keyboard = [
            [make_inline_kbb("Yes", CB_TEST, "Yes")],
            [make_inline_kbb("No", CB_TEST, "No")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        text = "Are you OK?"
        await update.message.reply_text(text, reply_markup=reply_markup)


class TestCallback(Callback):
    @classmethod
    def pattern(cls):
        return re.compile(rf"(?P<action>{CB_TEST}){CB_SEP}(?P<answer>(Yes|No))")

    @classmethod
    async def handler(cls, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()
        data = decode_callback(query.data, cls.pattern())
        answer = data["answer"]
        text = "Go cry"
        if answer == "Yes":
            text = "Good job"
        await query.edit_message_text(text=text)


class TestStep1Message(Message):
    @classmethod
    def filters(cls):
        return filters.Regex(f"^({TEST_CONVERSATION_BUTTON})$")

    @classmethod
    async def handler(cls, update: Update, context: ContextTypes.DEFAULT_TYPE):
        reply_keyboard = [["1"], ["2"], ["3"], ["Finish"]]
        await update.message.reply_text(
            "Step 1. Select next step",
            parse_mode=ParseMode.HTML,
            reply_markup=ReplyKeyboardMarkup(reply_keyboard),
        )
        return STEP1_STATE


class TestStep2Message(Message):
    @classmethod
    def filters(cls):
        return filters.Regex(f"^(2)$")

    @classmethod
    async def handler(cls, update: Update, context: ContextTypes.DEFAULT_TYPE):
        reply_keyboard = [["1"], ["2"], ["3"], ["Finish"]]
        await update.message.reply_text(
            "Step 2. Select next step",
            parse_mode=ParseMode.HTML,
            reply_markup=ReplyKeyboardMarkup(reply_keyboard),
        )
        return STEP2_STATE


class TestStep3Message(Message):
    @classmethod
    def filters(cls):
        return filters.Regex(f"^(3)$")

    @classmethod
    async def handler(cls, update: Update, context: ContextTypes.DEFAULT_TYPE):
        reply_keyboard = [["1"], ["2"], ["3"], ["Finish"]]
        await update.message.reply_text(
            "Step 3. Select next step",
            parse_mode=ParseMode.HTML,
            reply_markup=ReplyKeyboardMarkup(reply_keyboard),
        )
        return STEP3_STATE


class FinishConversationMessage(Message):
    @classmethod
    def filters(cls):
        return filters.Regex(f"^(Finish)$")

    @classmethod
    async def handler(cls, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "Congrats, you've finished. You can /start from beginning",
            parse_mode=ParseMode.HTML,
            reply_markup=ReplyKeyboardRemove(),
        )
        return END_STATE


class FallbackMessage(Message):
    @classmethod
    async def handler(cls, update: Update, context: ContextTypes.DEFAULT_TYPE):
        reply_keyboard = [["1"], ["2"], ["3"], ["Finish"]]
        await update.message.reply_text(
            "You can select only next step or finish",
            parse_mode=ParseMode.HTML,
            reply_markup=ReplyKeyboardMarkup(reply_keyboard),
        )


TestCommandHandler = TelegramCommandHandler(StartMessage)
TestMessageHandler = TelegramMessageHandler(TestMessage)
TestCallbackHandler = TelegramCallbackHandler(TestCallback)
Step1Handler = TelegramMessageHandler(TestStep1Message)
Step2Handler = TelegramMessageHandler(TestStep2Message)
Step3Handler = TelegramMessageHandler(TestStep3Message)
FinishConversationHandler = TelegramMessageHandler(FinishConversationMessage)
FallbackHandler = TelegramMessageHandler(FallbackMessage)