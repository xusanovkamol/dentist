from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def index(request):
    if request.method=="POST" and 'booking' in request.POST:
        Name=request.POST['Name']
        Number=request.POST['Number']
        Email=request.POST['Email']
        #Comment=request.POST['Comment']
        Text=request.POST['Text']
        send_mail(
            Name,
            f'Bemor {Name} telefon raqami: {Number}\nQabul sanasi: {Text}\n',
            Email,
            ['xusanovkamol01@gmail.com']
        )
        return render(request, 'index.html',{'first_name':Name})
    elif request.method=="POST" and 'sending' in request.POST:
        First_Name=request.POST['First_Name']
        Last_Name=request.POST['Last_Name']
        Email=request.POST['Email']
        Subject=request.POST['Subject']
        Your_Message=request.POST['Your_Message']
        send_mail(
            Subject,
            f'Bemor {First_Name} {Last_Name}\nUning email manzili: {Email}\n{Your_Message}',
            Email,
            ['xusanovk@mail.ru']
        )
        return render(request, 'index.html',{'first_name':First_Name})
    
    
    else:
        return render(request, 'index.html')

    
    