from django.template import Context
from django.shortcuts import render_to_response
from address.models import Author, Book

def insertbook(request):
    if request.POST:
        post = request.POST
        try:
            exit_author = Author.objects.get(Name = post["authorname"])
            new_book = Book(
                ISBN = post["ISBN"],
                Title = post["Title"],
                authorname = post["authorname"],
                AuthorID = exit_author,
                Publisher = post["Publisher"],
                PublishDate = post["PublishDate"],
                Price = post["Price"])
            new_book.save()
            return render_to_response("insertbook_ok.html")
        except:
            new_author = Author(
                Name = post["authorname"],
                Age = "NULL",
                Country = "NULL")
            new_author.save()
            
            new_book = Book(
                ISBN = post["ISBN"],
                Title = post["Title"],
                authorname = post["authorname"],
                AuthorID = new_author,
                Publisher = post["Publisher"],
                PublishDate = post["PublishDate"],
                Price = post["Price"])
            new_book.save()
            return render_to_response("addauthor.html",Context({"new_author":new_author}))
    return render_to_response("insertbook.html")
    
    
def insertauthor(request):
    id = request.GET["id"]
    author = Author.objects.get(id=int(id))
    if request.POST:
        post = request.POST
        author.Age = post["Age"]
        author.Country = post["Country"]
        author.save()
        return render_to_response("insertauthor_ok.html")
    return render_to_response("insertauthor.html",Context({"new_author":author}))

def allbook(request):
   book_list = Book.objects.all()
   c = Context({"book_list":book_list,})
   return render_to_response("allbook.html", c)
   
def allauthor(request):
   author_list = Author.objects.all()
   c = Context({"author_list":author_list,})
   return render_to_response("allauthor.html", c)
   
def deleteok(request):
    id = request.GET["id"] 
    book = Book.objects.get(id=int(id))
    book.delete()
    return render_to_response("deleteok.html",id)
    
def detail(request):
    id = request.GET["id"]
    book = Book.objects.get(id=int(id))
    return render_to_response("detail.html",Context({"book":book}),Context({"author":book.AuthorID}))

def update(request):
    id = request.GET["id"]
    book = Book.objects.get(id=int(id))
    if request.POST:
        post = request.POST
        book.authorname = post["authorname"]
        book.Publisher = post["Publisher"]
        book.PublishDate = post["PublishDate"]
        book.Price = post["Price"]
        book.save()
        return render_to_response("allbook.html",id,Context({"book_list":Book.objects.all(),}))
    return render_to_response("update.html",id,Context({"book":book}))
    
def insertauthor_ok(request):
    return render_to_response("insertauthor_ok.html")
    
def search(request):
    return render_to_response("search.html")
    
def find(request):
    c=Context({"book_list":Book.objects.filter(authorname = request.GET["Name"])})
    return render_to_response("find.html",c)