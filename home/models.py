from django.db import models

# Create your models here.
class department(models.Model):
    department_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50 , null=False)

    def __str__(self):
        return f"{self.department_id},{self.name}"