from django.shortcuts import render
from django.views import generic

class IndexView(generic.TemplateView):
    template_name = "train_tweet/index.html"
