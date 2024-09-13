from django import forms
from .models import Post, Category, Comment

#choices = [('coding', 'coding'), ('sports', 'sports'), ('technology', 'technology')]
choices = Category.objects.all().values_list('name', 'name')
choice_list =[]
for item in choices:
     choice_list.append(item)



class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'header_image', 'category', 'content']

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'content' :forms.Textarea(attrs={'class':'form-control'}),


        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
           
            'body' :forms.Textarea(attrs={'class':'form-control'}),

        }
