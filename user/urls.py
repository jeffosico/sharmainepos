from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('dashboard/', views.dashboard_view, name="dashboard"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('users/', views.users_view, name="users")
]

htmx_urlpatterns = [
    path('add-user/', views.add_user_view, name="add-user")
]

urlpatterns += htmx_urlpatterns