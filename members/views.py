from django.shortcuts import render

def member_dashboard(request):
    return render(request, "member/member_dashboard.html")