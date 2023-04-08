from django.shortcuts import render
from app.models import *
# Create your views here.
def deptment(request):
    do=dept.objects.all()
    D={'details':do}
    return render(request,'d.html',D)
def emp_no(request):
    em=emp.objects.all()
    em=emp.objects.filter(ename__startswith='a')
    em=emp.objects.filter(ename__startswith='s')
    em=emp.objects.filter(hiredate__year='1981')
    em=emp.objects.all()
    D={'details1':em}
    return render(request,'e.html',D)