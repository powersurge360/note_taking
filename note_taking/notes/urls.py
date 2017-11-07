from rest_framework.routers import DefaultRouter

from .api import BookViewSet, NoteViewSet


router = DefaultRouter()
router.register(r'book', BookViewSet)
router.register(r'note', NoteViewSet)

urlpatterns = router.urls
