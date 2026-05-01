from django.db import models

# Create your models here.
class Service(models.Model):
    #услуги компании
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")

    def __str__(self):
        return self.name


class AdCampaign(models.Model):
    #рекламные компании
    name = models.CharField(max_length=255, verbose_name="Название компании")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Услуга")
    channel = models.CharField(max_length=255, verbose_name="Канал продвижения")
    budget = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Бюджет")

    def __str__(self):
        return self.name


class Lead(models.Model):
    #потенциальные клиенты
    full_name = models.CharField(max_length=255, verbose_name="Ф.И.О.")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    campaign = models.ForeignKey(AdCampaign, on_delete=models.SET_NULL, null=True, verbose_name="Рекламная компания")

    def __str__(self):
        return self.full_name


class Contract(models.Model):
    #контракты
    name = models.CharField(max_length=255, verbose_name="Название")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Услуга")
    document = models.FileField(upload_to="contracts/", verbose_name="Файл с документом")
    date_created = models.DateField(verbose_name="Дата заключения")
    expiry_date = models.DateField(verbose_name="Период действия (до)")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")

    def __str__(self):
        return self.name


class Client(models.Model):
    #активные клиенты
    lead = models.OneToOneField(Lead, on_delete=models.CASCADE, verbose_name="Потенциальный клиент")
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, verbose_name="Контракт")

    def __str__(self):
        return f"Активный клиент: {self.lead.full_name}"

