from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from StudentManagementApp.models import Student

# Create your views here.
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if pass1 != pass2:
            messages.error(request, 'password do not match')
            return redirect('signup')


        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, "your account has been sucessfully created now you can login")
            return render(request, 'StudentManagementApp/signup.html')
        else:
            messages.error(request, "please choose a unique user")
            return render(request, 'StudentManagementApp/signup.html')


        #here User is a table conatin Admin interface in which we create the user
    else:
        return render(request,'StudentManagementApp/signup.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST['loginname']
        password = request.POST['loginpasword']
        # to authenticate user and password  si valid or not djnago provide an inbuilt module autheticate,
        user = authenticate(username=username, password=password)  # here we authenticate username and password
        if user is not None:  # means user and password is  valid
             request.session['uid'] = request.POST['loginname']
             login(request, user)  # means then user can login
             messages.success(request, 'user login successfully')
             return redirect('insert')
        else:
             messages.error(request, 'invalid username and password please try again')
             return render(request, 'StudentManagementApp/login.html')

    return render(request, 'StudentManagementApp/login.html')

def insert(request):
    if request.session.has_key('uid') and request.method == "GET":
        return render(request,'StudentManagementApp/insert.html')
    elif request.method=='POST':
      user=request.user
      fname = request.POST['fname']
      lname = request.POST['lname']
      course = request.POST['course']
      mobileno = request.POST['mobileno']
      email = request.POST['email']
      address=request.POST['address']
      student=Student(user=user,FirstName=fname,LastName=lname,Course=course,Mobileno=mobileno,Email=email,Address=address)
      student.save()
      messages.success(request,'insert record successfully')
      return redirect('insert')

    elif request.method == "GET":
           return redirect('/')

def logout1(request):
    if request.session.has_key('uid') and request.method == "GET":
                logout(request)
                return redirect('login')

def showall(request):
    if request.session.has_key('uid') and request.method=="GET":
            data=Student.objects.filter(user=request.user)
            return render(request,'StudentManagementApp/showall.html',{'data':data})
    else:
        return redirect('login')


def update(request,id):
    if request.session.has_key('uid') and request.method == "GET":
        data=Student.objects.get(Rollno=id)
        return render(request,'StudentManagementApp/update.html',{'data':data})
    elif request.method=='POST':
        data = Student.objects.get(Rollno=id)
        user=request.user
        data.FirstName = request.POST['ufname']
        data.LastName = request.POST['ulname']
        data.Course = request.POST['ucourse']
        data.Mobileno = request.POST['umobileno']
        data.Email = request.POST['uemail']
        user=user
        data.Address=request.POST['uaddress']
        data.save()
        # messages.success(request,'data  successfully')
        return redirect('showall')

    elif request.method == "GET":
           return redirect('/')

def delete(request,id):
    if request.session.has_key('uid'):
        data=Student.objects.get(Rollno=id)
        data.delete()
        return redirect('showall')
    else:
        return redirect('login')







