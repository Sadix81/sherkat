from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Post
from django.shortcuts import get_list_or_404

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            "title" ,
            "description" ,
            "image"
        ]


    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) > 100:
            raise forms.ValidationError("title cant exceed 100 characters.")
        return title
    

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 100  or len(description) > 300 :
            raise forms.ValidationError("Description must be between 100 and 300 characters.")
        return description


    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if not image.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                raise forms.ValidationError("Only PNG, JPEG, and JPG files are allowed for the image.")
        return image
    
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance





