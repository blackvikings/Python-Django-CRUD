from django import forms


class ContactFrom(forms.Form):
    fullname = forms.CharField(label='Full Name',
                               max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Full Name'}))
    email = forms.EmailField(label='E-mail',
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'E-mail'}))
    content = forms.CharField(label='Add Message',
                              max_length=200,
                              widget=forms.Textarea(attrs={'class': 'form-control',
                                                           'placeholder': 'Your Message'}))
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email

class LoginFrom(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)