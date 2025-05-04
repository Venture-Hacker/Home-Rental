from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from system.views import admin_house_list, admin_msg, order_list, house_created, order_update, order_delete, msg_delete, newhouse
from accounts.views import login_view, register_view, logout_view
from payment.views import success, cancel
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminn', admin_house_list, name='adminIndex'),
    path('listOrder/', order_list, name="order_list"),
    re_path(r'^(?P<id>\d+)/editOrder/$', order_update, name="order_edit"),
    re_path(r'^(?P<id>\d+)/deleteOrder/$', order_delete, name="order_delete"),
    path('create/', house_created, name="house_create"),
    path('message/', admin_msg, name='message'),
    re_path(r'^(?P<id>\d+)/deletemsg/$', msg_delete, name="msg_delete"),
    path('', include('system.urls')),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('newhouse/', newhouse, name="newhouse"),
    path('success/', success, name="success"),
    path('cancel/', cancel, name="cancel"),

    # Password reset URLs using path()
    path('reset_password/', 
         auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), 
         name="reset_password"),

    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
         name="password_reset_confirm"),

    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), 
         name="password_reset_complete"),
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
