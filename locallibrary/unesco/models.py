from django.db import models

class Category(models.Model) :
    #id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Region(models.Model):
	#id = models.AutoField(primary_key=True)
	name = models.CharField(unique=True, max_length=100)

	def __str__(self):
		return self.name

class States(models.Model):
	#id = models.AutoField(primary_key=True)
	name = models.CharField(unique=True, max_length=100)

	def __str__(self):
		return self.name

class Iso(models.Model):
	#id = models.AutoField(primary_key=True)
	name = models.CharField(unique=True, max_length=100)

	def __str__(self):
		return self.name

class Site(models.Model):
	#id = models.AutoField(primary_key=True)
	name = models.CharField(unique=True, max_length=255)
	description = models.TextField(blank=True, null=True)
	justification = models.TextField(blank=True, null=True)
	#year = models.TextField(blank=True, null=True)
	year = models.CharField(blank=True, null=True, max_length=255)
	#longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
	#longitude = models.FloatField(blank=True, null=True)
	longitude = models.CharField(blank=True, null=True, max_length=255)
	#latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
	#latitude = models.FloatField(blank=True, null=True)
	latitude = models.CharField(blank=True, null=True, max_length=255)
	area_hectares = models.FloatField(blank=True, null=True)
	#area_hectares = models.CharField(blank=True, null=True, max_length=255)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	#states = models.CharField(max_length=255)
	states = models.ForeignKey(States, on_delete=models.CASCADE)
	#region = models.CharField(max_length=255)
	region = models.ForeignKey(Region, on_delete=models.CASCADE)
	#iso = models.CharField(max_length=255)
	iso = models.ForeignKey(Iso, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
