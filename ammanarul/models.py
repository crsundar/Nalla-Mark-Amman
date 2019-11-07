from django.db import models
from datetime import date
from datetime import timedelta
import datetime



class Post(models.Model):
	STUDENT = '(Student) Almighty Nalla Mark Amma, please help me get good marks in my exams.'
	JOBSEEKER = '(Jobseeker) Almighty Nalla Mark Amma, please help me get a good job.'
	EMPLOYED = '(Employed) Almighty Nalla Mark Amma, please help me get get the promotion that I am looking forward to.'
	PARENT = '(Parent) Almighty Nalla Mark Amma, please help my child.'
	MARRIAGEHELP = '(Marriage Help) Almighty Nalla Mark Amma, please help me to get married.'
	FAMILYPROBLEMS ='(Family Problems) Almighty Nalla Mark Amma, please solve my family problems.'
	prayer = [
		(STUDENT, '(Student) Almighty Nalla Mark Amma. Please help me get good marks in my exams.'),
		(JOBSEEKER, '(Jobseeker) Almighty Nalla Mark Amma, please help me get a good job.'),
		(EMPLOYED, '(Employed) Almighty Nalla Mark Amma, please help me get get the promotion that I am looking forward to.'),
		(PARENT, '(Parent) Almighty Nalla Mark Amma, please help my child.'),
		(MARRIAGEHELP, '(Marriage Help) Almighty Nalla Mark Amma, please help me to get married.'),
		(FAMILYPROBLEMS, '(Family Problems) Almighty Nalla Mark Amma, please solve my family problems.'),
    ]

	name = models.CharField(max_length=50)
	town = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	phone = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	prayer = models.CharField(max_length=200, choices=prayer, default=STUDENT,)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	created_on = models.DateField(default=date.today)
	display_upto = models.DateField(default=date.today() + datetime.timedelta(days=28))
	profile = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.name


class Intense(models.Model):
	name = models.CharField(max_length=50)
	town = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	phone = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	prayer = models.TextField(max_length=400)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	created_on = models.DateField(default=date.today)
	display_upto = models.DateField(default=date.today() + datetime.timedelta(days=28))
	profile = models.ImageField(upload_to='images/')
	
	def __str__(self):
		return self.name


class Special(models.Model):
	name = models.CharField(max_length=50)
	town = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	phone = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	prayer = models.TextField(max_length=1000)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	created_on = models.DateField(default=date.today)
	display_upto = models.DateField(default=date.today() + datetime.timedelta(days=28))
	profile = models.ImageField(upload_to='images/')
	
	def __str__(self):
		return self.name		