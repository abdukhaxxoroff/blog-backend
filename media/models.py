from django.db import models
from posts.models import Post
import uuid

class Media(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file=models.FileField(upload_to="media/")
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name="medias", null=True)