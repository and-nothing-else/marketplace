from django import forms
from .models import Ticket, Comment
from cuser.middleware import CuserMiddleware


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['subject', 'message']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']


class CommentAdminForm(CommentForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].initial = CuserMiddleware.get_user()

    class Meta(CommentForm.Meta):
        fields = ['user', 'message']
