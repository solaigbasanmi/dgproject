from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import DailyANCRegisterForm,LabourDeliveryRegisterForm,ChildImmunizationRegisterForm, ContraceptiveStatisticsForm,StateBudgetForm,StateCostImplementationPlanForm,StateImplementingPartnerForm,StateFPCommodityForm,StateCommodityMixForm
from .models import DailyANCRegister,LabourDeliveryRegister, ChildImmunizationRegister, ContraceptiveStatistics,StateBudget,StateCostImplementationPlan,StateImplementingPartner,StateFPCommodity,StateCommodityMix
from django.db.models import Sum

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
        form = DailyANCRegisterForm()
    return render(request, 'anc_register_create.html', {'form': form})

def anc_register_list(request):
    records = DailyANCRegister.objects.all()  # Retrieve all StateBudget records
    return render(request, 'anc_register_list.html', {'record': records})


#labour register create
def labour_register_create(request):
    if request.method == 'POST':
        form = LabourDeliveryRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('labour_register_list')  # Redirect to a success page
    else:
        form = LabourDeliveryRegisterForm()
    return render(request, 'labour_register_create.html', {'form': form})

#list labour register
def labour_register_list(request):
    records =LabourDeliveryRegister.objects.all()  # Retrieve all StateBudget records
    return render(request, 'labour_register_list.html', {'record': records})


#labour register create
def child_immunization_create(request):
    if request.method == 'POST':
        form = ChildImmunizationRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('child_immunization_list')  # Redirect to a success page
    else:
        form = ChildImmunizationRegisterForm()
    return render(request, 'child_immunization_create.html', {'form': form})

#list labour register
def child_immunization_list(request):
    records =LabourDeliveryRegister.objects.all()  # Retrieve all StateBudget records
    return render(request, 'child_immunization_list.html', {'record': records})



def add_state_budget(request):
    if request.method == 'POST':
        form = StateBudgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('state_budget_list')  # Redirect to a success page
    else:
        form = StateBudgetForm()
    return render(request, 'add_state_budget.html', {'form': form})

def list_state_budget(request):
    budgets = StateBudget.objects.all()  # Retrieve all StateBudget records
    return render(request, 'list_state_budget.html', {'budgets': budgets})

# List all implementation plans
def list_state_costed_implementation_plan(request):
    plans = StateCostImplementationPlan.objects.filter(is_deleted=False)
    return render(request, 'list_state_costed_implementation_plan.html', {'plans': plans})

# Add a new implementation plan
def add_state_costed_implementation_plan(request):
    if request.method == 'POST':
        form = StateCostImplementationPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_state_costed_implementation_plan')
    else:
        form = StateCostImplementationPlanForm()
        return render(request, 'add_state_costed_implementation_plan.html', {'form': form})
    
def list_state_implementation_partner(request):
    partners = StateImplementingPartner.objects.filter(is_deleted=False)
    return render(request, 'list_state_implementation_partner.html', {'partners': partners})

# Add a new implementing partner
def add_state_implementation_partner(request):
    if request.method == 'POST':
        form = StateImplementingPartnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_state_implementation_partner')  # Redirect to the list view
    else:
        form = StateImplementingPartnerForm()
    return render(request, 'add_state_implementation_partner.html', {'form': form})


def list_fp_commodity(request):
    data = StateFPCommodity.objects.filter(is_deleted=False)
    return render(request, 'list_fp_commodity.html', {'commodities': data})

# Add a new implementing partner
def add_fp_commodity(request):
    if request.method == 'POST':
        form = StateFPCommodityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_fp_commodity')  # Redirect to the list view
    else:
        form = StateFPCommodityForm()
        return render(request, 'add_fp_commodity.html', {'form': form})
    
def list_state_commodity_mix(request):
    data = StateCommodityMix.objects.filter(is_deleted=False)
    return render(request, 'list_state_commodity_mix.html', {'commodities': data})

# Add a new implementing partner
def add_state_commodity_mix(request):
    if request.method == 'POST':
        form = StateCommodityMixForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_state_commodity_mix')  # Redirect to the list view
    else:
        form = StateCommodityMixForm()
        return render(request, 'add_state_commodity_mix.html', {'form': form})
    
def list_contraceptive_statistics(request):
    statistics = ContraceptiveStatistics.objects.all()  # Retrieve all instances
    return render(request, 'list_contraceptive_statistics.html', {'statistics': statistics})
def add_contraceptive_statistics(request):
    if request.method == 'POST':
        form = ContraceptiveStatisticsForm(request.POST)
        if form.is_valid():
            form.created_by ='demo'
            form.save()  # Save the form data to the database
            return redirect('list_contraceptive_statistics')  # Redirect to a relevant page after success
    else:
        form = ContraceptiveStatisticsForm()
    
    return render(request, 'add_contraceptive_statistics.html', {'form': form})
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