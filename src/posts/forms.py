from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'rows': '4'
    }))

    class Meta:
        model = Comment
        fields = ('title', 'content',)


class ContactForm(forms.Form):
    title = forms.CharField(label='Your message title', max_length=150)
    content = forms.CharField(widget=forms.Textarea())
