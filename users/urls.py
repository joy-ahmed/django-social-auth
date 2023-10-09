from django.urls import path

from users import views


urlpatterns = [
    path('', views.home, name='home'),
    path('logout', views.logout_page, name='logout'),
]
