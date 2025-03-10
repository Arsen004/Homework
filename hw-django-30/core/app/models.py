from django.db import models

from django.db import models


class BaseUser(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    class Meta:
        abstract = True


class Author(BaseUser):
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} (Автор)"

class FamousAuthor(Author):
    awards = models.TextField()

    def __str__(self):
        return f"{self.name} (Знаменитый автор)"

