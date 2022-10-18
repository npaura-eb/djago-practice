from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Todo


class TodoListView(ListView):
    # model = Todo
    def get_queryset(self):
        return Todo.objects.filter(user_assigned=self.request.user)

class TodoCreateView(CreateView):
    model = Todo
    fields = ['name', 'description', 'done', 'priority']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_assigned = self.request.user
        self.object.save()
        return super().form_valid(form)

class TodoDetailView(DetailView):
    model = Todo

# hacer: update un elemento, delete elemento, reasignar a otro usuario, 
# paginar lista inicial, cualquire package (oauth),
# login/logout, redirect login