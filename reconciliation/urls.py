from django.contrib import admin
from django.urls import path

from .api import api_router

urlpatterns = api_router.get_urls() + [
    path('admin/', admin.site.urls),
]
