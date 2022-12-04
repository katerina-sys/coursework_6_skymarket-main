from django.urls import include, path

# TODO настройка роутов для модели
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from ads.views import AdViewSet, CommentViewSet

ads_router = SimpleRouter()

# обратите внимание, что здесь в роуте мы регистрируем ViewSet,
# который импортирован из приложения Djoser
ads_router.register("users", AdViewSet, basename="ads")
comments_router = NestedSimpleRouter(ads_router, "ads", lookup="ad")
comments_router.register("comments", CommentViewSet)


urlpatterns = [
    path("", include(ads_router.urls)),
    path("", include(comments_router.urls))

]
