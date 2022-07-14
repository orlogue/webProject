from django.urls import path
from .views import *

urlpatterns = [
    path('buildings/', BuildingsList.as_view()),
    path('telegram_id/create/', TelegramIDCreate.as_view()),
    path('user/<str:phone_number>/', ProfileRetrieve.as_view())
]
