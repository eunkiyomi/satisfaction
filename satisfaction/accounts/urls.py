from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    # ex: /praises/
    path('', views.index, name='index'),
]
