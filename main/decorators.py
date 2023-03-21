from django.shortcuts import redirect


def notLoggedUser(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func





def allowedUsers(allowedGroups=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                
                group = request.user.groups.all()[2].name
                
            if group in allowedGroups:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('no_permission')
        return wrapper_func
    return decorator


def tendering_main_index(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='1-tendering_main_index').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func


def tendering_user_index(view_func):
    def wrapper_func(request, *args, **kwargs):        
        if request.user.groups.filter(name='1-1-tendering_user_index').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func


def contract_main_index(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='2-contract_main_index').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func


def contract_user_index(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='2-1-contract_user_index').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func


def project_main_index(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='3-project_main_index').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func


def project_user_index(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='3-1-project_user_index').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func


def add_new_tender(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='1-2-add_new_tender').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func


def update_tender(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='1-3-update_tender').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func


def preview_tender(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='1-4-preview_tender').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func


def add_new_contract(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='2-2-add_new_contract').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func


def preview_contract(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='2-3-preview_contract').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func


def add_new_project(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='3-2-add_new_project').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func


def preview_project(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='3-3-preview_project').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('no_permission')
    return wrapper_func












