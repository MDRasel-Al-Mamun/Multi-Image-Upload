from django.urls import path
from .views import HomeView, uploadView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('upload/', uploadView, name='upload')
]
