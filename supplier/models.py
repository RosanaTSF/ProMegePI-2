from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

USER = get_user_model()


# Abstracts Models
class PhoneBase(models.Model):
    class TypePhoneChoice(models.TextChoices):
        LANDLINE = "LL", _("Telefone Fixo")
        MOBILE = "MB", _("Celular")
    """Model definition for PhoneContact."""
    
    type_phone = models.CharField(_("Telefone"), max_length=2, choices=TypePhoneChoice.choices, default="MB")
    ddi_number = models.CharField(_("DDI"), max_length=3, null=True, blank=True)
    ddd_number = models.CharField(_("DDD"), max_length=2, null=False, blank=False)
    phone_number = models.CharField(_("Número"), max_length=9, null=False, blank=False)

    class Meta:
        abstract = True


class TimeStampBase(models.Model):
    
    created = models.DateTimeField(_("Criado em"), auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(_("Modificado em"), auto_now=True, auto_now_add=False)
    created_by = models.ForeignKey(
        USER, 
        verbose_name=_("Usuário"), 
        on_delete=models.CASCADE
    )
    class Meta:
        abstract = True

# Create your models here.
class Supplier(TimeStampBase):   
    """Model definition for Supplier."""
    
    
    is_active = models.BooleanField(_("Ativo"), default=True)
    company_name = models.CharField(_("Razão Social"), max_length=150, null=False, blank=False)
    fantasy_name = models.CharField(_("Nome Fantasia"), max_length=150, null=True, blank=True)
    cnpj_number = models.CharField(_("CNPJ"), max_length=14, null=False, blank=True)

    class Meta:
        """Meta definition for Supplier."""

        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        """Unicode representation of Supplier."""
        if self.fantasy_name:
            return self.fantasy_name.title()
        return self.company_name


class ContactSupplier(models.Model):
    """Model definition for ContactSupplier."""

    supplier_id = models.ForeignKey(
        Supplier, 
        verbose_name=_("Fornecedores"),
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(_("Nome"), max_length=30, null=False, blank=False)
    last_name = models.CharField(_("Sobrenome"), max_length=50, null=True, blank=True)
    position_company = models.CharField(_("Cargo na Empresa"), max_length=50, null=False, blank=False)
    e_mail = models.EmailField(_("E-mail"), max_length=254, null=False, blank=False)
    remarks = models.CharField(_("Observações"), max_length=254, null=True, blank=True)

    class Meta:
        """Meta definition for ContactSupplier."""

        verbose_name = 'Contato do Fornecedor'
        verbose_name_plural = 'Contatos dos Fornecedores'
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        """Unicode representation of ContactSupplier."""
        
        return f'{self.full_name.title()} - {self.position_company.title}'


class PhoneContact(PhoneBase):

    contact = models.ForeignKey(
        ContactSupplier, 
        verbose_name=_("Telefone"), 
        on_delete=models.CASCADE,
    )
    
    class Meta:
        """Meta definition for PhoneContact."""

        verbose_name = 'Telefones do Contato'
        verbose_name_plural = 'Telefones dos Contatos'

    def __str__(self):
        """Unicode representation of PhoneContact."""
        if self.ddi_number:
            return f'+{self.ddi_number} ({self.ddd_number}) {self.phone_number}'
        return f'({self.ddd_number}) {self.phone_number}'


class PhoneSupplier(PhoneBase):

    supplier_id = models.ForeignKey(
        Supplier, 
        verbose_name=_("Telefone"), 
        on_delete=models.CASCADE,
    )

    class Meta:
        """Meta definition for PhoneContact."""

        verbose_name = 'Telefones do Contato'
        verbose_name_plural = 'Telefones dos Contatos'

    def __str__(self):
        """Unicode representation of PhoneContact."""
        if self.ddi_number:
            return f'+{self.ddi_number} ({self.ddd_number}) {self.phone_number}'
        return f'({self.ddd_number}) {self.phone_number}'


class RequestSupplier(models.Model):
    class StatusChoice(models.TextChoices):
        INITIATED = "IT", _("Iniciado")
        PARALYZED = "PL", _("Paralizado")
        INPROGRESS = "IP", _("Em andamento")
        FINISHED = "FN", _("Finalizado")
        COMPLETED = "CP", _("Concluido")    
    """Model definition for ResquestSupplier."""

    supplier_id = models.ForeignKey(
        Supplier,
        verbose_name=_("Fornecedor"), 
        on_delete=models.CASCADE
    )
    request_date = models.DateField(_("Data da Requisição"), null=False, blank=False)
    reson_hiring = models.CharField(_("Motivo da Contratação"), max_length=254, null=False, blank=False)
    contract_value = models.FloatField(_("Valor Total do Contrato"), null=False, blank=False)
    status = models.CharField(_("Status"), max_length=2, choices=StatusChoice.choices, default="IT")

    class Meta:
        """Meta definition for ResquestSupplier."""

        verbose_name = 'Requisição ao Fornecedor'
        verbose_name_plural = 'Requisições aos Fornecedores'

    def __str__(self):
        """Unicode representation of ResquestSupplier."""
        return f'Data {self.request_date} - Valor Total R$ {self.contract_value}'
