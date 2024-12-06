from django.shortcuts import render,redirect
from django.core.paginator import Paginator,EmptyPage
from django.db.models import Q

from .models import Book,Author2
from .forms import BookForm,AuthorForm
# Create your views here.
# def createbook(request):
#     books=Book.objects.all()

#     if request.method=="POST":
#         title=request.POST.get("title")
#         price=request.POST.get("price")
#         author=request.POST.get("author")

#         book=Book(title=title,price=price,author=author)
#         book.save()

#     return render(request,"book.html",{"books":books})

def detailsview(request,book_id):
    book=Book.objects.get(id=book_id)
    return render(request,'detailsview.html',{"book":book})


# def updateview(request,book_id):
#     book=Book.objects.get(id=book_id)
#     if request.method=="POST":
#         title=request.POST.get("title")
#         price=request.POST.get("price")
#         author=request.POST.get("author")

#         book.title=title
#         book.price=price
#         book.author=author
#         book.save()
#         return redirect("/")
#     return render(request,"updateview.html",{"book":book})

def updateview(request,book_id):
     book=Book.objects.get(id=book_id)
     if request.method=="POST":
          form=BookForm(request.POST,request.FILES,instance=book)
          if form.is_valid():
               form.save()
               return redirect('/')
     else:
          form=BookForm(instance=book)
     return render(request,'updateview.html',{'form':form})



def deleteview(request, book_id):
    print("book_id received:", book_id)
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('/')
    return render(request, "deleteview.html", {"book": book})

def createbook(request):
    books=Book.objects.all()
    if request.method=="POST":
       form=BookForm(request.POST,request.FILES)

       if form.is_valid():
            form.save()
    else:
           form=BookForm()

    return render(request,'book.html',{'form':form,'books':books})
def Create_author(request):
    if request.method=="POST":
        form=AuthorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
            form=AuthorForm()
            
        

    return render(request,'author.html',{'form':form})

def index(request):
     return render(request,'base.html')
def listbook(request):
     
     book=Book.objects.all().order_by('id')
     paginator=Paginator(book,4)
     page_number=request.GET.get('page')
     try:
          page=paginator.get_page(page_number)
     except EmptyPage:
          page=paginator.page(page_number.num_pages)
          
     return render(request,'listview.html',{'books':book,'page':page})

def search(request):
     query=None
     books=None
     if 'q' in request.GET:
          query=request.GET.get('q')
          books=Book.objects.filter(Q(title__icontains=query) )
     else:
        book=[]
        
     context={'books':books,'query':query}
     return render(request,'search.html',context)

