from django.urls import path
from .views import StoreView , StoreDetailView

urlpatterns = [
    path('', StoreView.as_view() , name='store'),
    path('<slug:slug>/', StoreDetailView.as_view() , name="store_detail"),
]