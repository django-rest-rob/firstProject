from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    #function for string rep of Employee obj
    def __str_(self):
        return self.id + '|' + self.name + '|' + self.salary
