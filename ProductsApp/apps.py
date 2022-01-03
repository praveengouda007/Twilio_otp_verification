from django.apps import AppConfig


class ProductsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ProductsApp'

    def ready(self):
        from ProductsApp import schedule
        schedule.start()
