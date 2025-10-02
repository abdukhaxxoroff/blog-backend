from ninja import Router, File, UploadedFile
from media.schemas import MediaOut
from django.shortcuts import get_object_or_404
from posts.models import Post
from typing import List
from posts.schemas import PostOut
import uuid
from media.models import Media
router = Router(tags=["media"])

@router.patch("/upload", response=MediaOut)
def upload_media(request, file: UploadedFile = File(...)):
    media = Media.objects.create(file=file)
    return MediaOut.from_media(request, media)

@router.get("/all", response=list[MediaOut])
def get_all_media(request):
    medias =  Media.objects.all()
    return [MediaOut.from_media(request, media) for media in medias]

# 1. Get all media of a post
@router.get("/post/{post_id}", response=list[MediaOut])
def get_post_media(request, post_id: uuid.UUID):
    post = get_object_or_404(Post, id=post_id)
    return PostOut.from_post(request, post).media


# 2. Upload MANY files for a single post
@router.post("/upload/{post_id}", response=PostOut)
def upload_media(request, post_id: uuid.UUID, files : File[list[UploadedFile]]):
    post = get_object_or_404(Post, id=post_id)

    for f in files:  # 👈 use Django’s request.FILES
        Media.objects.create(post=post, file=f)
    
    
    return PostOut.from_post(request, post)


# 3. Replace a single media file (edit)
@router.put("/{media_id}", response=MediaOut)
def update_media(request, media_id: uuid.UUID, file: UploadedFile = File(...)):
    media = get_object_or_404(Media, id=media_id)
    media.file = file
    media.save()
    return MediaOut.from_media(request, media)


# 4. Delete a media
@router.delete("/{media_id}")
def delete_media(request, media_id: uuid.UUID):
    media = get_object_or_404(Media, id=media_id)
    media.delete()
    return {"success": True, "message": "Media deleted"}
