from django.shortcuts import render, redirect, get_object_or_404
from .models import Department, DepartmentMembership, Notification
from django.contrib.auth.decorators import login_required
# -------------------------
# JOIN DEPARTMENT
# -------------------------


@login_required
def join_department(request):

    departments = Department.objects.all()

    if request.method == "POST":

        department_id = request.POST.get("department")
        motivation = request.POST.get("motivation")

        print("DEBUG USER:", request.user)
        print("DEBUG DEPT:", department_id)

        if not department_id or not department_id.isdigit():
            return render(request, "departments/join_department.html", {
                "departments": departments,
                "error": "Please select a department properly"
            })

        obj = DepartmentMembership.objects.create(
            user=request.user,
            department_id=int(department_id),
            motivation=motivation or "",
            status="pending"
        )

        print("SAVED:", obj)  # 👈 THIS LINE

        return redirect("member_dashboard")

    return render(request, "departments/join_department.html", {
        "departments": departments
    })


# -------------------------
# APPROVE MEMBERSHIP
# -------------------------
def approve_membership(request, membership_id):

    membership = get_object_or_404(DepartmentMembership, id=membership_id)

    membership.status = "approved"
    membership.save()

    # NOTIFICATION
    Notification.objects.create(
        user=membership.user,   # ✅ correct
        message=f"You have been approved to join {membership.department.name}"
    )

    return redirect("director_dashboard")
# -------------------------
# MEMBER DASHBOARD
# -------------------------
@login_required
def member_dashboard(request):

    memberships = DepartmentMembership.objects.filter(
        user=request.user
    ).select_related('department').order_by('-created_at')

    # OPTIONAL (only if you have these models)
    sermons = Sermon.objects.all().order_by('-created_at') if 'Sermon' in globals() else []
    announcements = Announcement.objects.all().order_by('-created_at') if 'Announcement' in globals() else []

    return render(request, "member/member.html", {
        "memberships": memberships,
        "sermons": sermons,
        "announcements": announcements,
    })

# -------------------------
# CHATS
# -------------------------
def praise_chat(request):
    return render(request, "departments/praise_chat.html")


def media_chat(request):
    return render(request, "departments/media_chat.html")


def evangelism_chat(request):
    return render(request, "departments/evangelism_chat.html")