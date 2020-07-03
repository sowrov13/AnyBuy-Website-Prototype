from django.shortcuts import render
# from django.http import HttpResponse
from.models import Description

# Create your views here.
def home(request):
    
    updates = Description.objects.all()
    # update1 = Description()
    # update1.name = "Lokhon"
    # update1.desc = "School"
    # update1.price = 75
    # update1.img = 'img_1.jpg'
    

    
    # update2 = Description()
    # update2.name = "Siam"
    # update2.desc = "College"
    # update2.price = 70
    # update2.img = 'img_4.jpg'

    
    # update3 = Description() 
    # update3.name = "Shoumik"
    # update3.desc = "Home"
    # update3.price = 140
    # update3.img = 'img_3.jpg'
   
    
    # updates = [update1, update2, update3]
    
    return render(request, 'anybuyhtml.html',{'updates': updates})