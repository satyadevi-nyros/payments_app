from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import mobile_details,otp_details,file_details,plan_details,stripe_plan_details,Profilepic
from .forms import signUp,Login,OTP,UploadFile,Upgrade,searching,linkedin_search,facebook_search,UploadImage,checkbox
from django.template import RequestContext
from django.template import Context
from django.core.context_processors import csrf

from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render_to_response
import stripe
from twilio.rest import TwilioRestClient
from django.shortcuts import redirect
import os
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
# from django.contrib import auth.user_logged_out
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import logout
from django.core.mail import send_mail

# def email(request):
# 	name="satya"
# 	admin_email="satyatulasi518@gmail.com"
# 	mail="satyavanapalli101@yopmail.com"
# 	send_mail('Email verification for Online File Uploading', 'Dear %s,\n\nThank you for registered with Online File Uploading.\n Thanks for using our site. \n\n\n,Sincerely\n Online File Uploading.com'%(name),admin_email,[mail],fail_silently=False)	
# 	return HttpResponse("success.")
# from django.conf import settings
# import requests
# import csv
# def send(request):
# 	requests.post(
#         "https://api.mailgun.net/v3/sandbox8169e89897ab472bae3c2b510d933f00.mailgun.org/messages",
#         auth=("api", "key-696fb9278223dd4019661081a7b60513"),
#         data={"from": "Excited User <mailgun@sandbox8169e89897ab472bae3c2b510d933f00.mailgun.org>",
#               "to": "satyadevi123@yopmail.com",
#               "subject": "Hello",
#               "text": "Testingggggggg some Mailgun awesomness!"},
#                 "recipient-variables": ('{"satyadevi123@yopmail.com.com"}','{"satyadevi124@yopmail.com.com"}')})



# def send_template_message():
#     return requests.post(
#         "https://api.mailgun.net/v3/sandbox8169e89897ab472bae3c2b510d933f00.mailgun.org/messages",
#         auth=("api", "key-696fb9278223dd4019661081a7b60513"),
#         data={"from": "Excited User <tulasilakshmi59@gmail.com>",
#               "to": ["satyadevi123@yopmail.com.com, satyadevi124@yopmail.com.com"],
#               "subject": "Hey, %recipient.first%",
#               "text": "If you wish to unsubscribe, click http://mailgun/unsubscribe/%recipient.id%'",
#               "recipient-variables": ('{"satyadevi123@yopmail.com.com", '
#                                       '"satyadevi124@yopmail.com.com"')})






	# print "************"
	# print settings.BASE_DIR
	# path = '%s/email.csv'%(settings.BASE_DIR)
	# print path
	# with open(path,'rb') as f:
	# 	data=[tuple(line) for line in csv.reader(f)]
	# 	for store in data:
	# 		print store[0]
	# 		print store[1]

			# requests.post(
			# 	"https://api.mailgun.net/v3/sandbox24c9814cb27e4f0d9b2c869b557f28ec.mailgun.org",
			# 	auth=("api", "key-1e03fe95d640730376053e8bba12302b"),
			# 	data={"from": "Mailgun Sandbox <postmaster@sandbox24c9814cb27e4f0d9b2c869b557f28ec.mailgun.org>",
			# 		  "to": 'satyadevi123@yopmail.com',						"subject": "ggHello %s"%(store[1]),
			# 		  "text": "dddCongratulations %s, you just sent an email with Mailgun!  You are truly awesome!  You can see a record of this email in your logs: https://mailgun.com/cp/log .  You can send up to 300 emails/day from this sandbox server.  Next, you should add your own domain so you can send 10,000 emails/month for free."%(store[1])})
		

	# return HttpResponse("success.")



from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
	logout(request)
	return render(request, 'payments/logout.html')






# def membership_required(fn=None):
#     decorator = user_passes_test(my_custom_authenticated)
#     if fn:
#         return decorator(fn)
#     return decorator
# from django.http import HttpResponseRedirect
# def myuser_login_required(f):
# 		def wrap(request, *args, **kwargs):
# 			print "^&()_^&%#$&"
# 			# print text
# 			num_details=mobile_details.objects.filter(user_id=1)
# 			print num_details
# 				#this check the session if userid key exist, if not it will redirect to login page
# 				if 'userid' not in request.session.keys():
# 						return redirect("/uploading/1")
# 				return f(request, *args, **kwargs)
# 		wrap.__doc__=f.__doc__
# 		wrap.__name__=f.__name__
# 		return wrap



def plan_data(request):
	stripe_plan_details(file_count=2,plan="MONTHLY_GOLD").save()
	stripe_plan_details(file_count=5,plan="MONTHLY_PREMIUM").save()
	stripe_plan_details(file_count=20,plan="GOLD").save()
	stripe_plan_details(file_count=500,plan="PREMIUM").save()
	return redirect('/signup/%s')

def home(request):
	return render(request, 'payments/index_base.html')


def check(request):
	if request.method=='POST':
		# print "ja"
		# if 'plan1' in request.POST:
		# 	print "plan1"
		# else:
		# 	print "plan2"
		form = checkbox(request.POST)
		# name1=request.POST.get("plan1")
		# print name1
		# name2=request.POST.get("plan2")
		# print name2
		# name3=request.POST.get("plan3")
		# print name3
		# name4=request.POST.get("plan4")
		# print name4
		# print form
		if form.is_valid():
			print request.POST
			# print "fhfffffffffffffffffffffffffffffffffffffff"
			# # plans=request.POST.get("plan")
			# print "djfffffffffffffffff"
			d=[]
			print len(request.POST.get("plan1", ""))		
			print request.POST.get("plan2", "")
			print request.POST.get("plan3", "")
			print request.POST.get("plan4", "")

	else:
		form=checkbox()
	return render(request, 'payments/check.html',{'form':form})


	

def image_upload(request):
	if request.method == 'POST':
		print "posttttttttt"

		form = UploadImage(request.POST,request.FILES)
		print form
		data_file=request.FILES['model_pic']
		name=request.POST.get("Name")
		print name
		print data_file
		if form.is_valid():
			print "valied"
			print form
			form.save()
		# print form
			
					# messages.info(request, 'Invalied OTP')
		else:
			print"invale"
	else:
		form=UploadImage()
	return render(request,'payments/upload.html',{"form":form})


def image_update(request):
	image=Profilepic.objects.filter(id=15)
	print image
	for i in image:
		print i.model_pic
		print i.id
		print i.Name
	if request.method == 'POST':
		form = UploadImage(request.POST,request.FILES)
		pic=request.FILES['model_pic']
		name=request.POST.get("Name")
		print name
		print pic
		if form.is_valid():
			print "valied"
			image=Profilepic.objects.filter(id=15).update(model_pic=pic,Name=name)
			print image
		else:
			print "invalid"
	else:
		form=UploadImage()

	return render(request,'payments/image_update.html',{"form":form})





def signup(request):
	print "DDD"

	form=signUp()
	plans=[]
	if request.method == 'POST':
		print"hai"
		form = signUp(request.POST)
		# token = request.POST['card_number']
		# print token
		if form.is_valid():
			print "ok"
			name=request.POST.get("name")
			mail=request.POST.get("email")
			pwd=request.POST.get("password1")
			number=request.POST.get("number")
			plans=request.POST.get("plan")
			print pwd
			print "@@@@@@@@@@"
			print plans
			print "@@@@@@@@@@"
			# print "MONTHLY_GOLD"
			card = request.POST['card_number']
			month = request.POST['month']
			year = request.POST['year']
			cvc = request.POST['cvc']
			try:
			
				user = User.objects.create_user(name, mail, pwd)
				if(plans=="MONTHLY_GOLD"):
					print "gole1"
					s=mobile_details(user=user, mobile_number=number,file_count=2,plan=plans).save()
				elif(plans=="MONTHLY_PREMIUM"):
					print "gole2"
					s=mobile_details(user=user, mobile_number=number,file_count=5,plan=plans).save()
				elif(plans=="GOLD"):
					print "gole3"
					s=mobile_details(user=user, mobile_number=number,file_count=20,plan=plans).save()
				else:
					print "gole4"
					s=mobile_details(user=user, mobile_number=number,file_count=500,plan=plans).save()

				token = stripe.Token.create(
					card={
					"number": card,
					"exp_month": month,
					"exp_year": year,
					"cvc": cvc
					},
					)
				print token.id
				customer = stripe.Customer.create(email=mail,description="Example charge",source=token.id,plan=plans
												 
				)

				print customer
				print customer.id
				print customer.subscriptions.data
				print type(customer.subscriptions.data)
				data_list=customer.subscriptions.data
				for i in data_list:
					plan_name=i.plan.id
					sub_id=i.id
				print "subscriptions"
				print sub_id
				print "EEEEEEEEEEEEEEEEE"
				# plan = stripe.Plan.retrieve(plans)
				# plan_name = plan.currency
				# amount=plan.amount
				# print"!!!!!!!!!!!!##"
				# print amount
				print plan_name
				customer_details=plan_details(user=user,customer_id=customer.id,subscription_id=sub_id,plan=plan_name).save()
				# messages.info(request, (u"You have reached maximum uploading images limit for this product ..."))
				admin_email="satyatulasi518@gmail.com"
				print admin_email
				print mail
				# send_mail('Email verification for Online File Uploading', ' Dear %s,\n\nThank you for registered with Online File Uploading.\n You selected %s plan.\n Thanks for using our site. \n\n\nSincerely, \n Online File Uploading.com'%(name,plan_name),
				#  admin_email,[mail],fail_silently=False)

				requests.post(
		"https://api.mailgun.net/v3/sandbox8169e89897ab472bae3c2b510d933f00.mailgun.org/messages",
		auth=("api", "key-696fb9278223dd4019661081a7b60513"),
		data={"from": "Excited User <mailgun@sandbox8169e89897ab472bae3c2b510d933f00.mailgun.org>",
			  "to": mail,
			  "subject": "Email verification for Online File Uploading",
			  "text": "Dear %s,\n\nThank you for registered with Online File Uploading.\n You selected %s plan.\n Thanks for using our site. \n\n\nSincerely, \n Online File Uploading.com"%(name,plan_name)})
	# print "************"



				# requests.post(
				# "www.onlinefileuploading.com",
				# auth=("api", "key-1e03fe95d640730376053e8bba12302b"),
				# data={"from": "Mailgun Sandbox <postmaster@sandbox24c9814cb27e4f0d9b2c869b557f28ec.mailgun.org>",
				# 	  "to": 'roopa108@yopmail.com',
				# 	  "subject":'Email verification for Online File Uploading',
				# 	  "text": ' Dear %s,\n\nThank you for registered with Online File Uploading.\n You selected %s plan.\n Thanks for using our site. \n\n\nSincerely, \n Online File Uploading.com'%(name,plan_name)})
				# print "mailgun"





				# send_mail('Email verification for Online File Uploading', 'Dear %s,\n\nThank you for registered with Online File Uploading.\n Thanks for using our site. \n\n\n,Sincerely\n Online File Uploading.com'%(name),[admin_email],mail)	
	# send_mail('Email verification for Online File Uploading', 'Dear %s,\n\nThank you for registered with Online File Uploading.\n Thanks for using our site. \n\n\n,Sincerely\n Online File Uploading.com'%(name),admin_email,[mail],fail_silently=False)	

				
				if(plan_name=="PREMIUM"):
					admin_email="satyatulasi518@gmail.com"
					print "property"
					# send_mail(' New PREMIUM plan registered', 'Dear admin,\n\nNew PREMIUM plan registered.\n User and Emails: %s and %s. \n\n\n,Sincerely\n Online File Uploading.com'%(name,mail),admin_email,[admin_email],fail_silently=False)	
					requests.post(
					"https://api.mailgun.net/v3/sandbox8169e89897ab472bae3c2b510d933f00.mailgun.org/messages",
					auth=("api", "key-696fb9278223dd4019661081a7b60513"),
					data={"from": "Excited User <mailgun@sandbox8169e89897ab472bae3c2b510d933f00.mailgun.org>",
						  "to": admin_email,
						  "subject": "New PREMIUM plan registered",
						  "text": "Dear admin,\n\nNew PREMIUM plan registered.\n User and Emails: %s and %s. \n\n\n,Sincerely\n Online File Uploading.com"%(name,mail)})


# send_mail('Email verification for Online File Uploading', ' Dear %s,\n\nThank you for registered with Online File Uploading.\n You selected %s plan.\n Thanks for using our site. \n\n\nSincerely, \n Online File Uploading.com'%(name,plan_name),
# 				 admin_email,[mail],fail_silently=False)

					# send_mail('PREMIUM plan registered', 'A New user is registered with PREMIUM plan',"satyatulasi518@gmail.com")
#



				return render(request, 'payments/signup_success.html')
			except stripe.error.InvalidRequestError, e:
				print "invalid request error"
				messages.info(request, (u"You have entered invalid request ... !"))             
				pass
			except stripe.error.AuthenticationError, e:
				print "AuthenticationError"
				messages.info(request, (u"Your authentications failed due to stripe keys...!"))             
				pass
			except stripe.error.APIConnectionError, e:
				print "api connection error"
				messages.info(request, (u"Api connection error , re enter the details...!"))             
				pass
			except stripe.error.StripeError, e:
				print "stripe error"
				messages.info(request, (u"Some stripe traffic error , please provide the details again ...!"))            
				pass
			except IntegrityError:
				print "integrity error"                                              
				messages.info(request, (u"This User has already existed...!"))                
			# except Exception, e:
			# 	print "global exception"
			# 	messages.info(request, (u"Please provide correct details... !"))           
			# 	pass            

			# 	# return HttpResponseServerError(t.render(Context({
	# 'exception_value': "value",
# })))
				# messages.info(request, (u"user already exists ..."))

				# pass
				# except IntegrityError as e:
			# 	return render_to_response( {"message": e.message})
			# messages.info(request, 'success.')
			# return redirect('/login/')
		# else:
		#     return HttpResponse("error.")

	else:
		form=signUp()
	return render(request,'payments/signup.html',{"form":form})

def success(request):
	return render(request, 'payments/signup_success.html')


# $(document).ready(function(){
#             $("#user_form").validate({

#             rules:{% validation_rules  form %} ,
#             messages: {% validation_messages form %} ,

#             });
#             });









def login(request):
	print "K"
	if request.method == 'POST':
		print "post"
		form = Login(request.POST)
			# print form
		username = request.POST['name']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		print user
		print username
		if form.is_valid():
			print "form valied"
			# 			print "form valied"
			if user:
				print "valied"
				auth_login(request, user)
				
				if user.is_active:
					print "((((((((((("
					print user
					print request.user.id
					print "is_active"
					import random
					# print "randrange(1000, 10000, 4) : ", random.randrange(1000, 10000, 4)
					import string
					def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
						return ''.join(random.choice(chars) for _ in range(size))
					# print "#######"
					# print id_generator()
					number=User.objects.filter(username=username)
					print "@@@@@@@@@@@"
					for i in number:
						print i.id
						ph=mobile_details.objects.filter(user_id=i.id)
						for n in ph:
							d=[]
							print"$$$$$$$$$$$$"
							s="+91",n.mobile_number
							
							ph_num=s[0]+str(s[1])
							print ph_num
							account_sid ="AC482cdce0dbe53618d5f9c46d58827d85"
							auth_token = "6f908a39a70f71cf70b287bd3f3fa8c8"
							client = TwilioRestClient(account_sid, auth_token)
							message = client.messages.create(to=ph_num, from_="+1 415-599-2671",body=id_generator())
							otp_pwd=message.body
							print otp_pwd
							d1=i.id
							print "DDDDDDDDDD"
							print d1
							login_id=[]
							login_id.append(d1)
							print login_id[0]
							otp=otp_details(otp_id=d1,otp_password=otp_pwd).save()
							# return HttpResponse("success.")
							return redirect('/verification/%s'%d1)
							# return render(request, 'payments/login.html',{"login_id":login_id})
			else:
				messages.info(request, 'Name and Passwords did not match.')

	else:
		form = Login()

	return render_to_response('payments/login.html',RequestContext(request, {"form":form}))



def verification(request,text):
	print request.user.username
	print "$$$$$$$$$$$$$$"
	print "%&(@_(%F"
	print request.user
	print "ok"
	print text
	id=text

	if request.method == 'POST':
		print "posttttttttt"
		form = OTP(request.POST)
		if form.is_valid():
			print "jkjk"
		# print form
			otp_msg = request.POST['otp']
			print otp_msg
			otp=otp_details.objects.filter(otp_password=otp_msg)
			if otp:
				for j in otp:
					print "forloop"
					print j
					print j.otp_password
					if(j.otp_password==otp_msg):
						# if form.is_valid():
						print "valid"
						otp=otp_details.objects.filter(otp_password=otp_msg).delete()
						print otp
						# return HttpResponse("success.")
						# return render(request, 'payments/profile.html')
						return redirect('/uploading/%s'%id)
			else:
				messages.info(request, 'OTP is not valid.')
					# messages.info(request, 'Invalied OTP')

	else:
		form=OTP()
	return render(request,'payments/OTP.html',{"form":form})
	
	
# def uploading(request):
# 	return render(request, 'payments/profile.html')
# def handle_uploaded_file(f):
#     with open('some/file/name.txt', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


# from somewhere import handle_uploaded_file
# @login_required()
# @myuser_login_required
def uploading(request,text):
	print request.user.id
	print text
	# contextDict = {}
	id=text
	details=[]
	user_profile=User.objects.filter(id=text)
	for data in user_profile:
		details.append(data.username)
		details.append(data.email)
	print details
	num_details=mobile_details.objects.filter(user_id=text)
	for num in num_details:
		details.append(num.mobile_number)
		print "CCCCCCCCCCCCCC"
		print num.file_count
		print "CCCCCCCCCCCCCC"
	print details[0]
	print details[1]
	print details[2]
	
		# d=data.append(i.id)
		# print "WWWWWWW",d
		# print i.user_id

	# 	contextDict['id'] = i.id
	# 	print contextDict
	# medicine_object.save()


	for i in num_details:
		plan_count=i.file_count
		print "*********"
		print "*********"
	count=file_details.objects.filter(user_id=text).count()
	details.append(count)
	print details[3]
	list_files=[]
	file_list=file_details.objects.filter(user_id=text)
	for i in file_list:
		list_files.append(i.file_name)
	
	total_details=details.append(list_files)
	print "$$$$$$$"
	# print details[4]
	for i in details[4]:
		print i
	details_plan=plan_details.objects.filter(user_id=text)
	
	print "^^^^^^^^^^"
	for plan in details_plan:
		details.append(plan.plan)
	print "^^^^^^^^^^"
	print details[5]
	details.append(plan_count)
	print details[6]
	if request.method == 'POST':
		print"hai"
		try:
			data_file=request.FILES['file']
			file=data_file.name
			print file
			# f = open(data_file, 'r')
			# print f.read()
			# f.close()
			# import fileinput

			# for line in fileinput.input(['file']):
	# 			  print  line
			if(count<plan_count):
				print "not exeed"
				print plan_count

				form = UploadFile(request.POST, request.FILES)
				
				# import os
				fileName, fileExtension = os.path.splitext(file)

				if (fileExtension==".json") or (fileExtension==".csv"):
				#     print 'This file is flac file %s' %files
					print "format supported"
				
					if form.is_valid():
						print '****request*************'
						print request.POST
						print '*********'
						# handle_uploaded_file(request.FILES['file'])
						data_file=request.FILES['file']
						content=request.FILES['file'].read()
						print content
						title=request.POST.get("title")
						print title
						print "{{{{{{{{{{{{"
						print data_file
						user=otp_details.objects.filter()
						data=file_details(title=title,file_name=data_file,user_id=text,file_content=content).save()
						plan.name = title
						print"TTTTTTTTTTTTTT"
						print details[5]
						print plan.name
						plan.save()
						# import fileinput

						# for line in fileinput.input(['demo_csv.csv.csv']):
						# 	print line
						# medicine_object.save()
						# Profile.objects.all().count()
						# print data.file_name
						# return redirect('/upgrade/%s'%id)
						# return HttpResponse("success")
						return render(request,'payments/upload_success.html')
				else:
					messages.info(request,"Upload only csv and json files")
			else:
				messages.info(request, (u"You have reached maximum uploading files limit for your plan .upgrade your plan for uploading more files ..."))
		except:
			messages.info(request,"No file selected")

	else:
		form = UploadFile()
	# return render_to_response('payments/profile.html',RequestContext(request, {"form":form},{'name':name}))
	return render(request,'payments/profile.html',{"details":details})


def upgrade(request,text):
	print "K"
	can_uploaded_count=file_details.objects.filter(user_id=request.user.id).count()
	print can_uploaded_count
	uploaded_count=mobile_details.objects.filter(user_id=request.user.id)
	for c in uploaded_count:
		print "{{{{{{{{{{{{"
		print c.file_count
		# if(can_uploaded_count==c.file_count):
		current_details=[]
		current_details.append(request.user.username)
		current_details.append(request.user.email)
		current_plan=plan_details.objects.filter(user_id=request.user.id)
		for info in current_plan:
			current_details.append(info.plan)
			print info.plan
		greater_plane=stripe_plan_details.objects.filter(plan=info.plan)
		for g in greater_plane:
			print "884545787"
			print g.file_count
		available_plans=[]
		greater=stripe_plan_details.objects.filter(file_count__gt=g.file_count)
		for i in greater:
			available_plans.append(i.plan)

		print available_plans
			
		current_num=mobile_details.objects.filter(user_id=request.user.id)
		for num in current_num:
			print ")PPPPPPPPPPPPPPPPP"
			print num.plan
			current_details.append(num.mobile_number)
		current_details.append(available_plans)
		print current_details
		print "TTTTTTTAGAG"
		for i in current_details:
			print i
			# for num in current_num:
			# 	current_details.append(num.mobile_number)
			# 	print "{}%GHD&^"
			# 	available_count=num.file_count
			# 	current_details.append(available_count)
			
			# greater=stripe_plan_details.objects.filter(file_count__gt=available_count)
			# remaining_plans=[]
			# for g in greater:
			# 	print "TTTTTTTAGAG"
			# 	print g.plan
			# 	remaining_plans.append(g.plan)
			# current_details.append(remaining_plans)
		print current_details
		if request.method == 'POST':
			print "post"
			form = Upgrade(request.POST)
			if form.is_valid():
				print "ok"
				print form
				try:
					plans = request.POST.get('plan')
					print plans
					upgrade_details=plan_details.objects.filter(user_id=request.user.id)
					for info in upgrade_details:
						print info.customer_id
						print info.subscription_id
					customer = stripe.Customer.retrieve(info.customer_id)
					subscription = customer.subscriptions.retrieve(info.subscription_id)
					subscription.plan = plans
					subscription.save()
					update_plan_details=plan_details.objects.filter(user_id=request.user.id).update(plan=plans)
					stripe_plan_count=stripe_plan_details.objects.filter(plan=plans)
					print stripe_plan_count
					for i in stripe_plan_count:
						print i.file_count
						real_count=i.file_count
					count=file_details.objects.filter(user_id=request.user.id).count()
					current_details.append(count)
					remaining_count=real_count-count
					print remaining_count
					for d in  current_details:
						print d
					print "___________________"
					print num.plan
					# print info.plans
					admin_email="satyatulasi518@gmail.com"
					print plans
					print request.user.email
					update_mobile_details=mobile_details.objects.filter(user_id=request.user.id).update(plan=plans,file_count=real_count)
					# send_mail('Email verification for Upgrading plan', ' Dear %s,\n\nYou have successfully Upgraded your plan from %s to %s.\n Thanks for upgrading plan. \n\n\nSincerely, \n Online File Uploading.com'%(request.user.username,num.plan,plans),
					# 	   admin_email,[request.user.email], fail_silently=False)
					# print "WWWWWWWWWWWW"
					
					requests.post(
					"https://api.mailgun.net/v3/sandbox8169e89897ab472bae3c2b510d933f00.mailgun.org/messages",
					auth=("api", "key-696fb9278223dd4019661081a7b60513"),
					data={"from": "Excited User <mailgun@sandbox8169e89897ab472bae3c2b510d933f00.mailgun.org>",
						  "to": request.user.email,
						  "subject": "Email verification for Upgrading plan",
						  "text": "Dear %s,\n\nYou have successfully Upgraded your plan from %s to %s.\n Thanks for upgrading plan. \n\n\nSincerely, \n Online File Uploading.com"%(request.user.username,num.plan,plans)})


					print plans
					if(plans=="PREMIUM"):
						admin_email="satyatulasi518@gmail.com"
						print "property"
						# send_mail(' Upgraded to PREMIUM plan', 'Dear admin,\n\nUser has upgraded from %s to PREMIUM.\n User and Emails: %s and %s. \n\n\n,Sincerely\n Online File Uploading.com'%(num.plan,request.user.username,request.user.email),request.user.email,[admin_email])	
						requests.post(
					"https://api.mailgun.net/v3/sandbox8169e89897ab472bae3c2b510d933f00.mailgun.org/messages",
					auth=("api", "key-696fb9278223dd4019661081a7b60513"),
					data={"from": "Excited User <mailgun@sandbox8169e89897ab472bae3c2b510d933f00.mailgun.org>",
						  "to": admin_email,
						  "subject": "Upgraded to PREMIUM plan",
						  "text": "Dear admin,\n\nUser has upgraded from %s to PREMIUM.\n User and Emails: %s and %s. \n\n\n,Sincerely\n Online File Uploading.com"})






						# requests.post(
			   #      "https://api.mailgun.net/v3/sandbox8169e89897ab472bae3c2b510d933f00.mailgun.org/messages",
			   #      auth=("api", "key-696fb9278223dd4019661081a7b60513"),
			   #      data={"from": "Excited User <mailgun@sandbox8169e89897ab472bae3c2b510d933f00.mailgun.org>",
			   #            "to": admin_email,
			   #            "subject": "Upgraded to PREMIUM plan",
			   #            "text": "Dear admin,\n\nUser has upgraded from %s to PREMIUM.\n User and Emails: %s and %s. \n\n\n,Sincerely\n Online File Uploading.com"%(num.plan,request.user.username,request.user.email)})


					# send_mail(' New PREMIUM plan registered', 'Dear admin,\n\nNew PREMIUM plan registered.\n User and Emails: %s and %s. \n\n\n,Sincerely\n Online File Uploading.com'%(name,mail),admin_email,[admin_email],fail_silently=False)	

						# file_count_details=mobile_details.objects.filter(user_id=request.user.id)
						# for i in file_count_details:
						# 	file_count_no=i.file_count
						# 	print file_count_no
						# plan_file_count=stripe_plan_details.objects.filter(plan="GOLD")
						# for j in plan_file_count:
						# 	print j.file_count
						# update_count=j.file_count-file_count_no
						# print update_count
						# stirpe_file_count=mobile_details.objects.filter(user_id=request.user.id).update(file_count=update_count)
						# return render(request,'payments/upgrade_success.html')
				except:
					messages.info(request,"you dont have any plan to upgrade")

				# if form.is_valid():
				# 	print "ok"
				# 	return HttpResponse("success.")
				# else:
				# 	return HttpResponse("error.")
		else:
			form=Upgrade()
		return render(request,'payments/upgrade.html',{"current_details":current_details})
		# else:
		# 	return render(request,'payments/upgrade1.html')


# def facebook(request):
# 	driver.get("https://www.facebook.com/swamyven")  
# 	profile= [element for element in driver.find_elements_by_css_selector('div#fbProfileCover')]
# 	for i in profile:                                                                        
# 	    print i.find_element_by_css_selector('div#u_0_3.cover div._6-e h2._6-f a._8_2 span#fb-timeline-cover-name').text
# 	    print i.find_element_by_css_selector('div#u_0_3.cover a#fbCoverImageContainer.coverWrap.coverImage img.coverPhotoImg.photo.img').get_attribute("src")
# 		print i.find_element_by_css_selector('div#fbTimelineHeadline.clearfix div.name div.photoContainer div div.profilePicThumb img.profilePic.img').get_attribute("src")
# 	info= [element for element in driver.find_elements_by_css_selector('div#contentArea div#pagelet_timeline_main_column._5h60 div.timelineLoggedOutPagelet div.clearfix div.timelineLoggedOutMain.lfloat._ohe')]


 
# 	for i in info:                   
# 	 	print i.find_element_by_css_selector('div#pagelet_all_favorites._5h60.allFavorites div.fbTimelineSection.mtm.timelineFavorites.fbTimelineCompactSection div#favorites.profileInfoSection div.phs table.mtm._5e7-.profileInfoTable._3stp._3stn tbody tr th.label div.labelContainer').text   
# 	 	print i.find_element_by_css_selector('div#pagelet_all_favorites._5h60.allFavorites div.fbTimelineSection.mtm.timelineFavorites.fbTimelineCompactSection div#favorites.profileInfoSection div.phs table.mtm._5e7-.profileInfoTable._3stp._3stn tbody tr td.data div.mediaRowWrapper ul.uiList.pbl.mediaRow._509-._4ki._6-h._704._6-i li div.mediaPortrait div.profilePicContainer img.photo.img').get_attribute("src")
# 	    print i.find_element_by_css_selector('div#pagelet_all_favorites._5h60.allFavorites div.fbTimelineSection.mtm.timelineFavorites.fbTimelineCompactSection div#favorites.profileInfoSection div.phs table.mtm._5e7-.profileInfoTable._3stp._3stn tbody tr td.data div.mediaRowWrapper ul.uiList.pbl.mediaRow._509-._4ki._6-h._704._6-i li div.mediaPortrait a.mediaRowItem div.mediaPageName').text

# html.os-linux body#pagekey-uas-consumer-login-internal.member.v2.chrome-v5.chrome-v5-responsive.sticky-bg.js div#body div.wrapper.hp-nus-wrapper div#main.signin form#login.ajax-form.stacked-form fieldset div#control_gen_3.outer-wrapper div.inner-wrapper ul#mini-profile--js li.form-email div.fieldgroup.hide-label input#session_key-login


# def link(request):

# 	driver = webdriver.Firefox()
# 	driver.get("https://www.linkedin.com/uas/login?goback=&trk=hb_signin")
# 	elem = driver.find_element_by_css_selector("input#session_key-login")
# 	print "ha"
# 	elem.send_keys("satyatulasi518@gmail.com")
# 	elem1 = driver.find_element_by_name("session_password")
# 	elem1.send_keys("satya3112")
# 	elem2 = driver.find_element_by_name("signin")
# 	elem2.click()
# 	# time.sleep(5)
# 	elem3 = driver.find_element_by_id("main-search-box")
# 	elem3.send_keys("sri")
# 	elem3.click()
# 	elem4 = driver.find_element_by_name("search")
# 	elem4.click()
# 	d=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# 	for j in d:
# 		print j
# 		car= [element for element in driver.find_elements_by_css_selector('div#results-col.col div#results-container ol#results.search-results li.mod.result.idx%s.people'%j)]
# 		for i in car:
# 			try:
# 				print i.find_element_by_css_selector('div.bd h3 a.title.main-headline').get_attribute("href")
# 		   		print i.find_element_by_css_selector('div.bd h3 a.title.main-headline b').text
# 				print i.find_element_by_css_selector('div.bd div.description').text
# 				print i.find_element_by_css_selector('div.bd dl.demographic dd.separator bdi').text
# 				print i.find_element_by_css_selector('div.bd dl.demographic dd').text
# 			except:
# 				print"DD"
# 				pass
# 			# print i.find_element_by_css_selector('div.bd dl.demographic dd').text

# 	return HttpResponse("success")

# # html.os-linux body#pagekey-voltron_federated_search_internal_jsp.member.v2.voltron-page.chrome-v5.chrome-v5-responsive.sticky-bg.js div#body div.wrapper.hp-nus-wrapper div#srp_main_ div#srp_container.srp-type-people.show-survey div#results-col.col div#results-container ol#results.search-results li.mod.result.idx7.people div.bd dl.demographic dd

# # for i in car: 
# #     print i.find_element_by_css_selector('div.bd h3 a.title.main-headline').get_attribute("href")
# #    ....:     print i.find_element_by_css_selector('div.bd h3 a.title.main-headline').get_attribute("href")
# #    ....:     print i.find_element_by_css_selector('div.bd h3 a.title.main-headline b').text
# #    ....:     print i.find_element_by_css_selector('div.bd div.description').text
# #    ....:     print i.find_element_by_css_selector('div.bd dl.demographic dd.separator bdi').text
# #    ....:     print i.find_element_by_css_selector('div.bd dl.demographic dd').text
# #    ....:     print i.find_element_by_css_selector('div.bd dl.demographic dd').text


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def link(request):
	if request.method == 'POST':
		print "posttttttttt"
		form = linkedin_search(request.POST)
		if form.is_valid():
			information=[]
			name=request.POST.get("link_search")
			print name
			display = Display(visible=0, size=(800, 600))
			display.start()
			driver = webdriver.Firefox()
			driver.get("https://www.linkedin.com/uas/login?goback=&trk=hb_signin")
			elem = driver.find_element_by_css_selector("input#session_key-login")
			print "ha"
			elem.send_keys("satyatulasi518@gmail.com")
			elem1 = driver.find_element_by_name("session_password")
			elem1.send_keys("satya3112")
			print elem1
			elem2 = driver.find_element_by_name("signin")
			elem2.click()
			print elem2
			# time.sleep(5)
			elem3 = driver.find_element_by_id("main-search-box")
			elem3.send_keys(name)
			print elem3
			elem4 = driver.find_element_by_name("search")
			elem4.click()
			print elem4
			count=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
			for c in count:
				print c
				user_data=[]
				car= [element for element in driver.find_elements_by_css_selector('div#results-col.col div#results-container ol#results.search-results li.mod.result.idx%s.people'%c)]
				for i in car:
					try:
						user_data.append(i.find_element_by_css_selector('div.bd h3 a.title.main-headline').get_attribute("href"))
						user_data.append(i.find_element_by_css_selector('div.bd h3 a.title.main-headline').text)
						user_data.append(i.find_element_by_css_selector('div.bd div.description').text)
						user_data.append(i.find_element_by_css_selector('div.bd dl.demographic dd.separator bdi').text)
						# print i.find_element_by_css_selector('div.bd dl.demographic dd').text
						information.append(user_data)
						# print i.find_element_by_css_selector('div.bd h3 a.title.main-headline').text


					except:
						pass
			display.stop()
			return render(request,'payments/link_info.html',{"information":information})


	else:
		form=linkedin_search()
	# return render(request,'payments/insta.html',{"form":form})
	return render(request,'payments/link.html',{"form":form})



# from pyvirtualdisplay import Display
# from selenium import webdriver
# def facebook(request):
# 	if request.method == 'POST':
# 		print "posttttttttt"
# 		form = facebook_search(request.POST)
# 		if form.is_valid():
# 			information=[]
# 			profile_info=[]
# 			favorites=[]
# 			name=request.POST.get("fb_search")
# 			print name
# 			# display = Display(visible=0, size=(800, 600))
# 			# display.start()
# 			driver = webdriver.Firefox()
# 			driver.get("https://www.facebook.com/%s"%name)
# 			try:
# 				profile= [element for element in driver.find_elements_by_css_selector('div#fbProfileCover')]
# 				print "hai"
# 				for i in profile:                                                                        
# 					# print i.find_element_by_css_selector('div#u_0_3.cover div._6-e h2._6-f a._8_2 span#fb-timeline-cover-name').text
# 					# print i.find_element_by_css_selector('div#u_0_3.cover a#fbCoverImageContainer.coverWrap.coverImage img.coverPhotoImg.photo.img').get_attribute("src")
# 					# print i.find_element_by_css_selector('div#fbTimelineHeadline.clearfix div.name div.photoContainer div div.profilePicThumb img.profilePic.img').get_attribute("src")
# 					profile_info.append(i.find_element_by_css_selector('div#u_0_3.cover div._6-e h2._6-f a._8_2 span#fb-timeline-cover-name').text)
# 					print "cover"
# 					profile_info.append(i.find_element_by_css_selector('div#u_0_3.cover a#fbCoverImageContainer.coverWrap.coverImage img.coverPhotoImg.photo.img').get_attribute("src"))
# 					print "profile"
# 					profile_info.append(i.find_element_by_css_selector('div#fbTimelineHeadline.clearfix div.name div.photoContainer div div.profilePicThumb img.profilePic.img').get_attribute("src"))
# 					print "name"
# 					print profile_info
# 					information.append(profile_info)
# 					print "#######################"
# 					print information
# 				info= [element for element in driver.find_elements_by_css_selector('div#contentArea div#pagelet_timeline_main_column._5h60 div.timelineLoggedOutPagelet div.clearfix div.timelineLoggedOutMain.lfloat._ohe')]
# 				for i in info:                   
# 					favorites.append(i.find_element_by_css_selector('div#pagelet_all_favorites._5h60.allFavorites div.fbTimelineSection.mtm.timelineFavorites.fbTimelineCompactSection div#favorites.profileInfoSection div.phs table.mtm._5e7-.profileInfoTable._3stp._3stn tbody tr th.label div.labelContainer').text) 
# 					favorites.append(i.find_element_by_css_selector('div#pagelet_all_favorites._5h60.allFavorites div.fbTimelineSection.mtm.timelineFavorites.fbTimelineCompactSection div#favorites.profileInfoSection div.phs table.mtm._5e7-.profileInfoTable._3stp._3stn tbody tr td.data div.mediaRowWrapper ul.uiList.pbl.mediaRow._509-._4ki._6-h._704._6-i li div.mediaPortrait div.profilePicContainer img.photo.img').get_attribute("src"))
# 					favorites.append(i.find_element_by_css_selector('div#pagelet_all_favorites._5h60.allFavorites div.fbTimelineSection.mtm.timelineFavorites.fbTimelineCompactSection div#favorites.profileInfoSection div.phs table.mtm._5e7-.profileInfoTable._3stp._3stn tbody tr td.data div.mediaRowWrapper ul.uiList.pbl.mediaRow._509-._4ki._6-h._704._6-i li div.mediaPortrait a.mediaRowItem div.mediaPageName').text)
# 					information.append(favorites)
# 					print information
# 				# info= [element for element in driver.find_elements_by_css_selector('div#contentArea div#pagelet_timeline_main_column._5h60 div.timelineLoggedOutPagelet div.clearfix div.timelineLoggedOutMain.lfloat._ohe')]
# 				# for i in info:
# 				# 	information.append(i.find_element_by_css_selector('div#pagelet_all_favorites._5h60.allFavorites div.fbTimelineSection.mtm.timelineFavorites.fbTimelineCompactSection div#favorites.profileInfoSection div.uiHeader.fbTimelineAboutMeHeader div.clearfix.uiHeaderTop div h4.uiHeaderTitle').text)
# 				# # 	information.append(i.find_element_by_css_selector('div#pagelet_all_favorites._5h60.allFavorites div.fbTimelineSection.mtm.timelineFavorites.fbTimelineCompactSection div#favorites.profileInfoSection div.phs').text)
# 				# for j in information[0]:
# 				# 	print "**********"
# 				# 	# print j[0]
# 				# 	print j
# 				# 	# print j.name
# 				# 	# print "$$$$$$$$$$"
# 				# print type(information)
# 				# print information[1]
# 				# print information[2]
# 			except:
# 				pass
# 			return render(request,'payments/fb_info.html',{"information":information})


# 	else:
# 		form=facebook_search()
# 	return render(request,'payments/fb.html',{"form":form})
# 	# return HttpResponse("error.")



# In [22]: for i in  info:
   










from instagram.client import InstagramAPI
# 
import blockspring
import json
def instagram(request):
	accessToken ="2318107752.5b9e1e6.e6e250fcfbc34b0086de1c9f55de8eee"
	api = InstagramAPI(access_token=accessToken)
	if request.method == 'POST':
		print "posttttttttt"
		form = searching(request.POST)
		if form.is_valid():
			print "jkjk"
			name=request.POST.get("search")
			print name
			print form
			user_info=api.user_search(q=name)
			information=[]
			for i in user_info:
				print i.username
				user_data=[]
				try:

					info=blockspring.runParsed("get-instagram-user-info", {"user":i.username, "using_id": False }, {"api_key":"br_19033_6f02bdb020848e67749ac0e4087da7eac9cb0e99"}).params
					user_data.append(info['username'])
					user_data.append(info['id'])
					user_data.append(info['profile_picture'])
					user_data.append(info['full_name'])
					information.append(user_data)

				except:
					print "Exception"
					pass
			return render(request,'payments/info.html',{"information":information})

	else:
		form=searching()
	return render(request,'payments/insta.html',{"form":form})



	# return render(request,'payments/info.html')








# html#facebook.tinyViewport.tinyHeight body.timelineLayoutLoggedOutUserProfile.timelineLayoutLoggedOut._4lh.timelineLayout.fbx.UIPage_LoggedOut._2gsg._xw8._5p3y.gecko.x1.Locale_en_GB div._li div#globalContainer.uiContextualLayerParent div#content.fb_content.clearfix div div#mainContainer div#contentCol.clearfix.hasRightCol div#contentArea div#pagelet_timeline_main_column._5h60 div.timelineLoggedOutPagelet div.clearfix div.timelineLoggedOutMain.lfloat._ohe 
# div#pagelet_all_favorites._5h60.allFavorites div.fbTimelineSection.mtm.timelineFavorites.fbTimelineCompactSection div#favorites.profileInfoSection div.uiHeader.fbTimelineAboutMeHeader div.clearfix.uiHeaderTop div h4.uiHeaderTitle

# find_element_by_css_selector('div#pagelet_all_favorites._5h60.allFavorites div.fbTimelineSection.mtm.timelineFavorites.fbTimelineCompactSection div#favorites.profileInfoSection div.uiHeader.fbTimelineAboutMeHeader div.clearfix.uiHeaderTop div h4.uiHeaderTitle')








# def instagram(request):

# 	accessToken ="2318107752.5b9e1e6.e6e250fcfbc34b0086de1c9f55de8eee"
# 	api = InstagramAPI(access_token=accessToken)
# 	if request.method == 'POST':
# 		print "posttttttttt"
# 		form = searching(request.POST)
# 		if form.is_valid():
# 			print "jkjk"
# 			name=request.POST.get("search")
# 			print name
# 			print form
# 			user_info=api.user_search(q=name)
# 			information=[]
# 			print user_info
# 			print "PPPPPPPPPPPPPPPPPPP"
# 			# print user_info[0].username
# 			# print user_info[1].username
# 			# print user_info[10].username

# 			# try:
# 			# information=[]
			
# 			for i in user_info:
# 				user_data=[]
# 				# print "********"
# 				# print "KKKKKKKK"
				
# 				print i.username
				
# 				try:
					
# 					info=blockspring.runParsed("get-instagram-user-info", {"user":i.username, "using_id": False }, {"api_key":"br_19033_6f02bdb020848e67749ac0e4087da7eac9cb0e99"}).params
# 					# print info
# 					print info['username']
# 					print info['id']
# 					print info['profile_picture']
# 					print info['full_name']
# 					print type(user_info)

# 					user_data.append(info['username'])
# 					user_data.append(info['id'])
# 					user_data.append(info['profile_picture'])
# 					user_data.append(info['full_name'])
# 					# infomation.append(user_data)
# 					# print user_data
# 					# information.append(info['username'])
# 					# information.append(info['id'])
# 					# information.append(info['profile_picture'])
# 					# information.append(info['full_name'])
# 					# print information
# 					information.append(user_data)
# 					# return HttpResponse("error.")
# 				except:
# 					pass
# 				# return render(request,'payments/info.html',{"information":information})
# 			print information
# 	return render(request,'payments/info.html',{"information":information})
# # 

# 			# for i in xrange(20):
# 			# 	print "********"
# 			# 	print "JJJJJJJJJJJJJJJJ"
# 			# 	print user_info[i]


# # >>> for i in xrange(20):
# # ...   print user_info[i].username


# 				# info=blockspring.runParsed("get-instagram-user-info", {"user":i.username, "using_id": False }, {"api_key":"br_19033_6f02bdb020848e67749ac0e4087da7eac9cb0e99"}).params
# 				# print info
# 					# for key,value in info.iteritems():
# 					# 	print value

# 					# print info['username']
# 					# information.append(info['username'])
# 					# information.append(info['id'])
# 					# information.append(info['profile_picture'])
# 					# information.append(info['full_name'])
# 					# # for j in info:
# 					# # 	print j
# 					# # print info['username']
# 					# print information
# 				# print "https://www.instagram.com/%s"%(i.username)
# 				# return render(request,'payments/info.html',{"information":information})

# 		# 	except:
# 		# 		pass

# 		# print information


# 			# else:
# 			# 	messages.info(request, 'OTP is not valid.')
# 					# messages.info(request, 'Invalied OTP')

# 	else:
# 		form=searching()
# 	return render(request,'payments/insta.html',{"form":form})
# 	# return render(request,'payments/upgrade.html',{"current_details":current_details})




# accessToken ="2318107752.5b9e1e6.e6e250fcfbc34b0086de1c9f55de8eee"
# 	api = InstagramAPI(access_token=accessToken)
# 	d=api.user_search(q="a", count=100)

# d=api.user_search(q="a", count=100)
	# for i in d:
	# 	print i.username
	# 	info=blockspring.runParsed("get-instagram-user-info", {"user":i.username, "using_id": False }, {"api_key":"br_19033_6f02bdb020848e67749ac0e4087da7eac9cb0e99"}).params
	# 	# print info['username']
	# 	print info['id']
	# 	print info['profile_picture']
	# 	print info['full_name']
	# 	print "https://www.instagram.com/%s"%(i.username)



# application.search_company(selectors=[{'companies':
#              ['industries','locations']}],
#               params={'count':100,'universal-name':'linkedin',
#               'facet':'company-size,H,industry,43'})



# def upgrade(request,text):
# 	print "upgrade"
# 	if request.method == 'POST':
# 		print "ok"
# 		form = upgrade(request.POST)
# 		print "success"
		# return HttpResponse("error.")
	# current_details=[]
	# current_details.append(request.user.username)
	# current_details.append(request.user.email)
	# current_plan=plan_details.objects.filter(user_id=request.user.id)
	# for info in current_plan:
	# 	current_details.append(info.plan)
	# current_num=mobile_details.objects.filter(user_id=request.user.id)

	# for num in current_num:
	# 	current_details.append(num.mobile_number)
	# 	print "{}%GHD&^"
	# 	available_count=num.file_count
	# print current_details
	# greater=stripe_plan_details.objects.filter(file_count__gt=available_count)
	# remaining_plans=[]
	# for g in greater:
	# 	remaining_plans.append(g.plan)
	# current_details.append(remaining_plans)
	# print text
	# if request.method == 'POST':
	# 	print "ok"
	# 	form = upgrade(request.POST)
	# 	print "success"
	# 	# return HttpResponse("error.")
	# 	return render(request,'payments/upgrade.html',{"current_details":current_details})
	# else:
	# 	form=upgrade()
	# return render(request,'payments/upgrade.html',{"form":form})
	# if request.method == 'POST':
	# 	print "ok"

	# 	form = upgrade(request.POST)
	# 	print form
	# 	if form.is_valid():
	# 		plans=request.POST.get("plan")
	# 		print plan
	# 		return HttpResponse("error.")
			
	




# 	upgrade_details=plan_details.objects.filter(user_id=request.user.id)
# 	for info in upgrade_details:
# 		print info.customer_id
# 		print info.subscription_id
# 	customer = stripe.Customer.retrieve(info.customer_id)
# 	subscription = customer.subscriptions.retrieve(info.subscription_id)
# 	subscription.plan = "GOLD"
# 	subscription.save()
# 	update_plan_details=plan_details.objects.filter(user_id=request.user.id).update(plan="GOLD")
# 	update_mobile_details=mobile_details.objects.filter(user_id=request.user.id).update(plan="GOLD",file_count=20)
# 	file_count_details=mobile_details.objects.filter(user_id=request.user.id)
# 	for i in file_count_details:
# 		file_count_no=i.file_count
# 		print file_count_no
# 	plan_file_count=stripe_plan_details.objects.filter(plan="GOLD")
# 	for j in plan_file_count:
# 		print j.file_count
# 	update_count=j.file_count-file_count_no
# 	print update_count
# 	stirpe_file_count=mobile_details.objects.filter(user_id=request.user.id).update(file_count=update_count)
# # 
	# # return HttpResponse("success")


	# else:
	# # 	form=upgrade()
	# return render(request,'payments/upgrade.html',{"form":form})

# instance = ModelWithFileField(file_field=request.FILES['file'])
#             instance.save()


	# s=mobile_details(user=user, mobile_number=number).save()


	# def my_view(request):
 #    username = None
 #    if request.user.is_authenticated():
 #        username = request.user.username


# def login(request):
# 	print "login"
# 	if request.method == 'POST':
# 		print "post"
# 		form = Login(request.POST)
# 			# print form
# 		username = request.POST['name']
# 		password = request.POST['password']
# 		user = authenticate(username=username, password=password)
# 		print user
# 		# print username

# 		if form.is_valid():
# 			print "form valied"
# 			# 			print "form valied"
# 			if user is not None:
# 			# if user:
# 				print "valied"
# 				print user
				
# 				if user.is_active:
# 					# login(request, user)
# 					return HttpResponse("success.")
# 	else:
# 		form = Login()

# 	return render_to_response('payments/login.html',RequestContext(request, {"form":form}))


# if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect('birthdayreminder.views.main')

#     return render_to_response('login.html',{'username': username}, context_instance=RequestContext(request))









 # print token

			# token = stripe.Token.create(
   #  		card={
   #      		"number": card,
   #      		"exp_month": month,
   #      		"exp_year": year,
   #      		"cvc": cvc
   #  			},
			# 	)
			# print token.id
			# customer = stripe.Customer.create(email=mail,description="Example charge",plan=plans
											 
			# )

			# print customer











# def login(request):
# 	print "K"
# 	if request.method == 'POST':
# 		print "post"
# 		form = Login(request.POST)
# 		# print form
# 		username = request.POST['name']
# 		password = request.POST['password']
# 		user = authenticate(username=username, password=password)
# 		print user
# 		if form.is_valid():
# 			print "form valied"
# 			if user:
# 				print "valied"
				
# 				if user.is_active:
# 					print "((((((((((("
# 					print request.user.id
# 					print "is_active"
# 					import random
# 					# print "randrange(1000, 10000, 4) : ", random.randrange(1000, 10000, 4)
# 					import string
# 					def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
# 						return ''.join(random.choice(chars) for _ in range(size))
# 					# print "#######"
# 					# print id_generator()
# 					number=User.objects.filter(username=username)
# 					print "@@@@@@@@@@@"
# 					for i in number:
# 						print i.id
# 						ph=mobile_details.objects.filter(user_id=i.id)
# 						for n in ph:
# 							d=[]
# 							print"$$$$$$$$$$$$"
# 							s="+91",n.mobile_number
							
# 							ph_num=s[0]+str(s[1])
# 							print ph_num
# 							account_sid ="AC482cdce0dbe53618d5f9c46d58827d85"
# 							auth_token = "6f908a39a70f71cf70b287bd3f3fa8c8"
# 							client = TwilioRestClient(account_sid, auth_token)
# 							message = client.messages.create(to=ph_num, from_="+1 415-599-2671",body=id_generator())
# 							otp_pwd=message.body
# 							print otp_pwd
# 							d1=i.id
# 							print "DDDDDDDDDD"
# 							print d1
# 							otp=otp_details(otp_id=d1,otp_password=otp_pwd).save()
# 							# return HttpResponse("success.")
# 							return redirect('/verification/%s'%d1)
# 				# print id_generator()



# 				# return render(request, 'payments/OTP.html')
# 			else:
				
# 				return HttpResponse("Your Rango account is disabled.")
# 		else:
			
# 			print "Invalid login details: {0}, {1}".format(username, password)
# 			return HttpResponse("error.")
# 	else:
# 		form = Login()
# 		return render_to_response('payments/login.html',RequestContext(request, {"form":form}))


	# return render(request, 'payments/login.html')




# html#facebook.tinyViewport.tinyHeight body.timelineLayoutLoggedOutUserProfile.timelineLayoutLoggedOut._4lh.timelineLayout.fbx.UIPage_LoggedOut._2gsg._xw8._5p3y.gecko.x1.Locale_en_GB div._li div#globalContainer.uiContextualLayerParent div#content.fb_content.clearfix div div#mainContainer div#contentCol.clearfix.hasRightCol div#contentArea div#pagelet_timeline_main_column._5h60 div.timelineLoggedOutPagelet div.clearfix div.timelineLoggedOutMain.lfloat._ohe 
# div#pagelet_all_favorites._5h60.allFavorites div.fbTimelineSection.mtm.timelineFavorites.fbTimelineCompactSection div#favorites.profileInfoSection div.phs




# 	In [13]: for i in  info:
#     print i.find_element_by_css_selector('div#pagelet_all_favorites._5h60.allFavorites div.fbTimelineSection.mtm.timelineFavorites.fbTimelineCompactSection div#favorites.profileInfoSection div.uiHeader.fbTimelineAboutMeHeader div.clearfix.uiHeaderTop div h4.uiHeaderTitle').text
#    ....:     
# Favourites



import blockspring
import json

def facebook(request):
	if request.method == 'POST':
		print "posttttttttt"
		form = facebook_search(request.POST)
		if form.is_valid():
			name=request.POST.get("fb_search")
			print name
			info=blockspring.runParsed("facebook-user-search", { "name":name  }, {"api_key":"br_20271_00bc9ee7d5a054fd925133ec3a29cb36ecdca442"}).params			
			data=[]
			for key,values in info.iteritems():
				data=values
			# print data
			total=[]
			for i in data:
				d=[]
				print "!!!!!!!!!!!!!!!!!!!!!!!!"
				print i['name']
				print i['id']
				d.append(i['name'])
				d.append(i['id'])
				profile=i['name']
				p=profile.replace(" ", "")
				print "!!!!!!!!!!!!!!!!!!!!!!!!"
				print p
				d.append(p)

				total.append(d)

			print "****************"
			# print total
			for j in total:
				print j[0]
				print j[1]
			result="https://graph.facebook.com/10153807668609663/picture?type=large"


			return render(request,'payments/fb_info.html',{"result":result,'total':total})


	else:
		form=facebook_search()
	return render(request,'payments/fb.html',{"form":form})
	# return HttpResponse("error.")



# https://www.facebook.com/satyavanapalli.php?id=152112491823583