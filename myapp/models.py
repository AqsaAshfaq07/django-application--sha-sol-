from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title 

@receiver(post_save, sender=Product)  
def instance_created_at(sender, instance, created, **kwargs):
    if created:
        instance.created_at = instance.created_at or timezone.now()
        instance.save()
