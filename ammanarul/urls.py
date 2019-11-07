from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('choices', views.choices, name='choices'),
    path('premium', views.premium_list, name='premium_list'),
    path('premium/upload', views.upload_premium, name='upload_premium'),
    path('intense', views.intense_list, name='intense_list'),
    path('intense/upload', views.upload_intense, name='upload_intense'),
    path('special', views.special_list, name='special_list'),
    path('special/upload', views.upload_special, name='upload_special'),
]
