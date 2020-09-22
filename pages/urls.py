from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name="index"),

    # AUTH
    path('register/', views.register, name="register"),
]
