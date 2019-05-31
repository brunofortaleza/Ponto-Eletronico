from django.urls import path
from . import views
from app_frequencia.views import HomePageView, frequencia

urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('frequencia', frequencia, name = 'frequencia')
]