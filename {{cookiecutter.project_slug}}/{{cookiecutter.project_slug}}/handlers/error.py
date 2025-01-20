__all__ = ["error_handler"]

import json
import logging
import traceback

from django.conf import settings
from django.template.loader import render_to_string
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.error("Exception while handling an update:", exc_info=context.error)
    tb_list = traceback.format_exception(None, context.error, context.error.__traceback__)
    tb_string = "".join(tb_list)
    update_str = update.to_dict() if isinstance(update, Update) else str(update)
    in_data = json.dumps(update_str, indent=2, ensure_ascii=False)
    chat_data = str(context.chat_data)
    user_data = str(context.user_data)
    tb = tb_string
    message = render_to_string(
        "error.html",
        context={
            "update": in_data,
            "chat_data": chat_data,
            "user_data": user_data,
            "tb": tb,
        },
    )
    await context.bot.send_message(
        chat_id=settings.DEV_CHAT, text=message, parse_mode=ParseMode.HTML
    )
