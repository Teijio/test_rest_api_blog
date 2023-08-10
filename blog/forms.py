from django import forms
from django.core.exceptions import ValidationError

from .models import Subscriptions


class SubscriptionsForm(forms.ModelForm):
    class Meta:
        model = Subscriptions
        fields = ("user", "blog")

    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get("user")
        blog = cleaned_data.get("blog")
        if user == blog.owner:
            raise ValidationError("You can't subscribe to your blog.")
