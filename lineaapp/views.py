from django.shortcuts import render,redirect
from .models import*
# Create your views here.
def index(request):
    lines=post.objects.all().order_by('-date')
    return render(request,'index.html',{'lines':lines})

def create_accounts(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        pswd=request.POST.get("pswd")
        obj=account.objects.create(name=name,email=email,pswd=pswd)
        obj.save()
        if obj:
            return redirect(login)
        else:
            return redirect(create_accounts)
    return render(request,'create_account.html')

def login(request):
    if request.method=='POST':
        email=request.POST.get("email")
        pswd=request.POST.get("pswd")
        user=account.objects.filter(email=email,pswd=pswd).first()
        if user:
            request.session['user_id'] = user.id
            return redirect(home_page,id=user.id)
        else:
            return render(request, 'login.html', {
                'error_message': "Invalid email or password. Please try again."
            })
    return render(request,'login.html')

def home_page(request,id):
    user=account.objects.filter(id=id).first()
    return render(request,'home_page.html',{'user':user})

def upload_post(request,id):
    user = account.objects.filter(id=id).first()
    if request.method=='POST':
        content=request.POST.get("content")
        if user:
            post.objects.create(user=user,lines=content)
            return redirect(index)
    lines = post.objects.filter(user=user).order_by('-date')
    return render(request, 'home_page.html', {'user': user, 'lines': lines})

def view_my_lines(request,id):
    user=account.objects.get(id=id)
    lines=post.objects.filter(user=user).order_by('-date')
    return render(request, 'view_my_lines.html', {'lines': lines})

def delete_lines(request,id):
     user_id = request.session.get('user_id')
     user = account.objects.filter(id=user_id).first()
     line = post.objects.filter(id=id, user=user).first()
     line.delete()
     return redirect('view_my_lines', id=user.id)

def edit_post(request,id):
    user_id = request.session.get('user_id')
    user = account.objects.filter(id=user_id).first()
    line = post.objects.filter(id=id, user=user).first()
    if request.method == 'POST':
        new_content = request.POST.get('content')
        if new_content:
            line.lines = new_content
            line.save()
            return redirect('view_my_lines', id=user.id)
    return render(request,'edit_post.html', {'line': line})