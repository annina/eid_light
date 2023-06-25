
from django.shortcuts import render
from .models import Light, Friends

import json, random, string

from django.core.serializers import serialize
from django.http import JsonResponse

from django.contrib.auth.models import User


def index(request):
	
	return render(request, 'index.html',)
	

def tutorial(request):
	
	return render(request, 'tutorial.html',)
	

def privacy(request):
	
	return render(request, 'privacy.html',)
	

def yourlights(request, pk):
	if pk != 0:
		l = Light.objects.filter(user = pk)

	return render(request, 'yourlights.html', {'lights':l}  )



def public(request):
	
	return render(request, 'privacy.html',)
	

def deletelight(request,pk,lk):
	
	if pk != 0:
		
		l = Light.objects.filter(user = pk)
	if lk != 0:
		dl= Light.objects.filter(id = lk).delete()
		
		
		l = Light.objects.filter(user = pk)
			
	
		
		return render(request, 'createlight.html', {'lights':l}  )

	else:
		return render(request, 'createlight.html')	
	
		
def deletefriend(request,pk,lk):
	
	l = Light.objects.get(id=lk)
	f = Friends.objects.all().filter(light = l)
	
	if pk != 0:
		df= Friends.objects.filter(id = pk).delete()		
		return render(request, 'start.html', {'id':l.id,  'friends' : f, 'light_string':l.ident,})
	else:
		return render(request, 'start.html', {'id':l.id,  'friends' : f, 'light_string':l.ident,})



	
def createlight(request,pk):
	if pk != 0:
	
		l = Light.objects.filter(user = pk)
	
		print(l);

	
	
	
	
	
		if str(request.GET.get('lightname','')):
			name1 = request.GET.get('lightname','')
			print("lightname "+ name1);
			if str(request.GET.get('public','')) == "on":
				print("is public!");
				public1 = True
			else :
				public1 = False		
	

			lt = Light(name = name1,ident = get_random_string(10) , public = public1, user = request.user)
			lt.save()
		
			
		return render(request, 'createlight.html', {'lights':l}  )
	else:
		
		return render(request, 'createlight.html')	




def addfriends(request, pk, characters):
	if str(request.GET.get('name','')):
		
		name1 = str(request.GET.get('name',''))
		id1 = str(request.GET.get('id',''))
		sl1 =  get_random_string(10)
		print(get_random_string(10))
		f = Friends(name=name1,light=Light.objects.get(id=pk),on=False, ident=sl1)
		print("request.GET.get")
		print(name1)
		f.save();
	
	l = Light.objects.get(id=pk)
	

	f = Friends.objects.all().filter(light = l)
	
	
	return render(request, 'start.html', {'id':l.id,  'friends' : f, 'light_string':l.ident,})
	
def friend(request, pk, characters):
	

	
	if str(request.GET.get('on','')):
		# set status of light to "on"	
		f = Friends.objects.filter(ident__startswith = characters)
		for i in f:
			i.on = True
			i.save() # this will update only
		b = Friends.objects.filter(ident__startswith = characters)
		print(b[0].on)
		print (b[0].name)
		print("it should now be on")
	
		
		
		return render(request, 'light_on.html', {'id':pk,  'string' :characters, 'on':1 })
	else:
		l = Friends.objects.filter(ident__startswith = characters)
		if l[0].on == True:
			print(l[0].name + " the light should now be on ");
			print(l[0].on)
			return render(request, 'light_on.html', {'id':pk,  'string' :characters, 'on':1})	
		else:
			return render(request, 'light_on.html', {'id':pk,  'string' :characters, 'on':0 })


def light(request,pk,characters):
	# we need the random string.
	
	
	return render(request, 'lightlight.html', {'id':pk, 'characters': characters})

	
def jsonResponse(request,pk,characters):
	
	qs = Friends.objects.filter(light = pk)
	qs_json = serialize('json', qs)
	return JsonResponse(qs_json, safe=False)
	

	

def get_random_string(length):

    # choose from all lowercase letter
    # from here https://pynative.com/python-generate-random-string/
   	result_str = ''.join(random.sample(string.hexdigits, length))
   	return result_str
   	

  