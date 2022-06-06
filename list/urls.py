from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('add/', views.add, name="add"),
        path('login/', views.login, name="login"),
        path('viewall/', views.viewall, name="viewall"),
        path('view/<str:ID>', views.view, name="view"),
        path('addItemInTodoList/<str:Email>', views.addItemInTodoList, name="addItemInTodoList"),
        path('updateItemOfTodoList/<str:Email>/<str:ID>', views.updateItemOfTodoList, name="updateItemOfTodoList"),
        path('delete/<str:Email>/<str:ID>', views.delete, name="delete"),
    ]