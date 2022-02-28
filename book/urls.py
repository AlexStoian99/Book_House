from django.urls import path

from . import views

app_name = 'book'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('books_list/', views.BooksList.as_view(), name='books_list'),
    path('authors_list/', views.AuthorsList.as_view(), name='authors_list'),
    path('library_list/', views.LibraryList.as_view(), name='library_list'),
    path('create_books/', views.create_book, name="create_book"),
    path('<pk>/update', views.BooksUpdateView.as_view(), name='update_books'),
    path('create_author/', views.create_author, name="create_author"),
    path('<pk>/update_author', views.AuthorUpdateView.as_view(), name='update_author'),
    path('create_library/', views.create_library, name='create_library'),
    path('<pk>/update_library', views.LibraryUpdateView.as_view(), name='update_library'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('<pk>/delete_book', views.DeleteBook.as_view(), name='delete_book'),
    path('<pk>/delete_author', views.DeleteAuthor.as_view(), name='delete_author'),
    path('<pk>/delete_library', views.DeleteLibrary.as_view(), name='delete_library'),
    path('register/', views.register_view, name='register'),

]
