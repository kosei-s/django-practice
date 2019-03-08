from django.shortcuts import render
from django.views import generic
from .models import Train

class IndexView(generic.TemplateView):
    template_name = "train_tweet/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["foo"] = Train.objects.get(pk=1).line
        return context
