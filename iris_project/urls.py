
from django.contrib import admin
from django.urls import path
from iris_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),           # connects to home.html
    path('predict/', views.predict), # handles prediction form
]

