from django.urls import path
from Account import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login',views.login_account, name="Login"),
    path('logout', LogoutView.as_view(template_name= 'AppFood/logout.html'), name= "Logout"),
    path('registrar',views.register_account, name="Register"),
    path('editar_usuario', views.editar_usuario, name="EditarUser"),
]