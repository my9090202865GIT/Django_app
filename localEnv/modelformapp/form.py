from django import forms
from modelformapp.models import Student


class StudentForms(forms.ModelForm):
    name = forms.CharField()
    marks = forms.IntegerField()

    class Meta:
        model = Student
        fields = '__all__'

    def clean(self):
        print("clean called.")
        form_cleaned_data = super().clean()
        if len(form_cleaned_data['name']) < 4:
            raise forms.ValidationError("Name should be >4")

