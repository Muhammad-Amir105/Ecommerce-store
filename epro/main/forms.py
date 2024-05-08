from django import forms

class ratingform(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    title = forms.CharField(max_length=100, label='Title')
    discription = forms.CharField(widget=forms.Textarea, label='Description')
    rate = forms.ChoiceField(choices=[(i, str(i)) for i in range(1, 6)])