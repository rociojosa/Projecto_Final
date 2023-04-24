from django.urls import path
from Blog import views

urlpatterns = [
    path('', views.insertPost, name="InsertPost"),
    path('post/<str:pk>/', views.post, name= "Post"),
    path('edit/<str:pk>/', views.editPost, name= "EditPost"),
    path('post-list/', views.post_list, name='post_list'),
    path('post/<int:id>/', views.detalle_vista, name='post_detalle'),
    path(r'^(?P<pk>\d+)$', views.PostDetalle.as_view(), name="PostDetalle"),
    path('comment/<int:id>/', views.comment, name="comment_form"),
    path('comment/success', views.comment_success, name="comment_success"),
    path(r'^nuevo$', views.PostCreacion.as_view(), name="New"),
    path(r'^editar/(?P<pk>\d+)$', views.PostUpdate.as_view(), name="Edit"),
    path(r'^borrar/(?P<pk>\d+)$', views.PostDelete.as_view(), name="Delete"),

]