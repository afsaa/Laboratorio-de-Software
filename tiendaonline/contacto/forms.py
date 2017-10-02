from django import forms


class contactForm(forms.Form):
	nombre= forms.CharField(required =False, max_length=100, help_text='100 caracteres maximo')
	email = forms.EmailField(required=True)
	comentario = forms.CharField(required=True, widget=forms.Textarea)