from django.shortcuts import render
from django.views.generic import TemplateView


class Homepage(TemplateView):
    template_name = 'home/index.html'


def site_rules(request):
    return render(request, 'home/site_rules.html')
