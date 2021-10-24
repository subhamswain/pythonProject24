from django.contrib import admin
from .import models
from django.apps import apps

myapp = apps.get_app_config('api')
for model in myapp.get_models():
    admin.site.register(model)