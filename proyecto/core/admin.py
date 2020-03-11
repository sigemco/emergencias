from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserSigemco
from django.contrib.auth.models import Group
from .forms import SignUpForm, GroupAdminForm

# Register your models here.


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    #form = UserChangeForm
    add_form = SignUpForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'email', 'is_active', 'is_staff')
    list_filter = ('username', 'email',)
    fieldsets = (
        ('Datos del usuario', {'fields': ('username', 'email', 'password')}),
        ('Permisos', {'fields': ('is_active', 'is_staff',
                                 'is_superuser', 'groups', 'user_permissions')}),
        ('Datos de ingreso y creación', {
         'fields': ('last_login', 'date_joined')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class RoleAdmin(admin.ModelAdmin):
    '''
        Admin View for Sigemco
    '''
    list_display = ('nombre',)


admin.site.register(UserSigemco, UserAdmin)

# Unregister the original Group admin.
admin.site.unregister(Group)


# Create a new Group admin.
class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']


# Register the new Group ModelAdmin.
admin.site.register(Group, GroupAdmin)
