from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from prayers.models import PrayerRequest
from members.models import Member

# -------------------------------
# LOGIN VIEW
# -------------------------------
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Role-based redirect
            if user.role == 'pastor':
                return redirect('pastor_dashboard')
            elif user.role == 'treasurer':
                return redirect('treasurer_dashboard')
            elif user.role == 'secretary':
                return redirect('secretary_dashboard')
            else:
                return redirect('member_dashboard')
        else:
            return render(request, 'accounts/login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'accounts/login.html')


# -------------------------------
# ROLE DECORATOR
# -------------------------------
def role_required(role):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.role != role:
                return HttpResponse("Access Denied ❌")
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


# -------------------------------
# DASHBOARDS
# -------------------------------
   
@login_required
@role_required('pastor')
def pastor_dashboard(request):
    prayers = PrayerRequest.objects.all().order_by('-created_at')

    context = {
        'prayers': prayers,
        'total_members': Member.objects.count(),
        'total_sermons': 0,  # update later
        'total_prayers': PrayerRequest.objects.count(),
        'total_announcements': 0  # update later
    }

    return render(request, 'dashboards/pastor.html', context)


@login_required
@role_required('treasurer')
def treasurer_dashboard(request):
    return render(request, 'dashboards/treasurer.html')


@login_required
@role_required('secretary')
def secretary_dashboard(request):
    return render(request, 'dashboards/secretary.html')


@login_required
def member_dashboard(request):
    return render(request, 'dashboards/member.html')


# -------------------------------
# HOME PAGE
# -------------------------------
def home(request):
    return render(request, 'home.html')