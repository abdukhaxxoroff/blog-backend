from ninja import Schema
import uuid
from datetime import datetime
from posts.schemas import PostOut
class CommentIn(Schema):
    message: str
    post: uuid.UUID

class CommentOut(Schema):
    message: str
    post: PostOut
    created: datetime
    id: uuid.UUID
