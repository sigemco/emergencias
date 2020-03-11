from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import UserSigemco

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import Group


class SignUpForm(UserCreationForm):
    # Agregar campos aca si quiero agregar datos adicionales, sino directamente en class Meta
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Opcional')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Opcional.')
    email = forms.EmailField(
        max_length=254, help_text='Necesario. Informar una dirección de correo electrónico válida.')

    class Meta:
        model = UserSigemco
        #fields = ('username', 'first_name', 'last_name', 'email', 'bio','location','birth_date','password1', 'password2', )
        #roles = forms.ModelMultipleChoiceField(queryset=Rol.objects.all(),  widget=forms.SelectMultiple(), required=True)
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )


#User = get_user_model()
User = UserSigemco

# Create ModelForm based on the Group model.


class GroupAdminForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = []

    # Add the users field.
    usuarios = forms.ModelMultipleChoiceField(
        queryset=UserSigemco.objects.all(),
        required=False,
        # Use the pretty 'filter_horizontal widget'.
        widget=FilteredSelectMultiple('usuarios', False)
    )

    def __init__(self, *args, **kwargs):
        # Do the normal form initialisation.
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        # If it is an existing group (saved objects have a pk).
        if self.instance.pk:
            # Populate the users field with the current Group users.
            self.fields['usuarios'].initial = self.instance.user_set.all()

    def save_m2m(self):
        # Add the users to the Group.
        self.instance.user_set.set(self.cleaned_data['usuarios'])

    def save(self, *args, **kwargs):
        # Default save
        instance = super(GroupAdminForm, self).save()
        # Save many-to-many data
        self.save_m2m()
        return instance
