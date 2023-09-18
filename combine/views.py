from django.shortcuts import render
from . models import ShoppingItem
from django.http import StreamingHttpResponse
import cv2
import threading

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
####################################


#flashcards
####################################
def upload(request):
    return render(request,"upload.html")
####################################

