from django.urls import path
from Blog import views

urlpatterns = [
    path('', views.insertPost, name="InsertPost"),
    path('post/<str:pk>/', views.post, name= "Post"),
    path('edit/<str:pk>/', views.editPost, name= "EditPost"),

]