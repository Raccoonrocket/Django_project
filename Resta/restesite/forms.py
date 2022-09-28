from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=2,
        widget=forms.TextInput(
            attrs={'placeholder': 'Ваше имя', 'class': 'form-control valid'}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Ваш e-mail', 'class': 'form-control valid'}
        )
    )
    message = forms.CharField(
        min_length=10,
        widget=forms.Textarea(
            attrs={'placeholder': 'Сообщение', 'colls': 30, 'rows': 9, 'class': 'form-control w-100'}
        )
    )
