from django.urls import path

from . import views

app_name = 'praises'
urlpatterns = [
    # ex: /praises/
    path('', views.index, name='index'),

    # ex: /praises/20190828
    path('<int:date_text>/', views.index, name='index'),

    # ex: /praises/5/
    # path('<int:praise_id>/', views.detail, name='detail'),

    # ex: /praises/new/
    path('new/', views.new, name='new'),

    # ex: /praises/delete/3
    path('delete/<int:praise_id>/', views.delete, name='delete'),

    path('login/', views.login, name='login')
]
