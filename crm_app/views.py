from django.shortcuts import render, get_object_or_404, redirect
from .models import Service, AdCampaign, Lead, Contract, Client
from .forms import ContractForm
from django.db.models import Sum, Count
# Create your views here.

def promote_lead_view(request, lead_id):
    #поиск лида по его id
    lead = get_object_or_404(Lead, id=lead_id)

    if request.method == "POST":
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            #1. Сохраняем контракт в базу
            contract = form.save()

            #2. Создаем активного клиента, связываяя лида и новый контракт
            Client.objects.create(lead=lead, contract=contract)

            #3. После успеха отправляем менеджера в список активных клиентов
            return redirect("customers_list")

    else:
        form = ContractForm()

    return render(request, "create_contract.html", {"form": form, "lead": lead})


def customers_view(request):
    #список тех, кто уже заключил контракт
    customers = Client.objects.all()
    return render(request, "customers_list.html", {"customers": customers})


def index_view(request):
    #общее количество лидов и клиентов
    total_leads = Lead.objects.count()
    total_clients = Client.objects.count()

    #прибыль
    total_revenue = Contract.objects.aggregate(Sum("amount"))["amount__sum"] or 0

    #расчет эффективности каждой компании
    campaign_stats = AdCampaign.objects.annotate(
        lead_count=Count("lead"),
        clients_count=Count("lead__client")
    )

    context = {
        "total_leads": total_leads,
        "total_clients": total_clients,
        "total_revenue": total_revenue,
        "campaign_stats": campaign_stats,
    }
    return render(request, "index.html", context)


def campaigns_view(request):
    campaigns = AdCampaign.objects.all()
    return render(request, "campaigns_list.html", {"campaigns": campaigns})


def lead_view(request):
    leads = Lead.objects.all()
    return render(request, "leads_list.html", {"leads": leads})