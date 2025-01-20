from django.core.management.base import BaseCommand

from {{cookiecutter.project_slug}}.bot import start_bot


class Command(BaseCommand):
    help = "Запуск бота {{cookiecutter.bot_name}}"

    def handle(self, *args, **options):
        start_bot()
