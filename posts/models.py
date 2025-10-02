from django.db import models
import uuid
# Create your models here.
class Post(models.Model):
    id=models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    title=models.CharField(max_length=200)
    likes=models.IntegerField(default=0)

    @property
    def comments_count(self):
        return self.comments.count

    def __str__(self):
        
        return self.title
