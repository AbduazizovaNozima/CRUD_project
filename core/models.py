from django.db import models

from django.db import models

class Student(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    full_name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    degree = models.CharField(max_length=200)
    birth_date = models.DateField()

    def __str__(self):
            return self.full_name
