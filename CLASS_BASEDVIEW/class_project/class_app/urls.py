from django.urls import path, include
from . import views
urlpatterns = [
    path("",views.Booklistview.as_view(),name='booklist'),
    path("CreateView/",views.BookCreateView.as_view(),name='createbook'),
    path("detailsview/<int:pk>/",views.Bookdetailview.as_view(),name='details'),
    path("updateview/<int:pk>/",views.Bookupdateview.as_view(),name='update'),
    path("deleteview/<int:pk>/",views.Bookdelete.as_view(),name='delete'),
]
