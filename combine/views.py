from django.shortcuts import render, redirect
from . models import ShoppingItem
from django.http import StreamingHttpResponse
from django.shortcuts import render, redirect
from . models import ProjectItem
from django.core.files.storage import FileSystemStorage
from . forms import CardForm
from . models import Card
from . models import Book
import os
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import pandas as pd
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

###### hier versucht alles mit python zu machen, es ist aber wesentlich einfach mit javascript 
#
# def camera(request):
#     try:
#         cam = VideoCamera()
#         return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
#     except:
#         pass
#     return render(request, 'app1.html')
# class VideoCamera(object):
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)
#         (self.grabbed, self.frame) = self.video.read()
#         threading.Thread(target=self.update, args=()).start()
#     def __del__(self):
#         self.video.release()
#     def get_frame(self):
#         image = self.frame
#         _, jpeg = cv2.imencode('.jpg', image)
#         return jpeg.tobytes()
#     def update(self):
#         while True:
#             (self.grabbed, self.frame) = self.video.read()
# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def camera(request):
    return render(request, 'camera.html')

def documentscanner(request):

    
    return render(request, 'documentscanner.html')


####################################


#scraper
####################################
def scraper(request):
    return render(request, 'scraper.html')

def regroupbyhtml(request):
    books = Book.objects.all()
    context={
        'books': books,
    }
    return render(request, 'regroupbyhtml.html', context)

def chart(request):
    data = Book.objects.all()
    books = Book.objects.all()
    
    query = Book.objects.all().query
    query.group_by=['name']
    
    df = pd.DataFrame(data)

    noDuplicateRows = df.drop_duplicates()

    # noDuplicateNames = df.drop_duplicates(subset=['name'])

    
    # after=request.GET.get('after', None)
    # before=request.GET.get('before', None)

    # rdata = Book.objects.filter(name=True).order_by('-id')[0]
    # rdata = Book.objects.reverse()[0]

    rdata = Book.objects.order_by('-id')
    ldata = Book.objects.order_by('-id')[0]
    context={
        'rdata': rdata,
        'data':data,
        'ldata':ldata,
        'df':df.to_html(),
        'noDuplicateRows' : noDuplicateRows,
        'books' : books,
        
    }
   
    return render(request, "chunkychart.html",context)
# # to remove duplicate data and create a list of items to choose which item to display
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html

# to display the scraped data create a new html document
# display all the data set with all should be a thing

# to display individual item types you have to filter
# by a variable chooseable frome the no duplicate names list would be ideal
# https://docs.djangoproject.com/en/4.2/topics/db/queries/

####################################


#flashcards
####################################
def upload(request):
    return render(request,"upload.html")

def myprojects(request):
    if request.method == 'POST':  
        print('Received data: ', request.POST['itemName'])
        ProjectItem.objects.create(name = request.POST['itemName']) 

    project_items = ProjectItem.objects.all()
    return render(request,"uploadd/myprojects.html", {'project_items': project_items})

def myprojects_details(request, * , id):
    row_id = ProjectItem.objects.get(id = id)
    cards=Card.objects.filter(side=id)
    return render(request,"uploadd/theproject.html",{'row':row_id,'cards':cards})

def delete_project(request, pk):
    if request.method == "POST":
        projectitem = ProjectItem.objects.get(pk=pk)
        projectitem.delete()
    return redirect('myprojects')

def addtheproject(request, * , id):
    row_id = ProjectItem.objects.get(id = id)
    cards=Card.objects.all()

    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            front = form.cleaned_data['front']
            back = form.cleaned_data['back']
            title = form.cleaned_data['title']
            # print("hez")
            card = Card.objects.create(title=title,front=front,back=back,side=id)
            card.save()
            return redirect('/myprojects/'+str(id))

    else: 
        form = CardForm()
    return render(request,"uploadd/addtheproject.html",{'row':row_id,'cards':cards,'form':form})

def questtheproject(request, *, id):

    cards=Card.objects.all()
    projectcards = cards.filter(side=id)
    row_id = None
    
    try:
         
        after=request.GET.get('after', None)
        before=request.GET.get('before', None)
        both=after and before
        if after is not None:
            questioncard=projectcards.filter(id__gt=after).order_by('id')[0]
        elif before is not None:
            questioncard=projectcards.filter(id__lt=before).order_by('-id')[0]
        # elif both:
        #     questioncard=Card.objects.filter(id__gt=after).order_by('id')[0]
        else:
            print("hiiii")
            questioncard=projectcards.order_by('id')[0]
    
    except IndexError:
        if len(cards) > 0:
            questioncard=projectcards[0]
    except ValueError:
        if len(cards) > 0:
            questioncard=projectcards[0]
    return render(request,"uploadd/questionmodal.html",{'row':row_id,'cards':cards, 'questioncard': questioncard,'projectcards':projectcards })

def card_list(request):
    cards=Card.objects.all()
    return render(request, 'uploadd/card_list.html', {'cards': cards})

def card_question(request, *, id):
    cards=Card.objects.all()
    questioncard=None
    try:
         
        after=request.GET.get('after', None)
        before=request.GET.get('before', None)
        both=after and before
        if after is not None:
            questioncard=Card.objects.filter(id__gt=after).order_by('id')[0]
        elif before is not None:
            questioncard=Card.objects.filter(id__lt=before).order_by('-id')[0]
        # elif both:
        #     questioncard=Card.objects.filter(id__gt=after).order_by('id')[0]
        else:
            questioncard=Card.objects.all().order_by('id')[0]
    except IndexError:
        if len(cards) > 0:
            questioncard=cards[0]
    except ValueError:
        if len(cards) > 0:
            questioncard=cards[0]
    
    return render(request, 'uploadd/questionmodal.html', {'cards': cards,'questioncard': questioncard })

def upload_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            # print("hez")
            form.save()
            return redirect('/card/')

    else: 
        form = CardForm()

    return render(request,'uploadd/upload_card.html',{'form' : form})

def delete_card(request, pk):
    if request.method == "POST":
        card = Card.objects.get(pk=pk)
        if card.front:
            
            os.remove(card.front.file.name)
        if card.back:
            os.remove(card.back.file.name)
        card.delete()
    return redirect('card_list')

class CardListView(ListView):
    model=Card
    template_name="card_list.html" 
    context_object_name = 'card'

####################################

