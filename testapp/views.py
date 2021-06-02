from django.shortcuts import render
from testapp.forms import EmployeeForm

# Create your views here.


def employeeView(request):
    form=EmployeeForm()
    if request.method=="POST":
        form=EmployeeForm(request.POST)

        if form.is_valid():
            form.save()


    my_dict={'form':form}
    return render(request,"home.html",my_dict)
