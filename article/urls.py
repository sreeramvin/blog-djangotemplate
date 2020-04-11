from django.urls import path
from django.conf.urls import url
from . import views


app_name="article"
urlpatterns = [
    path('',views.artilce_list, name="list"),
    path('create/',views.article_create,name="create"),
    path('<slug:slug_n>/', views.article_detail, name="detail"),
  
]