from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect
from .models import Lead,Agent
from .forms import LeadForm
# Create your views here.

def lead_list(request):
    leads = Lead.objects.all()
    context ={
        'leads':leads
    }
    return render(request,"leads/lead_list.html",context)

def lead_detail(request,pk):
    lead = Lead.objects.get(id = pk)
    context = {
        'lead' : lead
    }
    return render(request,"leads/lead_detail.html",context)
@csrf_protect
def lead_create(request):
    form = LeadForm()
    print(request.POST)
    if request.method == 'POST':
        print("Recieving a post request")
        form = LeadForm(request.POST)

        if form.is_valid():
            print('Form is valid')
            print(form.cleaned_data)
            Lead.objects.create(
                first_name =  form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                age= form.cleaned_data['age'],
                agent = Agent.objects.first()

            )
            print('The lead has been created !')
            return redirect('/leads')
    context = {
        'form' : form
    }

    return render(request,"leads\lead_create.html",context)

