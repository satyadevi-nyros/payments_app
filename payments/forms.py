from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from .models import mobile_details,otp_details,file_details,Profilepic


class signUp(forms.Form):
	password1 = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(widget=forms.PasswordInput)
	
	name=forms.CharField(max_length=100,error_messages={'required': 'This field required!'})
	email=forms.EmailField(max_length=100,error_messages={'required': 'This field required!'})
	# number=forms.IntegerField(required=True)
	# card_number=forms.IntegerField(required=True)
	# cvc=forms.IntegerField(required=True)
	# month=forms.IntegerField(required=True)
	# year=forms.IntegerField(required=True)




	number = forms.RegexField(regex=r'^\+?1?\d{10}$', 
								error_message = ("Please enter valid mobile number."))

	card_number = forms.RegexField(regex=r'^\+?1?\d{16}$', 
								error_message = ("Please enter valid card number."))

	cvc = forms.RegexField(regex=r'^\+?1?\d{3}$', 
								error_message = ("Please enter valid cvc number."))
	year = forms.RegexField(regex=r'(?:(?:20)[0-9]{2})', 
								error_message = ("Please enter valid year."))
	month = forms.RegexField(regex=r'(0[1-9]|1[012])', 
								error_message = ("Please enter valid month like 02."))
# r'((?:201)\d)'
# (0[1-9]|1[012])
# r'((?:19|20)\d\d)'
# "([1-9]|[12]\d|3[01])"

# /(?:(?:19|20)[0-9]{2})/
	CHOICES=[('plan','MONTHLY_PREMIUM'),
		 ('plan','GOLD'),
		 ('plan', 'MONTHLY_GOLD'),
		 ('plan', 'PREMIUM')]
	# class Meta:
	# 	model = User
	# 	fields = ('username', 'email', 'password')
	# "username":{'unique':('user already exits')},

	def clean_email(self):
		email = self.cleaned_data.get('email')
		username = self.cleaned_data.get('username')
		if email and User.objects.filter(email=email).exclude(username=username).count():
			raise forms.ValidationError(u'Email addresses must be unique.')
			return email
	def clean_username(self):
		username = self.cleaned_data.get('username')
		email = self.cleaned_data.get('email')
		if username and User.objects.filter(username=username).exclude(email=email).count():
			raise forms.ValidationError("user already registerd")
			return username


	# def clean_password(self):
	# 	password1 = self.cleaned_data.get('password1')
	# 	password2 = self.cleaned_data.get('password2')

	# 	if password1 != password2:
	# 		raise forms.ValidationError("Passwords don't match")
	# 		return self.password1

	def clean(self):
		# cleaned_data = super(SignUpForm, self).clean()
		password1 =self.cleaned_data.get('password1')
		password2 =self.cleaned_data.get('password2')

		if password1 and password2 and password1 != password2:
			self._errors['password2'] = self.error_class(['passwords did not match.'])
			del self.cleaned_data['password2']
		return password1






class Login(forms.Form):
	password =forms.CharField(widget=forms.PasswordInput)
	name = forms.CharField(required=True)


class OTP(forms.Form):
	otp=forms.CharField(required=True)


# class UploadFile(forms.Form):
#     title = forms.CharField(max_length=50)
#     file= forms.FileField(required=False)

class UploadFile(forms.Form):
	title = forms.CharField(max_length=50)
	file= forms.FileField(required=False)



class Upgrade(forms.Form):
	CHOICES=[('plan','MONTHLY_PREMIUM'),
		 ('plan','GOLD'),
		 ('plan','MONTHLY_GOLD'),
		 ('plan','PREMIUM')]


class searching(forms.Form):
	search= forms.CharField(max_length=150)


class linkedin_search(forms.Form):
	link_search= forms.CharField(max_length=150)

class facebook_search(forms.Form):
	fb_search= forms.CharField(max_length=150)
	
class UploadImage(forms.ModelForm):
	class Meta:
		model = Profilepic
		fields=("model_pic","Name")
		# Name= forms.CharField(max_length=150)


class checkbox(forms.Form):
	name=forms.CharField(max_length=20,required=False),
	# choices = forms.MultipleChoiceField(
	# 	choices = [('plan1','MONTHLY_PREMIUM'),
	# 	 ('plan2','GOLD'),
	# 	 ('plan3', 'MONTHLY_GOLD'),
	# 	 ('plan', 'PREMIUM')],
 # # this is optional
	# 	widget  = forms.CheckboxSelectMultiple,
	# )




	# select = forms.ChoiceField(widget=forms.Select, choices=CHOICES)

	# import os
	# fileName, fileExtension = os.path.splitext('file')

	# if fileExtension==".txt" :
	# 	#     print 'This file is flac file %s' %files
	# 	print "ja"
	# # FILE_EXT_WHITELIST = ['csv','json']

	# def clean_content(self):
	# 	content = self.cleaned_data['file']
	# 	if content:
	# 	 	file_type = content.content_type.split('/')[0]
	# 		print file_type







# class Section(models.Model):
# 	content = models.FileField(upload_to="documents")

# class SectionForm(forms.ModelForm):
# 	class Meta:
# 		model = Section
# 	FILE_EXT_WHITELIST = ['pdf','text','msword']

# 	def clean_content(self):
# 		content = self.cleaned_data['content']
# 		if content:
# 			file_type = content.content_type.split('/')[0]
# 			print file_type
# 			if len(content.name.split('.')) == 1:
# 				raise forms.ValidationError("File type is not supported.")
# 			if content.name.split('.')[-1] in self.FILE_EXT_WHITELIST:
# 				return content
# 			else:
# 				raise forms.ValidationError("Only '.txt' and '.pdf' files are allowed.")






	# def name(self):
	# 	name = self.cleaned_data.get('name')
 # 		name:{
	# 			'unique':_('user already exits')
	# 			},



	# first_name = forms.CharField(error_messages={'required': 'Please let us know what to call you!'})
	
	# number=forms.IntegerField(required=True)
	# card_number=forms.IntegerField(required=True)
	# month=forms.IntegerField(required=True)
	# year=forms.IntegerField(required=True)
	# cvc=forms.IntegerField(required=True)
	# CHOICES=[('plan','MONTHLY_PREMIUM'),
	# 	 ('plan','GOLD '),
	# 	 ('plan', 'MOMTHLY_GOLD'),
	# 	 ('plan', 'PREMIUM ')]
	# def clean_email(self):
	# 	email = self.cleaned_data.get('email')
	# 	username = self.cleaned_data.get('username')
	# 	if email and User.objects.filter(email=email).exclude(username=username).count():
	# 		raise forms.ValidationError(u'Email addresses must be unique.')
	# 		return email


	# def clean_password(self):
	# 	password1 = self.cleaned_data.get('password1')
	# 	password2 = self.cleaned_data.get('password2')

	# 	if password1 and password1 != password2:
	# 		raise forms.ValidationError("Passwords don't match")

	# 	return self.cleaned_data


	# plans=[('plan','monthly gold user'),
 #         ('plan','monthly premium user'),
 #         ('plan','gold user'),
 #         ('plan','premium user')]
	# plan = forms.ChoiceField(choices=plan, widget=forms.RadioSelect(attrs={'type' : 'radio'}), initial=1)

	# schedule = forms.ChoiceField(
 #        choices=plans, widget=forms.RadioSelect)



	# email=forms.EmailField()
	# class Meta:
	# 	model=User
	# 	fields=['username','password']



# class Signup(ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     email=forms.EmailField(required=True)
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#     # class Meta:
#     # 	fields=("mobile_number")

# 	def clean_email(self):
# 		email = self.cleaned_data.get('email')
# 		username = self.cleaned_data.get('username')
# 		if email and User.objects.filter(email=email).exclude(username=username).count():
# 			raise forms.ValidationError(u'Email addresses must be unique.')
# 			return email

# class number(ModelForm):
# 	mobile_number = forms.IntegerField(required=True)
# 	class Meta:
#             model = mobile_details
#             fields=("mobile_number")
#             exclude = ('user',)