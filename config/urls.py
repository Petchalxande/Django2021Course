from django.contrib import admin
from django.urls import path

from environs import Env

env = Env()
env.read_env()


urlpatterns = [
    path(env("ADMIN_URL"), admin.site.urls),
]