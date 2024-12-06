from django.shortcuts import render,redirect
from my_app.models import Book
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from userapp. models import CartItem,Cart
import stripe
from django.conf import settings
from django.urls import reverse

# Create your views here.
def search_user(request):
     query=None
     books=None
     if 'q' in request.GET:
          query=request.GET.get('q')
          books=Book.objects.filter(Q (title__icontains=query) )
     else:
        book=[]
        
     context={'books':books,'query':query}
     return render(request,'search.html',context)

def listbook_user(request):
     
     book=Book.objects.all().order_by('id')
     paginator=Paginator(book,4)
     page_number=request.GET.get('page')
     try:
          page=paginator.get_page(page_number)
     except EmptyPage:
          page=paginator.page(page_number.num_pages)
          
     return render(request,'list.html',{'books':book,'page':page})
# def listbook_user(request):
#     books = Book.objects.all().order_by('id')  # Fetch all books ordered by ID
#     paginator = Paginator(books, 4)  # Paginate with 4 books per page
#     page_number = request.GET.get('page')  # Get the page number from the request

#     try:
#         page = paginator.get_page(page_number)  # Get the books for the current page
#     except EmptyPage:
#         page = paginator.page(paginator.num_pages)  # Fall back to the last page if invalid

#     return render(request, 'list.html', {'books': page})


def detailsview_user(request,book_id):
    book=Book.objects.get(id=book_id)
    return render(request,'detailsview.html',{"book":book})

# def add_to_cart(request,book_id):
#      book=Book.objects.get(id=book_id)
#      if book.quantity>0:
#           cart, created =Cart.objects.get_or_create(user=request.user)
#           cart_item,item_created=CartItem.objects.get_or_create(cart=cart,book=book)

#           if not item_created:
#                cart_item.quantity+=1
#                cart_item.save()
#      return redirect('viewcart')
from django.shortcuts import render, redirect
from my_app.models import Book
from userapp.models import CartItem, Cart

def add_to_cart(request, book_id):
    # Get the book with the given book_id
    book = Book.objects.get(id=book_id)
    
    # Check if the book is available in stock
    if book.quantity > 0:
        # Get or create the cart for the user
        cart, created = Cart.objects.get_or_create(user=request.user)
        
        # Get or create a CartItem for this specific book and cart
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, book=book)

        # If the cart item already exists, increase the quantity
        if not item_created:
            cart_item.quantity += 1
            cart_item.save()

    return redirect('viewcart')



def view_cart(request):
     cart,created=Cart.objects.get_or_create(user=request.user)
     cart_items=cart.cartitem_set.all()
     cart_item=CartItem.objects.all()
     total_price=sum(item.book.price*item.quantity for item in cart_items)
     total_items=cart_item.count()

     context={'cart_items':cart_item,'cart_item':cart_item,'total_price':total_price,'total_items':total_items}

     return render(request,'cart.html',context)

def increase_quantity(request,item_id):
     cart_item=CartItem.objects.get(id=item_id)
     if cart_item.quantity< cart_item.book.quantity:
          cart_item.quantity+=1
          cart_item.save()
     return redirect('viewcart')

def decrease_quantity(request,item_id):
     cart_item=CartItem.objects.get(id=item_id)
     if cart_item.quantity>1:
          cart_item.quantity-=1
          cart_item.save()
     return redirect('viewcart')

def remove_from_cart(request,item_id):
    
     try :
          cart_item=CartItem.objects.get(id=item_id)
          cart_item.delete()
     except cart_item.DoesNotExist:
          pass

def checkout_session(request):
     cart_items=CartItem.objects.all()

     if cart_items:
          stripe.api_key=settings.STRIPE_SECRET_KEY

          if request.method=='POST':
               line_items=[]
               for cart_item in cart_items:
                    if cart_item.book:
                         line_item={
                              'price_data':{
                                   'currency':'INR',
                                   'unit_amount':int(cart_item.book.price *100),
                                   'product_data':{
                                        'name':cart_item.book.title
                                   }
                                   
                              },
                              'quantity':1
                         }
                         line_items.append(line_item)
               if line_items:
                    checkout_session=stripe.checkout.Session.create(
                         payment_method_types=['card'],
                         line_items=line_items,
                         mode='payment',
                         success_url=request.build_absolute_uri(reverse('success')),
                         cancel_url=request.build_absolute_uri(reverse('cancel')),

                    )
                    return redirect(checkout_session.url,code=303)
               
def success(request):
     cart_items=CartItem.objects.all()
     for cart_item in cart_items:
          product=cart_item.book
          if product.quantity>=cart_item.quantity:
               product.quantity-=cart_item.quantity
               product.save()
     
     cart_item.delete()

     return render(request,'success.html')

def cancel(request):
     return render(request,'cancel.html')
          

    

     
