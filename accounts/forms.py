from django import forms
from . import models
from django.contrib.auth.forms import UserChangeForm
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget

class ProfileForms(forms.ModelForm):
    class Meta:
        model = models.ProfileModel
        fields = '__all__'
############################################################################
class UserCreationForm(forms.ModelForm):

    class Meta:
        model = models.users
        fields = ('username','password','email','phonenumber')
############################################################################
class LoginForm(forms.ModelForm):
    class Meta:
        model = models.users
        fields = ('username','password')
############################################################################
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = models.ProfileModel
        fields = ('location' , 'home' , 'zipcode' , 'melicode' , 'email' , 'birthday', 'name' )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'rectangle4'} ),
            'location': forms.TextInput(attrs={'class': 'rectangle36' }),
            'home': forms.TextInput(attrs={'class': 'rectangle30' }),
            'zipcode': forms.TextInput(attrs={'class': 'rectangle34' }),
            'melicode': forms.TextInput(attrs={'class': 'rectangle35' }),
            'email': forms.TextInput(attrs={'class': 'rectangle33' }),
        }
        labels ={
            'name':'',
            'location':'',
            'home':'',
            'zipcode':'',
            'melicode':'',
            'email':'',
        }

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['birthday'] = JalaliDateField(label=(''),  widget=AdminJalaliDateWidget)








############################################################################
class UserEditForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = '__all__'
############################################################################
class FavForm(forms.ModelForm):
    model = models.ProfileModel
    fields = ('favorites')
############################################################################
class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('content',)