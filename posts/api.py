from ninja import  Router
from .models import Post
from .schemas import PostIn, PostOut
import uuid
from django.shortcuts import get_object_or_404

router = Router(tags=["posts"])

@router.get("/", response=list[PostOut])
def get_posts(request):
    posts =  Post.objects.all()
    return [PostOut.from_post(request, post) for post in posts]

@router.post("/", response=PostOut)
def create_post(request, post: PostIn):
    post =  Post.objects.create(**post.dict())
    return PostOut.from_post(request, post)

@router.put("/{id}", response= PostOut)
def update_post(request, payload:PostIn, id:uuid.UUID):
    post = get_object_or_404(Post, id=id)
    post.title = payload.title
    post.likes = payload.likes
    post.save()
    return PostOut.from_post(request, post)

@router.delete("/{id}",)
def delete_post(request, id:uuid.UUID):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return {"success": True, "message": "Post deleted"}

