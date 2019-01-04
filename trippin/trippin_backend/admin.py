from django.contrib import admin
from .models import Trip, Restaurant, Activity
from django.contrib.auth import get_user_model 
from django.contrib.auth.admin import UserAdmin 
from .forms import CustomUserCreationForm, CustomUserChangeForm 
from .models import CustomUser 


# Register your models here.
class CustomUserAdmin(UserAdmin): 
    add_form = CustomUserCreationForm 
    form = CustomUserChangeForm 
    model = CustomUser 
    list_display = ['email', 'username', 'name'] 


admin.site.register(Trip)
admin.site.register(Restaurant)
admin.site.register(Activity)
admin.site.register(CustomUser, CustomUserAdmin)


    
    