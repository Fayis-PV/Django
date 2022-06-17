from django.urls import path
from . import views

app_name = "cla"
urlpatterns = [
    path('',views.index, name = 'index'),
    path('about',views.about, name = 'about'),
    path('computer',views.computer, name = 'computer'),
    path('laptop',views.laptop, name = 'laptop'),
    path('product',views.product, name = 'product'),
    path('contact',views.contact, name = 'contact'),
    path('login',views.login, name = 'login'),
    path('signup',views.signUp, name = 'signup')
]
