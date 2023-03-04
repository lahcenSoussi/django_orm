from django.shortcuts import render,redirect
from django.http import HttpResponse as res
from one.models import *

# Create your views here.
def Home(request):
    return res('You are in Your Home')
def Index(request):
    return render(request,'index.html',{'name':'lahcen','city':'Tiflet'})

def List_catgs(request):
    get_catgs = Category.objects.all()
    return render(request,'Category/list_catgs.html',{'ctgs':get_catgs})
def Create_catg(request):
    if request.method == 'POST':
        label = request.POST.get('label')
        new_catg = Category(label=label)
        new_catg.save()
        return redirect('catgs')
    return render(request,'Category/create_catg.html')
def List_courses(request):
    courses = Course.objects.all()
    return render(request,'Course/list_courses.html',{'courses':courses})

def List_profs(request):
    profs = Prof.objects.all()
    return render(request,'Prof/list_profs.html',{'profs':profs})
# def all_courses(request):
#     get_courses = Course.objects.all()
#     return render(request,"courses/index.html",{"courses":get_courses})

# def get_one_course(request,id):
#     get_course = Course.objects.get(id=id)
#     return render(request,"courses/one_course.html",{"course":get_course})

# def update_course(request,id):
#     if request.method =="POST":
#         label = request.POST.get('label')
#         price = int(request.POST.get('price'))
#         tags = request.POST.getlist('tag')
#         course = Course.objects.get(id=id)
#         course.label=label
#         course.price = price
#         course.save()
#         course.tag.set(tags)
#         return redirect('courses')
#     else:
#         course = Course.objects.get(id=id)
#         get_tag = Tag.objects.all()
#         context ={
#             "course":course,
#             "tags" :get_tag,
#         }
#         return render(request,'courses/update_course.html',context)

# def delete_course(request,id):
#     if request.method == 'POST':
#         course = Course.objects.get(id=id)
#         try:
#             course.delete()   
#             return redirect('courses')
#         except Exception as e:
#             print(e)
    
# def create_course(request):
    if request.method == "POST":
        label = request.POST.get('label')
        price = int(request.POST.get('price'))
        catgs = request.POST.get('category')
        tags = request.POST.getlist('tag')
        add_course = Course(label=label,price=price,category_id=catgs)
        add_course.save()
        get_last_course=Course.objects.last()
        get_last_course.tag.add(*tags)
        
        return res('good')
    get_admin = User.objects.all()
    get_catg = Category.objects.all()
    get_tag = Tag.objects.all()
    #get_tag = get_course.tag.all()
    context ={
        "admins" : get_admin,
        "catgs" : get_catg,
        "tags" :get_tag
    }
    return render(request,'courses/create_one_course.html',context)