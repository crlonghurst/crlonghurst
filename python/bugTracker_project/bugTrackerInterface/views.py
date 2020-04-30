from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Bug

class BugListView(ListView):
    model = Bug
    template_name = './bugTrackerInterface/home.html'
    context_object_name = 'bugs'

class BugDetailView(DetailView):
    model = Bug


class BugCreateView(LoginRequiredMixin, CreateView):
    model = Bug
    fields = ['application', 'description', 'snippet']

    def form_valid(self, form):
        form.instance.addedBy = self.request.user
        return super().form_valid(form)

class BugUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Bug 
    fields = ['description', 'snippet', 'finished']

    def form_valid(self, form):
        form.instance.addedBy = self.request.user
        return super().form_valid(form)

    def test_func(self):
        bug = self.get_object()
        if self.request.user == bug.addedBy:
            return True
        return False

class BugDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Bug
    success_url = '/'


    def test_func(self):
        bug = self.get_object()
        if self.request.user == bug.addedBy:
            return True
        return False