from django.db import models

# Create your models here.

class UserLogin(models.Model):
    username=models.CharField(max_length=50, null=True)
    password=models.CharField(max_length=50, null=True)
    utype=models.CharField(max_length=50, null=True)


class AddTender(models.Model):
    location = models.CharField(max_length=50, null=True)
    company = models.CharField(max_length=50, null=True)
    tender_type = models.CharField(max_length=50, null=True)
    total_budget = models.CharField(max_length=50, null=True)
    starting_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    year = models.CharField(max_length=4, null=True)

class AddContractors(models.Model):
    name = models.CharField(max_length=50, null=True)
    qualification = models.CharField(max_length=50, null=True)
    experience = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=500, null=True)
    mobile_no = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    profile_photo = models.FileField(upload_to='documents', null=True)
    status = models.CharField(max_length=100, null=True)

class AddCategory(models.Model):
    category_name = models.CharField(max_length=50, null=True)

class AddMaterialUsages(models.Model):
    tender_location = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=50, null=True)
    uom = models.CharField(max_length=50, null=True)
    qty = models.IntegerField(null=True)
    usage_date = models.DateField(null=True)
    price = models.IntegerField(null=True)
    total = models.IntegerField(null=True)


class AddTenderBooking(models. Model):
    tender_id = models.CharField(max_length=50, null=True)
    contractor_id = models.CharField(max_length=50, null=True)
    booking_date = models.DateField(null=True)
    booking_time = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, null=True)

class AddComplaint(models.Model):
    contractor_id = models.CharField(max_length=50, null=True)
    about_work = models.CharField(max_length=50, null=True)


    suggestions = models.CharField(max_length=50, null=True)

class NewTenderProgress(models.Model):
    contractor_id = models.CharField(max_length=50, null=True)
    tender_id = models.CharField(max_length=50, null=True)
    work_per = models.IntegerField(null=True)
    entry_date = models.DateField(null=True)
    upload_photo = models.FileField(upload_to='documents/', null=True)


class OtpCodeNew(models.Model):
    otp = models.IntegerField(null=True)
    status = models.CharField(max_length=50, null=True)





