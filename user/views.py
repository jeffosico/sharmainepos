from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomAuthenticationForm, RegistrationForm
from .models import Profile
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

def unauthenticated_user(login_view):
    def wrapper_function(request):
        if request.user.is_authenticated:
            return redirect("dashboard")
        else:
            return login_view(request)

    return wrapper_function

@login_required(login_url='/login/')
def home_view(request):
    return redirect('dashboard')

@login_required(login_url='/login/')
def dashboard_view(request):
    return render(request, 'user/dashboard.html')

@unauthenticated_user
def login_view(request):
    next = request.GET.get('next') or ''

    user = request.user
    if user.is_authenticated:
        return redirect("dashboard")
    
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if next:
                print("next!")
                return redirect(next)
            else:
                return redirect("dashboard")
    else:
        form = CustomAuthenticationForm
        return render(request, 'user/login.html', {'form':form})
    return render(request, 'user/login.html', {'form':form})


@login_required(login_url='/login/')
def users_view(request):
    form = RegistrationForm()
    users = Profile.objects.all()
    context = {
        'users':users,
        'form':form
    }

    # if request.method == "POST":
    #     form = RegistrationForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #     else:
    #         print('false')
    #         context['form'] = form
    #         return render(request, 'user/users.html', context)

    return render(request, 'user/users.html', context)

def add_user_view(request):
    form = RegistrationForm(request.POST, request.FILES)
    
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    username = request.POST.get('username')
    is_admin = request.POST.get('is_admin') or False
    is_staff = request.POST.get('is_staff') or False
    if is_staff:
        role = "Staff"
    if is_admin:
        role = "Admin"
    else:
        is_admin = False
        is_staff = False

    if form.is_valid():
        user = form.save()
        print(user.username)
        return HttpResponse("<tr><td><input type='checkbox' id='checkthis' /></td><td>"+first_name+"</td><td>"+last_name+"</td><td>"+email+"</td><td>"+username+"</td><td>"+role+"</td><td><a href='' style='color:green;'><i class='fas fa-edit'></i></th></a>&nbsp;&nbsp;&nbsp;<a href='' style='color:red;'><i class='fas fa-trash-alt'></i></th></a></td><td></td></tr>")
    else:
        print(form.errors)
        return HttpResponse("Error")

def logout_view(request):
    logout(request)
    return redirect('login')