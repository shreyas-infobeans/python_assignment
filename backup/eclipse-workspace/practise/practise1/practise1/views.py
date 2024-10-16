from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import UsersForm

def aboutUs(request):
   name = request.GET['output']
   return render(request,"blog-single.html",{'name':name})

def userForm(request):
   name = ''
   email = ''
  
   fn = UsersForm()
   data = {'form':fn}
   try:
      name = request.POST['name']
      email = request.POST['email']
      data = {
         'name':name,'email':email
      }
      url = "/about-us?output={}".format(email)
      return HttpResponseRedirect(url)
   except:
      pass
   return render(request,"userform.html",data)

def portfolio(request):
   return render(request,"portfolio-details.html")

def calculator(request):
   c  = ''
   try:
      if(request.method=="POST"):
         n1 = eval(request.POST.get('num1'))
         n2 = eval(request.POST.get('num2'))
         action = request.POST.get('action')
         if action=="multiple":
            c = n1*n2
         elif action=="add":
            c = n1+n2
         elif action=="subtract":
            c = n1-n2
         elif action=="divide":
            c = n1+n2
  
   except:
      c = "Invalid"
   print(c)
   return render(request,"calculator.html",{"c":c})

def contactUs(request):
   return render(request,"contact.html")

def home(request):
  data = {
    'title':'Home Page111',
    'bdata':"here you go",
    'clist':['PHP','Java','Oracle'],
    'number':[10,20,30],
    'student_details':[
      {'name':'pradeep','phone':'0000'},
      {'name':'shreyas','phone':'3333'}
    ]
  }
  return render(request,"index.html",data)

def Course(request):
  return HttpResponse("Course Page")

def courseDetails(request,courseId):
  return HttpResponse(courseId)