from django.shortcuts import render

from modelformapp.form import StudentForms


# Create your views here.

def student_view(request):
    form = StudentForms()
    if request.method == 'POST':
        form = StudentForms(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save(commit=True)
            print("Record inserted into DB successfully...")
            form = StudentForms()
    return render(request, 'modelformapp/studentform.html', {'form': form})
