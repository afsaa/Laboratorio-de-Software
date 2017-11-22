from django import forms


class contactForm(forms.Form):
	nombre= forms.CharField(required =False, max_length=100, help_text=' 100 caracteres maximo', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}))
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo'}))
	comentario = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese su mensaje'}))

class emailForm(forms.Form):
	email = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'para:'}), label="email")
	comentario = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese su mensaje'}))
