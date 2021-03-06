from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate
from .models import Commenti, nuovo_utente, candidato

class nome_utente(forms.Form):
    name = forms.CharField(label='nome_utente', max_length=30)

class password(forms.Form):
    password = forms.CharField(label='password', max_length=25)
    
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)    

class FormCommenti(forms.ModelForm):
    class Meta:
        model = Commenti
        fields = ('nome', 'email', 'corpo')

class registrazione(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2",]

class lavoraconnoi(forms.ModelForm):
    class Meta:
        model = candidato
        fields = ['scelta_ruolo', 'esperienza', 'nome_candidato', 'cognome_candidato', 'indirizzo_candidato', 'email_candidato', 'cellulare_candidato', 'cv']

