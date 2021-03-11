from agents.views import AgentListView,AgentCreateView
from django.urls import path
app_name = 'agents'
urlpatterns = [
    path('',AgentListView.as_view(),name='agent-list'),
    path('create/',AgentCreateView.as_view(),name='agent-create')
]
