from django.contrib import admin
from django.urls import path, include
from base.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'base', BaseViewSet, basename='base')  # префикс base будет после api/v1/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),  # роутер сам генерирует набор маршрутов связанных с вьюсетом!
    # path('api/v1/base/', BaseViewSet.as_view() ),
    # path('api/v1/base/<int:pk>/', BaseApiUpdate.as_view()),
    # path('api/v1/basedelete/<int:pk>/', BaseApiDestroy.as_view()),

]
