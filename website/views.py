from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import  DailyANCRegisterForm,LabourDeliveryRegisterForm,ChildImmunizationRegisterForm,ChildImmunizationTallyForm 
from .models import DailyANCRegister,LabourDeliveryRegister, ChildImmunizationRegister,ChildImmunizationTally 


from datetime import datetime
from calendar import monthrange
import logging

logger = logging.getLogger('myapp')  # Use the logger you defined in settings

def home(request):
   
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            # Authenticate
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You Have Been Logged In!")
                return redirect('home')
            else:
                messages.success(request, "There Was An Error Logging In, Please Try Again...")
                return redirect('home')
    else:
		    return render(request, 'home.html', {})

        

def login_user(request):
    pass

def logout_user(request):
    pass

def anc_register_create(request):
    if request.method == 'POST':
        form = DailyANCRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('anc_register_list')  # Redirect to a success page
        else:
            print("Form is not valid:", form.errors)  # Output validation errors
    else:
        form = DailyANCRegisterForm()
    return render(request, 'anc_register_create.html', {'form': form})

def anc_register_view(request, id):
    entry = get_object_or_404(DailyANCRegister, id=id)  # Retrieve the specific entry by ID
    return render(request, 'anc_register_view.html', {'entry': entry})


def anc_register_list(request):
    records = DailyANCRegister.objects.all()  # Retrieve all StateBudget records
    return render(request, 'anc_register_list.html', {'records': records})


#labour register create


def labour_register_create(request):
    if request.method == 'POST':
        form = LabourDeliveryRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('labour_register_list')  # Redirect to a success page
        else:
            print("Form is not valid:", form.errors)  # Output validation errors
    else:
        form = LabourDeliveryRegisterForm()
    return render(request, 'labour_register_create.html', {'form': form})


#list labour register
def labour_register_list(request):
    records =LabourDeliveryRegister.objects.all()  # Retrieve all StateBudget records
    return render(request, 'labour_register_list.html', {'records': records})



def labour_register_view(request, id):
    entry = get_object_or_404(LabourDeliveryRegister, id=id)  # Retrieve the specific entry by ID
    return render(request, 'labour_register_view.html', {'entry': entry})



#labour register create

def child_immunization_create(request):
    if request.method == 'POST':
        form = ChildImmunizationRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('child_immunization_list')  # Redirect to a success page
        else:
            print("Form is not valid:", form.errors)  # Output validation errors
    else:
        form = ChildImmunizationRegisterForm()
    return render(request, 'child_immunization_create.html', {'form': form})



#list immunization register
def child_immunization_list(request):
    records =ChildImmunizationRegister.objects.all()  # Retrieve all StateBudget records
    return render(request, 'child_immunization_list.html', {'records': records})



def child_immunization_view(request, id):
    entry = get_object_or_404(ChildImmunizationRegister, id=id)  # Retrieve the specific entry by ID
    return render(request, 'child_immunization_register_view.html', {'entry': entry})


#tally 
def child_immunization_tally_create(request):
    if request.method == 'POST':
        form = ChildImmunizationTallyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('child_immunization_tally_list')  # Redirect to a success page
        else:
            print("Form is not valid:", form.errors)  # Output validation errors
    else:
        form = ChildImmunizationRegisterForm()
    return render(request, 'child_immunization_tally_create.html', {'form': form})



#list immunization register
def child_immunization_tally_list(request):
    records =ChildImmunizationTally.objects.all()  # Retrieve all StateBudget records
    return render(request, 'child_immunization_tally_list.html', {'records': records})





def dashboard(request):
    # You can fetch data here for the charts if needed
    data = (
        StateImplementingPartner.objects.values('thematic_area')
        .annotate(total_cost=Sum('actual_implementation_cost'))
    )
    thematic_areas = []
    total_costs = []
    for entry in data:
        thematic_areas.append(entry['thematic_area'])
        total_costs.append(entry['total_cost'])

    context = {
        'thematic_areas': thematic_areas,
        'total_costs': total_costs,
    }
    return render(request, 'dashboard.html',context)