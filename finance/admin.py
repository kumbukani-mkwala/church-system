from django.contrib import admin
from .models import Payment, Expense

admin.site.register(Payment)
admin.site.register(Expense)