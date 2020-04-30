from django.urls import path
from .views import BugListView, BugDetailView, BugCreateView, BugUpdateView, BugDeleteView
from . import views

urlpatterns = [
    path('', BugListView.as_view(), name='bug-home'),
    path('bugTrackerInterface/<int:pk>/', BugDetailView.as_view(), name='bug-detail'),
    path('bugTrackerInterface/new/', BugCreateView.as_view(), name='bug-create'),
    path('bugTrackerInterface/<int:pk>/update/', BugUpdateView.as_view(), name='bug-update'),
    path('bugTrackerInterface/<int:pk>/delete/', BugDeleteView.as_view(), name='bug-delete'),
]