# pygame_website/urls.py

from django.urls import path, include
from django_flask import urls as flask_urls

urlpatterns = [
    # ...
    path('flask/', include(flask_urls)),
]