from django.apps import AppConfig


class UserManagerAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_manager_app'


def ready(self):
        import user_manager_app.signals