
from django.urls import path, include


from . import views

app_name='public'
urlpatterns = [
    path("", views.index, name='index'),
    path('accounts/', views.about, name='about'),
    path('contact',views.contact,name="contact"),
]