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

    #upload
    path('myprojects',views.myprojects, name="myprojects"),
    path('delete_myprojects/<int:pk>/', views.delete_project, name='delete_project'),
    path('myprojects/<int:id>',views.myprojects_details, name="myproject_details"),
    path('myprojects/<int:id>/add',views.addtheproject, name="addtheproject"),
    path('myprojects/<int:id>/quest',views.questtheproject, name="questtheproject"),
    path('upload', views.upload, name="upload"),

    path('card_question', views.card_question, name="card_question"),
    path('card/',views.card_list, name="card_list"),
    path('card/upload/', views.upload_card, name="upload_card"), 
    path('card/<int:pk>/', views.delete_card, name='delete_card'),
    path('classcard/',views.CardListView.as_view(), name="class_card_list"),

    
    #flashcards
    path('upload', views.upload, name="upload"),

    #documentscnaner
    path('camera', views.camera, name="camera"),
    path('documentscanner', views.documentscanner, name="documentscanner"), 

    #scraper
    path('scraper', views.scraper, name="scraper"),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
