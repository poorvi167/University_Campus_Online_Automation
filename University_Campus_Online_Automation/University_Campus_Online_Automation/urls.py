
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('student/', include('Student.urls')),
    path('accounts/', include('accounts.urls')),
    path('', views.home_page,name="home"),
path('dashboard/', views.dashboard,name="dashboard"),

]

urlpatterns += staticfiles_urlpatterns()
