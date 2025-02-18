from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.core.validators import MaxValueValidator

class User(AbstractUser):
    username = None  # Видаляємо username
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    phone_number = models.IntegerField(
        validators=[MaxValueValidator(9999999999)],
        blank=True,
        null=True
    )
    is_seller = models.BooleanField(default=False)

    # Унікальний ідентифікатор користувача
    user_id = models.CharField(max_length=100, unique=True)

    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name="custom_user_permissions", blank=True
    )

    USERNAME_FIELD = 'user_id'  # Використовуємо user_id як основний ідентифікатор
    REQUIRED_FIELDS = ['first_name', 'last_name', 'age']

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user_id = f"{self.first_name.lower()}_{self.last_name.lower()}_{self.pk}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user_id

class Talent_dsc(models.Model):
    prof = models.CharField(max_length=100)

class Talent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=50)
    talent_dsc = models.ForeignKey(Talent_dsc, on_delete=models.PROTECT)

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class Contract(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    talent_id = models.OneToOneField(Talent, on_delete=models.CASCADE)
    project_id = models.OneToOneField(Project, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)









