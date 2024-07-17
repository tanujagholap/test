from django.db import models
# Create your models here.


class Order(models.Model):
    order_id = models.IntegerField()
    title = models.CharField(max_length=20)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateField()
    updated_at = models.DateField()


