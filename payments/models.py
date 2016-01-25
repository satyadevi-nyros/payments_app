from django.db import models
from django.contrib.auth.models import User
# Create your models here.




# class user_details(models.Model):
# 	name=models.CharField(max_length=200)
# 	email=models.EmailField(max_length=200)
# 	password=models.CharField(max_length=100)
	# password2=models.CharField(max_length=100)



class mobile_details(models.Model):
	user=models.ForeignKey(User)
	mobile_number=models.IntegerField()
	file_count=models.IntegerField()
	plan=models.CharField(max_length=100)

class otp_details(models.Model):
	otp_id=models.IntegerField()
	otp_password=models.CharField(max_length=200)

class file_details(models.Model):
	user=models.ForeignKey(User)
	title=models.CharField(max_length=200)
	file_name=models.FileField()
	file_content=models.CharField(max_length=5000)

class plan_details(models.Model):
	user=models.ForeignKey(User)
	customer_id=models.CharField(max_length=100)
	subscription_id=models.CharField(max_length=100)
	plan=models.CharField(max_length=100)

class stripe_plan_details(models.Model):
	file_count=models.IntegerField()
	plan=models.CharField(max_length=100)

	# def __str__(self):
 #    	return self.user

class Profilepic(models.Model):
    model_pic = models.ImageField(upload_to="satya", null=True, blank=True)
    Name=models.CharField(max_length=50)



# 	question_text = models.CharField(max_length=200)