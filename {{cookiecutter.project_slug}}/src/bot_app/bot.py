import logging

from django.conf import settings
from telegram import BotCommand, Update
from telegram.ext import (
    Application,
    PicklePersistence,
    ConversationHandler,
)

{% if cookiecutter.need_examples == 'yes' %}
from {{cookiecutter.project_slug}}.handlers import (
    TestCallbackHandler,
    TestCommandHandler,
    TestMessageHandler,
    Step1Handler,
    Step2Handler,
    Step3Handler,
    FinishConversationHandler,
    FallbackHandler,
)
from {{cookiecutter.project_slug}}.bot_config import CONVERSION_STATE, CONVERSION_NAME
from {{cookiecutter.project_slug}}.bot_config import STEP1_STATE, STEP2_STATE, STEP3_STATE
{% endif %}

from {{cookiecutter.project_slug}}.handlers import error_handler


logger = logging.getLogger(__name__)

async def post_init(app: Application) -> None:
    commands = [
        BotCommand("start", "Start working"),
    ]
    await app.bot.set_my_commands(commands)


def start_bot():
    {% if cookiecutter.need_examples == 'yes' %}persistence = PicklePersistence(filepath=CONVERSION_STATE){% endif %}
    application = Application.builder().token(settings.BOT_TOKEN).post_init(post_init)
    {% if cookiecutter.need_examples == 'yes' %}application = application.persistence(persistence){% endif %}
    application = application.build()
    {% if cookiecutter.need_examples == 'yes' %}conv_handler = ConversationHandler(
        entry_points=[Step1Handler],
        states={
            STEP1_STATE: [Step2Handler, FinishConversationHandler],
            STEP2_STATE: [Step3Handler, FinishConversationHandler],
            STEP3_STATE: [FinishConversationHandler],


        },
        fallbacks=[FallbackHandler],
        name=CONVERSION_NAME,
        persistent=True,
    )
    application.add_handler(conv_handler)
    application.add_handler(TestCallbackHandler)
    application.add_handler(TestCommandHandler)
    application.add_handler(TestMessageHandler){% endif %}
    application.add_error_handler(error_handler)
    application.run_polling(allowed_updates=Update.ALL_TYPES)
