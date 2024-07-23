from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):

    content = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 5,
        'placeholder': 'Оставить комментарий',
    }))

    class Meta:
        model = Comment
        fields = ('content', )