from django.shortcuts import render,redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm ,UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from .models import Record

from django.contrib import messages
from django.db.models import Q

def home(request):
    #return HttpResponse('Hello Django')
    return render(request, 'webapp/index.html')

# Register a User View
def register(request):
    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():
            messages.success(request, "Account created successfuly!")
            form.save()
            
            return redirect('my-login')
    context = {'form' : form}

    return render(request , 'webapp/register.html', context=context)

# Login a User view

def my_login(request):

    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username , password = password)

            if user is not None:

                auth.login(request, user)
                messages.success(request, "You have logged in successfuly!")
                return redirect('dashboard')
    context = {'form': form}

    return render(request, 'webapp/my-login.html', context )


# dashboard view 
@login_required(login_url='my-login')
def dashboard(request):
    query = request.GET.get('q')
    my_records = Record.objects.all()

    if query:
        my_records = my_records.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) 
            
            )
        
    context = {'records' : my_records,'query': query}

    return render(request, 'webapp/dashboard.html',context)


# Creating a record
@login_required(login_url='my-login')
def create_record(request):

    form = CreateRecordForm()

    if request.method == "POST":
        form = CreateRecordForm(request.POST)

        if form.is_valid():
            form.save() 
            messages.success(request, "Record created successfully!")
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'webapp/create-record.html', context)


# Update the record
@login_required(login_url='my-login')
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)

    if request.method == "POST":
        form = UpdateRecordForm(request.POST , instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully!")
            return redirect("dashboard")
    context = {'form': form}
    return render(request, 'webapp/update-record.html', context)

# View Single Record
@login_required(login_url='my-login')
def singular_record(request, pk):

    all_records = Record.objects.get(id=pk)
    context = {'record' : all_records}

    return render(request, 'webapp/view-record.html',context )

# Delete a record
@login_required(login_url='my-login')
def delete_record(request, pk):
    
    all_records = Record.objects.get(id=pk)
    all_records.delete()
    messages.success(request, "Record deleted successfully!")
    return redirect("dashboard")


# Log out user view
def user_logout(request):

    auth.logout(request)
    messages.success(request, "User logged out!")
    return redirect("my-login")