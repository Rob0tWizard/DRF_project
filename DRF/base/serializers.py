import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Base


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Base
        fields=('title','content','cat') # __all__ - для всех полей

# class BaseModel:
#     def __init__(self, title, content):
#         self.title=title
#         self.content=content

    #РУЧНОЙ СЕРИАЛИЗАТОР,ИЛИ КАК ЭТО РАБОТАЕТ ПОД КАПОТОМ номер 1 !
# class BaseSerializer(serializers.Serializer):
#     title=serializers.CharField(max_length=100)
#     content=serializers.CharField()
#     time_create=serializers.DateTimeField(read_only=True)
#     time_update=serializers.DateTimeField(read_only=True)
#     is_published=serializers.BooleanField(default=True)
#     cat_id=serializers.IntegerField()
#
#
#     def create(self, validated_data):
#         return Base.objects.create(**validated_data)
#
#
#     def update(self, instance, validated_data):             #инстанс - ссылканамодель , валидатед_дата - это словарьизпроверенных данных, который нужно изменить
#         instance.title=validated_data.get('title', instance.title)
#         instance.content=validated_data.get('content', instance.content)
#         instance.time_update=validated_data.get('time_update', instance.time_to_update)
#         instance.time_published=validated_data.get('time_published', instance.is_published)
#         instance.cat_id=validated_data.get('cat_id', instance.cat_id)
#         instance.save()
#         return instance
#
#     def delete(self, instance):
#         instance.delete()
#

# def encode():
#     model=BaseModel("spiderman", "peter parker")
#     model_sr=BaseSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep="\n")
#     json= JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream= io.BytesIO(b'{"title":"spiderman","content":"peter parker"}')
#     data=JSONParser().parse(stream)
#     serializer=BaseSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
