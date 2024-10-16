from django.db import models

# Create your models here.
class Employee(models.Model):
  name = models.CharField(max_length=250)
  emp_no = models.CharField(max_length=250)  
  def __str__(self):
    return self.name

class Contract(models.Model):
    contract_number = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    client_name = models.CharField(max_length=255)

    def __str__(self):
        return self.contract_number

  
