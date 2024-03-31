from django import forms

class EmailForm(forms.Form):
    recipient =  forms.EmailField()
    cc = forms.EmailField(required=False)
    bcc = forms.EmailField(required=False)
    message = forms.CharField(widget= forms.Textarea)
    attachment = forms.FileField(required=False)