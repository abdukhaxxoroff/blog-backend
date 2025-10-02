
from ninja import Router,Schema
from posts.models import Post
from .models import Comment
from .schemas import CommentIn, CommentOut
import uuid
from django.shortcuts import get_object_or_404
router = Router(tags=["comments"])

@router.get("/post/{post_id}", response=list[CommentOut])
def get_comments(request, post_id:uuid.UUID):
    return get_object_or_404(Post, id=post_id).comments

@router.post("/", response=CommentOut)
def create_comment(request, payload: CommentIn):
    post = get_object_or_404(Post, id=payload.post)
    comment = Comment.objects.create(post=post, message=payload.message)
    return comment

@router.put("/{comment_id}", response=CommentOut)
def edit_comment(request, payload: CommentIn, comment_id:uuid.UUID):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.message = payload.message
    comment.save()
    return comment

@router.delete("/{comment_id}")
def delete_comment(request, comment_id: uuid.UUID):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return {"success": True, "message": "Comment deleted"}


    # e42cdbbf-e4aa-4e24-b73d-13c35f670f1d