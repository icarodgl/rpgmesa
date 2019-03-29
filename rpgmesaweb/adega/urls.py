"""rpgmesaweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="Index"),
    path('listar/vendedores/', views.listar_vendedores, name="Listar vendedores"),
    path('listar/vendas/todas/<int:mes>/<int:ano>', views.Listar_vendas_periodo, name="Listar todas vendas periodo"),
    path('listar/vendas/<int:vendedor_id>', views.Listar_vendas_periodo, name="Listar vendas vendedor"),
    path('listar/vendas/<int:vendedor_id>/<int:mes>/<int:ano>', views.Listar_vendas_periodo_vendedor, name="Listar vendas vendedor periodo"),
    path('nova/venda/', views.nova_venda, name="Nova venda"),
    path('novo/produto/', views.novo_produto, name="Novo produto"),
    path('editar/produto/<int:id>', views.editar_produto, name="editar produto"),
    path('editar/venda/<int:id>', views.editar_venda, name="editar produto"),
]