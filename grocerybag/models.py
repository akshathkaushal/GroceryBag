from django.db import models
from django.contrib.auth.models import User

'''class customList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="origin", null=True)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name'''


# Create your models here.
class listItem(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="origin")
    #origin = models.ForeignKey(customList, on_delete=models.CASCADE, null=True)
    user_email = models.EmailField(null=True)

    UNITS = (
        ('kg', 'Kgs'),
        ('gm', 'Grams'),
        ('l', 'Litres'),
        ('ml', 'Mililitres'),
        ('m', 'Metres'),
        ('cm', 'Centimetres')
    )
    STAT = (
        ('Bought','Bought'),
        ('Left','Left'),
        ('Not-Available','Not-Available')
    )
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=50, choices=UNITS, default='kg')
    status = models.CharField(max_length=50, choices=STAT, default='L')
    date = models.DateField(blank=False, null=True)

    def __str__(self):
        return self.name