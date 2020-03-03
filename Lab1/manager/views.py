from django import views
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, ListView

from manager.constants import STATUS_CHOICES
from manager.models import Task


class MainView(views.View):
    def get(self, request):
        try:
            option = request.GET['option']
        except:
            option = 'Undone'

        finally:
            aaa = None

            if option == 'Undone':
                temp = '-status'
            elif option == 'Done':
                temp = 'status'
            else:
                aaa = 15
                temp = 'id'

            tasks = Task.objects.all().order_by(temp, 'deadline')

            return render(
                request,
                'main.html',
                context={'tasks': tasks, 'choices': STATUS_CHOICES, 'option': option, 'aaa': aaa}
            )


class TaskUpdateView(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'update_obj.html'

    def get_success_url(self):
        return reverse_lazy('main')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete_obj.html'

    def get_success_url(self):
        return reverse_lazy('main')


class TaskCreateView(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'create_obj.html'

    def form_valid(self, form):
        self.object = Task(**form.cleaned_data)
        self.object.save()

        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('main')


