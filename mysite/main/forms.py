from django import forms
from .models import Comment, Search


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'text')
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Ваше имя",
                        }),
            "text": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Ваш комментарий...",
                       }),

        }
class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ('text',)
        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'input',
                "placeholder": "Введите название книги",
            })
        }
# class NewLetterForm(forms.ModelForm):
#     class Meta:
#         model = NewsLetter
#         widgets = {
#             'email': forms.EmailInput(attrs={
#                 'class': 'input',
#                 "placeholder": "Ваш email",
#             }),
#         }
