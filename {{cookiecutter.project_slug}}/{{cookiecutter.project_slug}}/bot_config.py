{% if cookiecutter.need_examples == 'yes' %}
from telegram.ext import ConversationHandler

TEST_CB_BUTTON = "Test callback"
TEST_CONVERSATION_BUTTON = "Test conversation"

STEP1_STATE = 1
STEP2_STATE = 2
STEP3_STATE = 3
END_STATE = ConversationHandler.END

CB_TEST = "TEST"

CONVERSION_NAME = "{{cookiecutter.project_slug}}_loop"
CONVERSION_STATE = "{{cookiecutter.project_slug}}_state.pickle"
{% endif %}

CB_SEP = ":"
