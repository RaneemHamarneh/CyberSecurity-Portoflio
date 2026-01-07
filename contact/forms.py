from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=120)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, max_length=4000)

    # Honeypot field (keep hidden in the template)
    company = forms.CharField(required=False)

    def clean_company(self):
        value = self.cleaned_data.get("company", "")
        if value:
            raise forms.ValidationError("Spam detected.")
        return value
