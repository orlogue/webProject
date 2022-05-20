from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'profiles', ProfilesViewSet)

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', profile_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', homepage, name='homepage'),
    path('api/', include(router.urls)),

]