from django.urls import path
from .import views
app_name ="leads"

urlpatterns = [
    path('' ,views.lead_list,name="home"),
    path('<pk>/',views.lead_detail,name="details")
]
