from django.db import models
from posts.models import Post
import uuid
# Create your models here.

class Comment(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message=models.CharField()
    created = models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"Comment on {self.post.title}"
