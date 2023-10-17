from django.apps import AppConfig


class WebToolsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'common_web_tools_lab.web_tools'

    def ready(self):
        import common_web_tools_lab.web_tools.signals