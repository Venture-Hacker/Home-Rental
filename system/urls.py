from django.urls import path, re_path
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('houselist/', views.house_list, name='house_list'),
    path('createOrder/', views.order_created, name='order_create'),
    re_path(r'^(?P<id>\d+)/edit/$', views.house_update, name='house_edit'),
    re_path(r'^house/detail/(?P<id>\d+)/$', views.house_detail, name='house_detail'),
    re_path(r'^detail/(?P<id>\d+)/$', views.order_detail, name='order_detail'),
    re_path(r'^(?P<id>\d+)/delete/$', views.house_delete, name='house_delete'),
    re_path(r'^(?P<id>\d+)/deleteOrder/$', views.order_delete, name='order_delete'),
    path('contact/', views.contact, name='contact'),
    path('newhouse/', views.newhouse, name='newhouse'),
    re_path(r'^(?P<id>\d+)/like/$', views.like_update, name='like'),
    path('popularhouse/', views.popular_house, name='popularhouse'),
    path('payment_with_express/', views.payment_with_express, name='payment_with_express'),
    path('payment_with_cart/', views.payment_with_cart, name='payment_with_cart'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('ipn/', views.ipn, name='ipn'),
    path('noweasy/', views.noweasy, name='noweasy'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
]
