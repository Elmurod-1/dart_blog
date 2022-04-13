from django.urls import path
from .views import index, single

urlpatterns = [
    path('', index, name='home'),
    path('article/<slug:slug>/', single, name='single'),
]


