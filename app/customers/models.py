from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Customer(models.Model):
    owner = models.ForeignKey('auth.User', related_name='customers', on_delete=models.CASCADE, default=1)
    created = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=100, blank=True)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    national_id = models.IntegerField(unique=True)
    phone_number = models.CharField(max_length=13, blank=True)
    email = models.EmailField()

    class Meta:
        ordering = ['created']
        db_table = 'customers'
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.first_name

