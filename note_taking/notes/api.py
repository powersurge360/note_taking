from rest_framework.viewsets import ModelViewSet

from .models import Book, Note
from .serializers import BookSerializer, NoteSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
