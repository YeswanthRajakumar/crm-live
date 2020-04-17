from django.shortcuts import redirect
from django.http import HttpResponse


def login_and_registerpage_restriction_after_authenticated(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:

            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized......')

        return wrapper_func

    return decorator


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        group = request.user.groups.all()[0].name
        print('G-Group :', group)
        if group == 'Admin':
            return view_func(request, *args, **kwargs)
        if group == 'Customer':
            return redirect('user-page')
    return wrapper_func
