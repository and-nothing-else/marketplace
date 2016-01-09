from django.views.generic import ListView, DetailView
from .models import Help


class HelpListView(ListView):
    model = Help
    template_name = 'help/help_list.html'
    context_object_name = 'articles'


class HelpDetailView(DetailView):
    model = Help
    template_name = 'help/help_detail.html'
    context_object_name = 'article'
