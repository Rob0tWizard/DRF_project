from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from base.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'base', BaseViewSet, basename='base')  # префикс base будет после api/v1/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),       #авторизация по сессиям
    path('api/v1/', include(router.urls)),  # роутер сам генерирует набор маршрутов связанных с вьюсетом!

    path('api/v1/auth/', include('djoser.urls')),                   #авторизация по  DJOSER токену
    path('api/v1/auth/', include('djoser.urls.authtoken')),         # происходит туть .../token/login/
    #re_path(r'^auth/', include('djoser.urls.authtoken')),          # ПОЧЕМУ ТО НЕ РАБОТАЕТ! ???????

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),    # авторизация по JWT token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),   # для обновления аксес токена по рефрещ, view тут из библиотеки JWT
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),      #не забудь про BEARER из настроек для токена!!!!!

    # path('api/v1/base/', BaseViewSet.as_view() ),
    # path('api/v1/base/<int:pk>/', BaseApiUpdate.as_view()),
    # path('api/v1/basedelete/<int:pk>/', BaseApiDestroy.as_view()),

]
