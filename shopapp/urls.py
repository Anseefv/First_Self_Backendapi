from django.urls import path
from .views import *
urlpatterns = [

    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('test/',TestView.as_view()),
    path('product/',ProductCreateListView.as_view()),
    path('product/<int:pk>/',ProductRetriveView.as_view()),
    

]