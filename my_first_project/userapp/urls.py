


from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path("",views.listbook_user,name='booklist'),
    path("search",views.search_user,name='search'),
    path("add_to_cart/<int:book_id>/",views.add_to_cart,name="addtocart"),
    path("view_cart/",views.view_cart,name="viewcart"),
    path("increase/<int:item_id>/",views.increase_quantity,name="increase_quantity"),
    path("decrease/<int:item_id>/",views.decrease_quantity,name="decrease_quantity"),
    path("remove_from_cart/<int:book_id>/",views.remove_from_cart,name="remove_cart"),
    path("create_checkout_session/",views.checkout_session,name='create_checkout_session'),
    path("success/",views.success,name='success'),
    path('cancel',views.cancel,name='cancel')


    
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

