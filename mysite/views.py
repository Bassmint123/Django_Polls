from django.shortcuts import render
from django.views.generic import TemplateView

# This is an example of a function based view
def index(request):
    template_name = "index.html"
    context = {}
    return render(request, template_name, context=context)

# This is an example of a class based view
class AboutPageView(TemplateView):
    template_name = 'about.html'