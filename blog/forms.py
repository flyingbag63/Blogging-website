from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

class AddCommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)

    def clean_renewal_date(self):
        data = self.cleaned_data['comment']

        if not data:
            raise ValidationError(_('No comment'))


        return data
