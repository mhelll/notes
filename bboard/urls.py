from django.urls import path

from .views import SelfIndex

urlpatterns = [
    path('', SelfIndex.as_view(), name='self-index')
]