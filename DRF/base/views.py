from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Base, Category
from .serializers import BaseSerializer
from rest_framework.views import APIView


#class BaseViewSet(viewsets.ModelViewSet):               #один этот вьюсет заменяетнам все 3 ручных класса номер 2!
class BaseViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):

    queryset = Base.objects.all()
    serializer_class = BaseSerializer

        #если не хватает функционала роутера инужны иные урл выводы, исп ДЕКОРАТОР экшен
    @action(methods=['get'], detail=True)       #детаил фолс выдает список записей, тру - одну
    def category(self, request, pk=None):                 #новый маршрут формируется по имени метода
        cats= Category.objects.get(pk=pk)
        return Response({'cats': cats.name})

#           РАБОТА РУЧКАМИ, РУЧНЫЕ ПРЕДСТАВЛЕНИЯ,номер 2 !
# class BaseApiList(generics.ListCreateAPIView):
#     queryset = Base.objects.all()
#     serializer_class = BaseSerializer
#
#
# class BaseApiUpdate(generics.UpdateAPIView):
#     queryset = Base.objects.all()  # отправляться будет только одна измененная запись,тк это ленивый запрос
#     serializer_class = BaseSerializer  # базовый класс сам обработает запрос вернет только изм запись
#
#
# class BaseApiDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Base.objects.all()
#     serializer_class = BaseSerializer

#               РАБОТА РУЧКАМИ, КЛАСС ПРЕДСТАВЛЕНИЯ,номер 1 !
# class BaseApiView(APIView):  # класс APIView связывает запрос и метод, метод прописываем сами
#     def get(self, request):
#         bse = Base.objects.all()
#         return Response({"posts": BaseSerializer(bse, many=True).data})
#
#     def post(self, request):
#         serializer = BaseSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)  # исключение чтобдобавлять записи
#         serializer.save()
#
#         return Response({'post': serializer.data})  # запустит метод криэйт из serializers.py
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"eror": "method PUT not allowed"})
#
#         try:
#             instance = Base.objects.get(pk=pk)
#         except:
#             return Response({'error': 'method does not exist'})
#
#         serializer = BaseSerializer(data=request.data, instance=instance)  # instance - этоточтомы хотим изменить
#         serializer.is_valid(raise_exception=True)
#         serializer.save()  # если мы одновременно передаем и DATA и INSTANCE, то срабатываетметод UPDATE
#         return Response({'post': serializer.data})
#
#
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"eror": "method DELETE is not allowed"})
#
#         try:
#             instance= Base.objects.get(pk=pk)
#         except:
#             return Response({'error': 'method does not exist'})
#
#         serializer=BaseSerializer(data=request.data,instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.delete(instance)
#         return Response({'post':'delete post'+str(pk)})
