from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from filters import MyModelFilter


class MyModelViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,)  # Подключаем библотеку, отвечающую за фильтрацию к CBV
    filter_set_class = MyModelFilter  # Выбираем наш фильтр
