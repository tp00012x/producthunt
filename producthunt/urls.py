from django.contrib import admin
from django.urls import path, include
from products import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
