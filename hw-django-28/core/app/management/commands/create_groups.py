from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Создает группу 'User Manager' и дает ей доступ к управлению пользователями"

    def handle(self, *args, **kwargs):
        group_name = "User Manager"

        # Создаем или получаем группу
        group, created = Group.objects.get_or_create(name=group_name)

        # Получаем все права, связанные с моделью пользователя
        user_permissions = Permission.objects.filter(content_type__model="user")

        # Добавляем права группе
        group.permissions.set(user_permissions)
        group.save()

        self.stdout.write(self.style.SUCCESS(f"Группа '{group_name}' создана и права добавлены!"))
