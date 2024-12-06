


from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("author/",views.Create_author,name='author'),
    path("createbook",views.createbook,name='createbook'),
    path("bookdetails/<int:book_id>/",views.detailsview,name='details'),
    path("update/<int:book_id>/",views.updateview,name='update'),
    path("deleteview/<int:book_id>/",views.deleteview,name='delete'),
    path("index/",views.index),
    path("",views.listbook,name='booklist'),
    path("search",views.search,name='search')
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

