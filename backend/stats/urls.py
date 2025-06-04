from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActionViewSet

router = DefaultRouter()
router.register(r'actions', ActionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]