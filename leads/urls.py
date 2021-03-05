from django.urls import path
from .import views
app_name ="leads"

urlpatterns = [
    path('all/' ,views.home_page,name="home")
]
