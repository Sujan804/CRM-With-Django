from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect
from .models import Lead,Agent
from .forms import LeadModelForm,LeadForm
# Create your views here.
def landing_page(request):
    return render(request,"landing.html")

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
    form = LeadModelForm()
    print(request.POST)
    if request.method == 'POST':
        print("Recieving a post request")
        form = LeadModelForm(request.POST)
        if form.is_valid():
            print('Form is valid')
            form.save()
            # print(form.cleaned_data)
            # Lead.objects.create(
            #     first_name =  form.cleaned_data['first_name'],
            #     last_name = form.cleaned_data['last_name'],
            #     age= form.cleaned_data['age'],
            #     agent = form.cleaned_data['agent']
            # )
            print('The lead has been created !')
            return redirect('/leads/')
    context = {
        'form' : form,
        'agents': Agent.objects.all()
    }

    return render(request,"leads\lead_create.html",context)

  ##========================Basic way To ipdate=================
# def lead_update(request,pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method=="POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             lead.first_name = form.cleaned_data['first_name']
#             lead.last_name = form.cleaned_data['last_name']
#             lead.age = form.cleaned_data['age']
#             lead.save()
#             return redirect('/leads/')

#     context = {
#         'lead' :lead,
#         'form' : form
#     }
#     return render(request,'leads/lead_update.html',context)

##Quick and easy way to update

def lead_update(request,pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST,instance=lead)
        form.save()
        return redirect('/leads/')
    
    context = {
        'lead':lead,
        'form' : form
    }

    return render(request,'leads/lead_update.html',context)


def lead_delete(request,pk):
    lead = Lead.objects.get(id= pk)
    lead.delete()
    return redirect('/leads/')





