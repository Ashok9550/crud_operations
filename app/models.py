from django.db import models

# Create your models here.
class dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    dloc=models.CharField(max_length=100)
    def __str__(self):
        return str(self.deptno)
class emp(models.Model):
    deptno=models.ForeignKey(dept,on_delete=models.CASCADE)
    ename=models.CharField(max_length=100)
    empno=models.IntegerField()
    job=models.CharField(max_length=100)
    mgr=models.IntegerField()
    hiredate=models.DateField()
    sal=models.IntegerField()
    comm=models.IntegerField()
    def __str__(self):
        return self.ename

