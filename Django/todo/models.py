from django.db import models
from datetime import datetime



class TodoData(models.Model):
    from users.models import User
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    desc=models.TextField()
    created=models.DateTimeField(auto_now_add=True )
    due_date = models.DateTimeField(default=datetime.now())
    complete = models.BooleanField(default=False)
