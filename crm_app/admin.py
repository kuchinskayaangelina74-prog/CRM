from django.contrib import admin
from .models import Service, AdCampaign, Lead, Contract, Client
# Register your models here.

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "cost")


@admin.register(AdCampaign)
class AdCampaignAdmin(admin.ModelAdmin):
    list_display = ("name", "service", "channel", "budget")


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone", "campaign")


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ("name", "date_created", "amount")


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("lead", "contract")
    


