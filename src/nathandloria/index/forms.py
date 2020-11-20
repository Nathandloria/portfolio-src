from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField()
    first_name.label = 'First Name'

    last_name = forms.CharField()
    last_name.label = 'Last Name'

    email = forms.EmailField()
    email.label = 'Email'

    main_text = forms.CharField(widget=forms.Textarea(attrs={'rows': 4,}))
    main_text.label = 'Your Message'
