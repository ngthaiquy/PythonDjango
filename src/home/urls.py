from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('contact/', views.about, name='contact'),
    # path('blog/', views.blogs),


]
