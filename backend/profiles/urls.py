from django.urls import path
from .views import *


urlpatterns = [
    # path('', homepage, name='homepage'),
    path('buildings/', BuildingsList.as_view()),
    path('telegram_id/create', TelegramIDCreate.as_view())
]