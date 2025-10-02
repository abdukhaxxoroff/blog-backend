# schemas.py
from ninja import Schema
from uuid import UUID
from media.schemas import MediaOut
class PostIn(Schema):   # for creating
    title: str
    likes: int

class PostOut(PostIn):  # for reading (includes id)
    id: UUID
    comments_count: int
    media: list[MediaOut]

    @staticmethod
    def from_post(request, post):
        return PostOut(
                id=post.id,
                comments_count=post.comments_count,
                title=post.title,
                likes=post.likes,
                media=[MediaOut.from_media(request, m) for m in post.medias.all()]
            )