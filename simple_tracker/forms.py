from django import forms
from django.forms import ModelForm, TextInput, NumberInput
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
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class':'form-control text-center',
                                    'autofocus': 'true',
                                    'placeholder': 'Class name here'
                                    }),
            'misses': NumberInput(attrs={'class':'form-control text-center'}),
        }
