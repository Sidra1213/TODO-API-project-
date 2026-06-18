from django.urls import path
from .views import TodoView

urlpatterns = [
    path('posts/', TodoView.as_view()),
    path('posts/<int:todo_id>/', TodoView.as_view()), # user_id ko todo_id kiya
]