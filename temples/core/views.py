from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Church, Comment


class MainListView(ListView):
    model = Church
    context_object_name = 'main_list'
    template_name = 'core/index.html'


class ObjectDetailView(DetailView):
    model = Church
    context_object_name = 'object'
    template_name = 'core/object_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    # if request.method == 'POST':
    #     new_comment = request.POST['comment']  #
    # Comment.objects.create(text=new_comment)  #
    # else:
    # new_comment = ''  #
    # return render(request, 'core/object_detail.html', {
    #     'new_comment': new_comment,  #
    # })
