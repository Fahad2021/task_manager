from django.urls import path
from .views import TodoListCreateView, TodoDetailView,TodoListView,TodoUpdateView,TodoDeleteView

urlpatterns = [
    path('todo/', TodoListCreateView.as_view(), name='todo-list-create'),
    path('todo/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('todo/all/', TodoListView.as_view(), name='all-todo-list'),  
    path('todo/delete/<int:pk>/', TodoDeleteView.as_view(), name='todo-delete'), 
    path('todo/update/<int:pk>/', TodoUpdateView.as_view(), name='todo-update'), 
]