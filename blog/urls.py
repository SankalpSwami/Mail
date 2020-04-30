from django.urls import path
from . import views
from .views import ComposeDetailView, ComposeCreateView
from django.views.generic import TemplateView

urlpatterns = [
	path('inbox', views.inbox, name='blog-inbox'),
	path('compose/<int:pk>/', ComposeDetailView.as_view(), name='compose-detail'),
	path('compose/new/', ComposeCreateView.as_view(), name='compose-create'),
	path('index/', views.mail, name='mail'),
	path('sent/', views.sent, name='blog-sent'),
]