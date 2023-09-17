from django.shortcuts import render
from . models import ShoppingItem

# Create your views here.


def home(request):
    return render(request, "home.html")

def one(request):
    return render(request, "home2.html")


#####################################
# first project todolist

def mylist(request):
    if request.method == 'POST':
        print('Received data: ', request.POST['itemName'])
        ShoppingItem.objects.create(name = request.POST['itemName']) 

    all_items = ShoppingItem.objects.all()
    return render(request,"shopping_list.html", {'all_items': all_items})

def removeitem(request, * ,id):
 
    print('Received data: ', id)
    ShoppingItem.objects.filter(id=id).delete()

####################################


#docuscanner
####################################

def docuscanner(request):
    return render(request, 'docuscanner.html')

####################################


#scraper
####################################
def scraper(request):
    return render(request, 'scraper.html')
####################################


#flashcards
####################################
def upload(request):
    return render(request,"upload.html")
####################################

