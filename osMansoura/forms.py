from django import forms
from django.forms import widgets
from osMansoura.models import Student, Track

class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields = ('fname','lname','age','student_track')
        #fields = '__all__'
        widgets={
            'fname':forms.TextInput(attrs={'class':'form-control','placeholder':'first Name'}),
            'lname':forms.TextInput(attrs={'class':'form-control','placeholder':'last Name'}),
            'age':forms.NumberInput(attrs={'class':'form-control'}),
            'student_track':forms.Select(attrs={'class':'form-control'}),
        }

class TrackForm(forms.ModelForm):
    class Meta:
        model= Track
        # fields = ('name',)
        fields = '__all__'
