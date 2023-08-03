from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# from . models import Formdata,District,Branch
# from  .forms import FormPageForm
# Create your views here.
def demo(request):
    return render(request,"home.html")

def login(request):
    if request.method == 'POST':
        return redirect('new_page')
    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        return redirect('login')
    return render(request,"register.html")

def branches(request):
    districts = ["Thiruvananthapuram","Kollam","Alappuzha","Kottayam","Eranakulam"]
    return render(request,"branches.html",{'districts':districts})

def wikipedia_redirect(request):
    district = request.GET.get('district', '')
    wikipedia_url = f"https://en.wikipedia.org/wiki/{district}"
    return redirect(wikipedia_url)

def new_page(request):
    if request.method == 'POST':
        return redirect('form_page')
    return render(request,"new_page.html")

def form_page(request):
    # districts = District.objects.all()
    # branch = Branch.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        date_of_birth = request.POST.get('date_of_birth')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        mail_id = request.POST.get('mail_id')
        mob_no = request.POST.get('mob_no')

        # form_data = Form(
        #     name=name,
        #     date_of_birth=date_of_birth,
        #     age=age,
        #     gender=gender,
        #     address=address,
        #     mail_id=mail_id,
        #     mob_no=mob_no,
        # )
        # form_data.save()
        return redirect('logout')
    return render(request,'form_page.html')

def logout(request):
    if request.method == 'POST':
        return redirect('demo')
    return render(request,"logout.html")

