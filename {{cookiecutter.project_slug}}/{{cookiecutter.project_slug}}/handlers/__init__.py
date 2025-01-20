{% if cookiecutter.need_examples == 'yes' %}
from .examples import *
{% endif %}
from .error import *