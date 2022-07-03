from django.urls import path,include
from home import views
urlpatterns = [
    path('',views.IndiaNews,name="india"),
    path('world/',views.world,name="world"),
    path('india/',views.IndiaNews,name="india"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
]