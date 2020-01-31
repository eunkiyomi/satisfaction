from django.urls import path, re_path

from . import views

app_name = 'praises'
urlpatterns = [
    # ex: /praises/
    path('', views.index, name='index'),

    # ex: /praises/20190828
    re_path(r'^(?P<date_text>\d{8})/$', views.index, name='index'),

    # ex: /praises/5/
    # path('<int:praise_id>/', views.detail, name='detail'),

    # ex: /praises/new/
    path('new/', views.new, name='new'),

    # ex: /praises/delete/3
    path('delete/<int:praise_id>/', views.delete, name='delete'),

    path('login/', views.login, name='login'),

    path('change-id/', views.change_id, name='change_id'),
    path('set-id/', views.set_id, name='set_id'),

    re_path(r'^(?P<date_text>\d{8})/photo/$', views.set_photo, name='set_photo'),

    path('backup/', views.backup, name='backup')
]
