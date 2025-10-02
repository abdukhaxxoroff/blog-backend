from ninja import NinjaAPI
from posts.api import router as posts_router
from comments.api import router as comments_router
from media.api import router as media_router

api = NinjaAPI()

api.add_router('/posts', posts_router)
api.add_router('/comments', comments_router)
api.add_router('/media', media_router)