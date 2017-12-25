import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function based view
# def home(request):
# 	html_ = """<!DOCTYPE html>
# 	<html lang=en>
# 	<head>
# 	</head>
# 	<body>
# 	<h1>Hello Django</h1>
# 	<p>This is html coming through</p>
# 	</body>
# 	</html>
# 	"""
# 	return HttpResponse(html_)
	
def home(request):
	num = None
	some_list = [random.randint(0,100000000), random.randint(0,100000000), random.randint(0,100000000)]
	condition_bool_item = True
	title = "Django Basics"
	if condition_bool_item:
		num = random.randint(0,100000000)

	context = {
			# "bool_item": True,
			"num": num,
			"django": title,
			"some_list": some_list
	}
	return render(request, "base.html", context)

def home2(request):
	num = None
	some_list = [random.randint(0,100000000), random.randint(0,100000000), random.randint(0,100000000)]
	condition_bool_item = True
	title = "Django Basics"
	if condition_bool_item:
		num = random.randint(0,100000000)

	context = {
			# "bool_item": True,
			"num": num,
			"django": title,
			"some_list": some_list
	}
	return render(request, "base.html", context)

def home3(request):
	num = None
	some_list = [random.randint(0,100000000), random.randint(0,100000000), random.randint(0,100000000)]
	condition_bool_item = True
	title = "Django Basics"
	if condition_bool_item:
		num = random.randint(0,100000000)

	context = {
			# "bool_item": True,
			"num": num,
			"django": title,
			"some_list": some_list
	}
	return render(request, "base.html", context)