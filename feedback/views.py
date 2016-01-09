from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .models import Ticket
from .forms import TicketForm, CommentForm
from django.shortcuts import redirect


class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'feedback/ticket_list.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TicketDetailView(LoginRequiredMixin, DetailView):
    model = Ticket
    template_name = 'feedback/ticket_detail.html'
    context_object_name = 'ticket'

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, pk=self.kwargs['pk'], user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm(self.request.POST or None)
        return context

    def get(self, request, *args, **kwargs):
        ticket = self.get_object()
        ticket.is_read_by_user = True
        ticket.save()
        return super().get(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            ticket = self.get_object()
            instance = form.save(commit=False)
            instance.user = self.request.user
            instance.ticket = ticket
            instance.save()
            return redirect(ticket.get_absolute_url())
        return super().get(*args, **kwargs)


class TicketCreateView(LoginRequiredMixin, CreateView):
    form_class = TicketForm
    template_name = 'feedback/ticket_create.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return redirect(instance.get_absolute_url())
