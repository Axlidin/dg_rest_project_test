from django.urls import path
from rest_framework.routers import SimpleRouter


from .views import (BookListApiView, book_list_view, BookDeleteApiView,
                    BookDetailApiView, BookUpdateApiView, BookCreateApiView,
                    BookListCreateApiView, BookUpdateDelateApiView, BookCreateView, BookViewSet)

router = SimpleRouter()
router.register('books', BookViewSet, basename='books')
urlpatterns = [
    # path('books/', BookListApiView.as_view()),
    # path('bookslistcreate/', BookListCreateApiView.as_view()),
    # path('book/create/', BookCreateApiView.as_view()),
    # path('book/', BookCreateView.as_view()),
    # path('booksupdatedelete/<int:pk>', BookUpdateDelateApiView.as_view()),
    # path('books/<int:pk>/', BookDetailApiView.as_view()),
    # path('books/<int:pk>/delete', BookDeleteApiView.as_view()),
    # path('books/<int:pk>/update', BookUpdateApiView.as_view()),
    # # path('book/', book_list_view),
]
urlpatterns += router.urls
