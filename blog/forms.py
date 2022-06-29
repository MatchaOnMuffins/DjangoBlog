from django import forms
from .models import Post, Comments


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'content']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'New post!'}),
            # <input type="text" class="form-control"
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'A short description'}),
            # 'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author', 'id': 'author'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Post content'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'content']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'New post! (edited)'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'A short description (edited)'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Post content (edited)'}),
        }


class AddComment(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment content'}),
        }
