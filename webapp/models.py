from django.db import models

# Contact Table
class Contact(models.Model):
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255, blank = True)
	home_phone = models.IntegerField(blank = True, null = True)
	work_phone = models.IntegerField(blank = True, null = True)
	mobile = models.IntegerField(blank = True, null = True)
	fax = models.IntegerField(blank = True, null = True)
	notes = models.TextField(blank = True)
	address_first_line = models.CharField(max_length = 255, blank = True)
	address_second_line = models.CharField(max_length = 255, blank = True)
	suburb = models.CharField(max_length = 255, blank = True)
	state = models.CharField(max_length = 255, blank = True)
	country = models.CharField(max_length = 255, blank = True)
	post_code = models.IntegerField(blank = True, null = True)

	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.first_name

# Organisation Table
class Organisation(models.Model):
	name = models.CharField(max_length = 255)
	notes = models.TextField(blank = True)
	address_first_line = models.CharField(max_length = 255, blank = True)
	address_second_line = models.CharField(max_length = 255, blank = True)
	suburb = models.CharField(max_length = 255, blank = True)
	state = models.CharField(max_length = 255, blank = True)
	country = models.CharField(max_length = 255, blank = True)
	post_code = models.IntegerField(blank = True, null = True)

	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	contacts = models.ManyToManyField(Contact, blank = True)

	def __str__(self):
		return self.name

# OrganisationHistory Table
class OrganisationHistory(models.Model):
	notes = models.TextField()
	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	organisation = models.ForeignKey(Organisation, blank = True)

	class Meta:
		verbose_name_plural = "Organisation History"

# Facility Table
class Facility(models.Model):
	name = models.CharField(max_length = 255)
	notes = models.TextField(blank = True)
	address_first_line = models.CharField(max_length = 255, blank = True)
	address_second_line = models.CharField(max_length = 255, blank = True)
	suburb = models.CharField(max_length = 255, blank = True)
	state = models.CharField(max_length = 255, blank = True)
	country = models.CharField(max_length = 255, blank = True)
	post_code = models.IntegerField(blank = True, null = True)

	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	organisation = models.ForeignKey(Organisation)
	contacts = models.ManyToManyField(Contact, blank = True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Facilities"

# FacilityHistory Table
class FacilityHistory(models.Model):
	notes = models.TextField()
	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)
	
	facility = models.ForeignKey(Facility, blank = True)

	class Meta:
		verbose_name_plural = "Facility History"

# Department Table
class Department(models.Model):
	name = models.CharField(max_length = 255)
	notes = models.TextField(blank = True)
	address_first_line = models.CharField(max_length = 255, blank = True)
	address_second_line = models.CharField(max_length = 255, blank = True)
	suburb = models.CharField(max_length = 255, blank = True)
	state = models.CharField(max_length = 255, blank = True)
	country = models.CharField(max_length = 255, blank = True)
	post_code = models.IntegerField(blank = True, null = True)

	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	facility = models.ForeignKey(Facility)
	contacts = models.ManyToManyField(Contact, blank = True)

	def __str__(self):
		return self.name

# DepartmentHistory Table
class DepartmentHistory(models.Model):
	notes = models.TextField()
	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)
	
	department = models.ForeignKey(Department, blank = True)

	class Meta:
		verbose_name_plural = "Department History"


#######################
## Additional Tables ##
#######################

# WorkOrder Table
class WorkOrder(models.Model):
	name = models.CharField(max_length = 255)

	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	class Meta:
		verbose_name_plural = "Work Order"

# PurchaseOrder Table
class PurchaseOrder(models.Model):
	name = models.CharField(max_length = 255)

	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.name

# Asset Table
class Asset(models.Model):
	name = models.CharField(max_length = 255)

	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.name

# Service Table
class Service(models.Model):
	name = models.CharField(max_length = 255)

	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.name