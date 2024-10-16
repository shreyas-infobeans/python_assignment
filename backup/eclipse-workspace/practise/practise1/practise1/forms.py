from django import forms

class UsersForm(forms.Form):
  name = forms.CharField()
  email = forms.EmailField()
  message = forms.CharField(label="value 3",required=False,widget=forms.Textarea(attrs={'class':'form-control'}))
