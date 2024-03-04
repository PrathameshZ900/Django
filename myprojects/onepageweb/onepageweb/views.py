from django.http import HttpResponse,HttpResponseRedirect

from django.shortcuts import render
from .forms import UsersForm
from service.models import ServiceItem
from news.models import NewsArticle

def about_us(request,idd):
    return HttpResponse(idd+" Welcome to my Django Project")

# def check_prime(request):
#     # Get the value of 'n' from the request
#     n = int(request.GET.get('n', 0))

#     cn = 0
#     for i in range(2, n // 2):
#         if n % i == 0:
#             cn += 1

#     if cn == 0:
#         return HttpResponse("It's Prime ok.")
#     else:
#         return HttpResponse("It's not Prime Broo.")


# from django.shortcuts import render
# from django.http import HttpResponse

# def check_prime(request):
#     if request.method == 'POST':
#         number = int(request.POST.get('number', 0))
#         is_prime = True if number > 1 and all(number % i != 0 for i in range(2, int(number**0.5) + 1)) else False
#         return render(request, 'prime_result.html', {'number': number, 'is_prime': is_prime})
#     else:
#         return render(request, 'check_prime_form.html')

def course(request,courseid):
    return HttpResponse(courseid+" This is your Course.")


def check_prime(request,n):
    cn=0
    n=int(n)
    for i in range(2,n//2):
        if(n%i==0):
            cn+=1
    if(cn==0):
        return HttpResponse("<b style='color:green;'>" + str(n) + "</b> is a Prime Number.")
    else:
        return HttpResponse("<b style='color:red;'>" + str(n) + "</b> is not a Prime Number.")            

def homePage(request):
    return render(request,"index.html")


def homeDjango(request):
    data={
        'title':"Home",
        'intro':"Hello This Is First Project for D-Jango part...",
        'img1':"https://www.djangoproject.com/m/img/logos/django-logo-negative.png",
        'img2':"https://images.ctfassets.net/aq13lwl6616q/OTaLX16ljumwlrj5KfHC0/f2e1e55a249f4ce5dc4704374f610c3c/Course_Thumbnail_-_Django_3.png"


    }
    return render(request,"index.html",data)
def stdData(request):
    data={
        'logo':"CodePM",
        'numbers':[1,2,3,4,5,6,7],
        'course':["Java","Python","React","NodeJs","C++","GOLang"],
        'std':[{'name':"Prathamesh Magar",'Phone':9284297393,'class':"12th com"},
        {'name':"Rushikesh Gaware",'Phone':9284297393,'class':"last year B.A." }]
    }
    return render(request,"index.html",data)
def is_prime(n):
    cn=0
    n=int(n)
    for i in range(2,n//2):
        if(n%i==0):
            cn+=1
    if(cn==0):
        return ("<b style='color:green;'>" + str(n) + "</b> is a Prime Number.")
    else:
        return ("<b style='color:red;'>" + str(n) + "</b> is not a Prime Number.")   
# def userform(request):
#     data={
#         'title':"User Form",

#     }


#     return render(request, "userform.html",data)
  
# def submit(request):
#     try:
#         n1=request.GET("username")
#         n2=request.GET("email")
#         n3=request.GET("password")
#         n4=request.GET("confirm_password")
#         n5=request.GET("birthdate")
#         n6=request.GET("gender")

#         print("UserName: "+n1)
#         print("E-mail: "+n2)
#         print("Birthdate: "+n5)
#         print("Gender: "+n6)

#     except:
#         pass

# views.py



def userform(request):
    data = {'title': "User Form"}

    if request.method == 'POST':
        try:
            # Retrieving form data from POST request
            n1 = request.POST.get("username")
            n2 = request.POST.get("email")
            n3 = request.POST.get("password")
            n4 = request.POST.get("confirm_password")
            n5 = request.POST.get("birthdate")
            n6 = request.POST.get("gender")

            # Printing form data
            print("UserName: ", n1)
            print("E-mail: ", n2)
            print("Birthdate: ", n5)
            print("Gender: ", n6)

            # You can perform further processing here, such as saving data to a database

        except Exception as e:
            print("Error:", e)

    return render(request, "userform.html", data)

def submit(request):
    if request.method == 'POST':
        # Retrieving form data from POST request
        n1 = request.POST.get("username")
        n2 = request.POST.get("email")
        n3 = request.POST.get("password")
        n4 = request.POST.get("confirm_password")
        n5 = request.POST.get("birthdate")
        n6 = request.POST.get("gender")

        # Printing form data
        print("UserName: ", n1)
        print("E-mail: ", n2)
        print("Birthdate: ", n5)
        print("Gender: ", n6)

        # You can perform further processing here, such as saving data to a database

    return render(request, "userform.html") 
def sum(request):
    ans=0
    try:
        n1=int(request.GET["num1"])
        n2=int(request.GET["num2"])
        ans=n1+n2
    except:
        pass 
    return render(request, "get.html",{"ans":ans})


def sumpost(request):
    data = {}  # Initialize data dictionary
    if request.method == "POST":
        try:
            # Retrieve values from the POST request
            n1 = int(request.POST.get("num1", 0))  # Use .get() method with a default value
            n2 = int(request.POST.get("num2", 0))  # Use .get() method with a default value
            ans = n1 + n2  # Calculate the sum
            # Store data in a dictionary for rendering
            data = {
                'n1': n1,
                'n2': n2,
                'ans': ans
            }
            url = "/userform/?ans={}".format(ans)
            print(ans)
            return HttpResponseRedirect('/userform/')
        except ValueError:
            # Handle the case where the values cannot be converted to integers
            data['error'] = "Invalid input. Please enter valid numbers."
       
    return render(request,"post.html",data)

def action(request):
    data = {}  # Initialize data dictionary
    if request.method == "POST":
        try:
            # Retrieve values from the POST request
            n1 = int(request.POST.get("num1", 0))  # Use .get() method with a default value
            n2 = int(request.POST.get("num2", 0))  # Use .get() method with a default value
            ans = n1 + n2  # Calculate the sum
            # Store data in a dictionary for rendering
            data = {
                'n1': n1,
                'n2': n2,
                'ans': ans
            }
            url = "/CheckPrime/?ans={}".format(ans)
            print(ans)
            return HttpResponseRedirect('/CheckPrime/'+str(ans))
        except ValueError:
            # Handle the case where the values cannot be converted to integers
            data['error'] = "Invalid input. Please enter valid numbers."
       
    return render(request,"action.html",data)



def formDjango(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            # Retrieving form data from validated form
            username = form.cleaned_data.get("UserName")
            email = form.cleaned_data.get("E_mail")
            password = form.cleaned_data.get("Password")
            birthdate = form.cleaned_data.get("Birthdate")
            gender = form.cleaned_data.get("Gender")

            # Printing form data
            print("UserName:", username)
            print("E-mail:", email)
            print("Password:", password)
            print("Birthdate:", birthdate)
            print("Gender:", gender)

            # You can perform further processing here, such as saving data to a database

            return render(request, "success.html", {'username': username})  # Redirect to success page
        else:
            print("Form is not valid")
    else:
        form = UsersForm()

    return render(request, "formdjango.html", {'title': "User Form", 'form': form})






def service_view(request):
    servicedata = ServiceItem.objects.all().order_by('title')[2:9]
    data = {
        'servicedata': servicedata,
    }
    return render(request, "service.html", data)



def news(request):
    newsdata = NewsArticle.objects.all().order_by("headline")[:3]
    data = {
        'newsdata': newsdata,
    }
    return render(request, "news.html", data)

