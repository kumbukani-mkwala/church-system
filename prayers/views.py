from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PrayerRequest


@login_required
def submit_prayer(request):
    if request.method == 'POST':
        message = request.POST['message']
        is_private = request.POST.get('is_private') == 'on'

        PrayerRequest.objects.create(
            user=request.user,
            message=message,
            is_private=is_private
        )

        return redirect('member_dashboard')

    return render(request, 'prayers/submit_prayer.html')


@login_required
def view_prayers(request):
    prayers = PrayerRequest.objects.all().order_by('-created_at')
    return render(request, 'prayers/view_prayers.html', {'prayers': prayers})