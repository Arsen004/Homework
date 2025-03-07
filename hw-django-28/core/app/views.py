from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def user_info(request):
    user = request.user
    groups = user.groups.all()
    
    print(f"Пользователь: {user.username}")
    print(f"Email: {user.email}")
    print(f"Группы: {[group.name for group in groups]}")
    print(f"Суперпользователь: {user.is_superuser}")
    print(f"Статус: {'Аутентифицирован' if user.is_authenticated else 'Не аутентифицирован'}")

    return render(request, 'user_info.html', {'user': user, 'groups': groups})
