from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from combine.views import removeitem
from . import views


urlpatterns = [
    #mainpage
    path('', views.home, name="home"),
    
    # path('', views.loginPage, name="login"),
    path('one', views.one),
    # path('logout', views.logoutUser, name="logout"),

    #todolist
    path('mylist', views.mylist, name="mylist"),
    path('mylist/<int:id>', removeitem),
    
    
    #flashcards
    path('upload', views.upload, name="upload"),

    #scraper
    path('scraper', views.scraper, name="scraper"),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
