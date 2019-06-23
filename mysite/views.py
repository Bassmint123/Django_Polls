from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    template_name = "index.html"
    context = {}
    return render(request, template_name, context=context)


class AboutPageView(TemplateView):
    template_name = 'about.html'