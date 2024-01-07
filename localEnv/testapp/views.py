from django.shortcuts import render

from testapp.forms import StudentForm
from testapp.forms import FeedBackForms


# Create your views here.
def studentinput_view(request):
    submitted = False
    sname = ''
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print('Form validation success and print data')
            print('Name:', form.cleaned_data['name'])
            print('Roll No:', form.cleaned_data['rollno'])
            print('Marks:', form.cleaned_data['marks'])
            sname = form.cleaned_data['name']
            submitted = True
    form = StudentForm()
    return render(request, 'testapp/test.html', {'form': form, 'submitted': submitted, 'sname': sname})


def feedback_view(request):
    submitted = False
    name = ''
    form = FeedBackForms()
    if request.method == 'POST':
        form = FeedBackForms(request.POST)
        if form.is_valid():
            print('Form validation success and printing feedback information')
            print('*' * 58)
            print('Name:', form.cleaned_data['name'])
            print('Rollno:', form.cleaned_data['rollNo'])
            print('MailID:', form.cleaned_data['email'])
            print('Feedback:', form.cleaned_data['feedback'])
            submitted = True
            name = form.cleaned_data['name']
        else:
            print('else block of form.is_valid().')
            # form.save()
    return render(request, 'testapp/feedback.html', {'form': form, 'submitted': submitted, 'name': name})
