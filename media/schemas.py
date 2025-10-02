from ninja import Schema
import uuid
class MediaOut(Schema):
    id: uuid.UUID
    file: str

    @staticmethod
    def from_media(request, media):
        return MediaOut(id=media.id, file=request.build_absolute_uri(media.file.url))