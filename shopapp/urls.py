from django.urls import path
from .views import *

from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('store',StoreViewSet,basename='store')

urlpatterns = [

    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('test/',TestView.as_view()),
    path('product/',ProductCreateListView.as_view()),
    path('product/<int:pk>/',ProductRetriveView.as_view()),
    path('category/', CategoryCreateListView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),
    

]+router.urls