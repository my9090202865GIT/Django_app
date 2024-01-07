from django import forms
from django.core import validators


class StudentForm(forms.Form):
    name = forms.CharField()
    marks = forms.IntegerField()
    rollno = forms.IntegerField()


class FeedBackForms(forms.Form):
    name = forms.CharField()
    rollNo = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea,
                               validators=[validators.MaxLengthValidator(20), validators.MinLengthValidator(3)])

    def clean_name(self):
        print('validating name')
        inputname = self.cleaned_data['name']
        if len(inputname) < 4:
            raise forms.ValidationError("Error message")
        return inputname

    def clean(self):
        cleaned_data=super().clean()
        print("clean method called.-->",cleaned_data)
