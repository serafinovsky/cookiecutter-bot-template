import re
from abc import ABC, abstractmethod
from typing import Type

from telegram import Update
from telegram.ext import CallbackQueryHandler, ContextTypes, MessageHandler, CommandHandler
from telegram.ext.filters import BaseFilter


class Message(ABC):
    @classmethod
    def filters(cls) -> BaseFilter | None:
        return None

    @classmethod
    @abstractmethod
    async def handler(cls, update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass


class Command(Message):
    @classmethod
    @abstractmethod
    def command(cls) -> str:
        pass


class Callback(ABC):
    @classmethod
    @abstractmethod
    def pattern(cls) -> re.Pattern:
        pass

    @classmethod
    @abstractmethod
    def handler(cls, update: Update, context: ContextTypes.DEFAULT_TYPE):
        pass


class TelegramMessageHandler(MessageHandler):
    def __init__(self, message: Type[Message], *args, **kwargs):
        super().__init__(message.filters(), message.handler, *args, **kwargs)


class TelegramCallbackHandler(CallbackQueryHandler):
    def __init__(self, callback: Type[Callback], *args, **kwargs):
        super().__init__(callback.handler, callback.pattern(), *args, **kwargs)


class TelegramCommandHandler(CommandHandler):
    def __init__(self, command: Type[Command], *args, **kwargs):
        super().__init__(command.command(), command.handler, command.filters(), *args, **kwargs)

