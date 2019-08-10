from django.http import HttpResponse
from django.shortcuts import render
import csv
def data(n,g,h,w,bmi):
    global p,status
    status = ""
    p = ""
    if bmi<18:
        status='Under Weight'
        p = "gain.pdf"
    elif bmi>18 and bmi<23:
        status = 'Fit'
        p = "maintain.pdf"
    elif bmi>23 and bmi<27:
        status = 'Over Weight'
        p = "loss.pdf"
    elif bmi>27 and bmi<32:
        status = 'Obeese Class 1'
        p = "loss.pdf"
    elif bmi>32 and bmi<37:
        status = 'Obeese Class 2'
        p = "loss.pdf"
    elif bmi>37:
        status = 'Obeese Class 3'
        p = "loss.pdf"
        
    with open(r"C:\Users\Sarthak\sc\bmi\bmi\static\1.csv",'a') as data:
        dt = csv.writer(data)
        dt.writerow([n,g,h,w,bmi,status])
    
def hey(request):
    return render(request,'t.html')

def bmi(request):
    global p,status
    name = request.POST.get('name')
    name = name.title()
    gender = request.POST.get('gender')
    height = request.POST.get('height')
    weight = request.POST.get('weight')

    if name=='':
        name = 'no name'
    if gender == '':
        gender = 'not specified'
    if str(height)!='' and str(weight)!='':
        height = int(height)
        height = height/100
        weight=float(weight)
        bmi = weight/(height**2)
        bmi= int(bmi)
        data(name,gender,height,int(weight),bmi)
        l = {'n':name,'g':gender,'h':height,'w':weight,'b':bmi,'address':p,'s':status}
        return render(request,'1.html',l)
    else:
        return HttpResponse('please fill empty spaces first')





