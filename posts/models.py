from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    discription=models.TextField(max_length=155)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    due_data=models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    