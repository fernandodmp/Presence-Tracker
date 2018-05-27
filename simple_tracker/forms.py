from django import forms
from django.forms import ModelForm, TextInput, NumberInput, EmailInput, PasswordInput
from django.contrib.auth.models import User
from simple_tracker.models import Course

class DeleteForm(forms.Form):
    course_choice = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices = [], label = '')

    def __init__(self, *args, **kwargs):
        super(DeleteForm, self).__init__(*args, **kwargs)
        self.fields['course_choice'] = forms.ChoiceField(choices=[(course.name, course.name) for course in Course.objects.order_by('misses')],
                                                         widget=forms.Select(attrs={'class': 'form-control'}),
                                                         label = ''
                                                        )

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'misses',)
        widgets = {
            'name': TextInput(attrs={'class':'form-control text-center',
                                    'autofocus': 'true',
                                    'placeholder': 'Class name here'
                                    }),
            'misses': NumberInput(attrs={'class':'form-control text-center'}),
        }

class UserForm(ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Password'}))
    confirm_password= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Confirm Password'}))
    class Meta():
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': TextInput(attrs={'class':'form-control',
                                    'autofocus': 'true',
                                    'placeholder': 'John Doe'
                                    }),
            'email': EmailInput(attrs={'class':'form-control',
                                    'placeholder': 'you@example.com'
                                    }),         
        }

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )