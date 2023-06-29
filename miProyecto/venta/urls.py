from django.urls import path
from . import views


urlpatterns = [
    path('',views.index_view,name=''),
    path('index/',views.index_view,name='index'),
    path('carrito/',views.carrito_view,name='carrito'),
    path('detalle/',views.detalle_view,name='detalle'),
    path('hombre/',views.hombre_view,name='hombre'),
    path('mujer/',views.mujer_view,name='mujer'),
    path('infantil/',views.infantil_view,name='infantil'),
    path('unisex/',views.unisex_view,name='unisex'),
    path('login/',views.login_view,name='login'),
    path('register/',views.register_view,name='register'),
    
    path('producto_add/',views.producto_add, name='producto_add'),
    path("producto_del/<str:pk>", views.producto_del, name="producto_del"),
    path("producto_find/<str:pk>", views.producto_find, name="producto_find"),
    path("producto_update/", views.producto_update, name="producto_update"),
    path("producto_mod/", views.producto_mod, name="producto_mod"),
    
    path("search/", views.search, name="search"),
    path("producto_search/", views.producto_search, name="producto_search"),
    path("usuario/", views.usuario, name="usuario"),
    
    path('prueba',views.prueba, name='prueba'),
    path('usuarioAdd/',views.usuarioAdd, name='usuarioAdd'),
]