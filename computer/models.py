from django.db import models

# Create your models here.
class ComputerBrands(models.Model):
  brand_name = models.CharField(max_length=50, blank=True)
  logo = models.ImageField(upload_to='static/logos/')

  def __str__(self):
    return self.brand_name

class ComputerSpecification(models.Model):
  generation = models.CharField(max_length=50, blank=True)
  price_min = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
  price_max = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
  ram = models.IntegerField(null=True)
  brand = models.ForeignKey(ComputerBrands, blank=True, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.brand.brand_name} - {self.generation}th gen - {self.ram}GB"

class Computer(models.Model):
  computer_code = models.CharField(max_length=50, blank=True, unique=True)
  computer = models.ForeignKey(ComputerSpecification, blank=True, on_delete=models.CASCADE)
  quantity = models.IntegerField()
  unit_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
  total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

  def save(self, *args, **kwargs):
    self.total_price = self.quantity * self.unit_rate
    super().save(*args, **kwargs)

  def __str__(self):
    return self.computer_code