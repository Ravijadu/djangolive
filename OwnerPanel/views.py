from django.shortcuts import render,redirect
from .forms import OwnerRegistration

# Create your views here.
def owner(request):
  if request.method == 'POST':
    fm = OwnerRegistration(request.POST,request.FILES)
    if fm.is_valid():
      fm.save()
      return render(request,'OwnerListing/owner.html',{'form':fm})
  else:
    fm = OwnerRegistration()
  return render(request,'OwnerListing/owner.html',{'form':fm})




