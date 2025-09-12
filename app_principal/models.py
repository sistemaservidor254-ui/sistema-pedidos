from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from decimal import Decimal
from django.core.validators import FileExtensionValidator

# =========================
# ESTOQUE
# =========================


class MovimentoEstoque(models.Model):
    """
    Representa um movimento de estoque (entrada ou saída) de um item licitado.
    Guarda informações como quantidade, data, fornecedor e documento.
    """

    TIPO_CHOICES = (
        ("ENTRADA", "Entrada"),
        ("SAIDA", "Saída"),
    )

    # Relaciona com o item licitado
    item = models.ForeignKey(
        "app_principal.ItemLicitado",
        on_delete=models.PROTECT,  # Não deixa apagar o item se houver movimentos
        related_name="movimentos",
    )

    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    quantidade = models.DecimalField(max_digits=12, decimal_places=3)
    data_movimento = models.DateTimeField(default=timezone.now)
    documento = models.CharField(max_length=100, blank=True)
    observacao = models.TextField(blank=True)

    fornecedor = models.ForeignKey(
        "app_principal.Fornecedor",
        on_delete=models.PROTECT,
        related_name="movimentos",
        null=True,
        blank=True,
    )

    cancelado = models.BooleanField(default=False)

    # Arquivo da NF-e (local)
    arquivo_nf = models.FileField(upload_to="notas_fiscais/", blank=True, null=True)

    # Link público no MEGA
    arquivo_nf_url = models.URLField(blank=True, null=True)

    # Link público no Google Drive
    arquivo_nf_url_drive = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ("-data_movimento", "-id")

    def __str__(self):
        return f"{'[CANCELADO] ' if self.cancelado else ''}{self.tipo} {self.quantidade} de {self.item.codigo} em {self.data_movimento:%d/%m/%Y}"


class SaldoEstoque(models.Model):
    """
    Guarda o saldo atual de um item licitado.
    Atualizado automaticamente via signals quando um MovimentoEstoque é criado ou apagado.
    """

    item = models.OneToOneField(
        "app_principal.ItemLicitado", on_delete=models.CASCADE, related_name="saldo"
    )
    quantidade = models.DecimalField(max_digits=14, decimal_places=3, default=0)

    def __str__(self):
        return f"Saldo {self.item.codigo}: {self.quantidade}"


# Função auxiliar para atualizar saldo
def _aplicar_movimento_no_saldo(item, tipo, quantidade):
    """
    Atualiza o saldo do item conforme o tipo de movimento.
    Entrada soma, saída subtrai.
    """
    saldo, _ = SaldoEstoque.objects.get_or_create(item=item)
    if tipo == "ENTRADA":
        saldo.quantidade = (saldo.quantidade or Decimal("0")) + quantidade
    else:
        saldo.quantidade = (saldo.quantidade or Decimal("0")) - quantidade
    saldo.save(update_fields=["quantidade"])


# Signals para atualizar saldo automaticamente
@receiver(post_save, sender=MovimentoEstoque)
def atualizar_saldo_on_save(sender, instance, created, **kwargs):
    """
    Quando um MovimentoEstoque é criado, atualiza o saldo.
    """
    if created:
        _aplicar_movimento_no_saldo(instance.item, instance.tipo, instance.quantidade)


@receiver(post_delete, sender=MovimentoEstoque)
def atualizar_saldo_on_delete(sender, instance, **kwargs):
    """
    Quando um MovimentoEstoque é apagado, reverte o saldo.
    """
    tipo_inverso = "SAIDA" if instance.tipo == "ENTRADA" else "ENTRADA"
    _aplicar_movimento_no_saldo(instance.item, tipo_inverso, instance.quantidade)


# =========================
# LICITAÇÕES
# =========================


class Edital(models.Model):
    """
    Representa um edital de licitação.
    """

    TIPO_CHOICES = (
        ("ENFERMAGEM", "Enfermagem"),
        ("MEDICAMENTOS", "Medicamentos"),
    )
    numero = models.CharField(max_length=30, unique=True)
    processo = models.CharField(max_length=30, blank=True)
    pregao = models.CharField(max_length=30, blank=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    objeto = models.TextField(blank=True)

    def __str__(self):
        return f"{self.numero} - {self.tipo}"


class Fornecedor(models.Model):
    """
    Representa um fornecedor participante de licitações.
    """

    razao_social = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.CharField(max_length=255, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=2, blank=True)
    telefone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.razao_social} ({self.cnpj})"


class ARPContrato(models.Model):
    """
    Representa um contrato de Ata de Registro de Preços.
    """

    numero_arp = models.CharField(max_length=30)
    edital = models.ForeignKey(
        Edital, on_delete=models.CASCADE, related_name="contratos"
    )
    fornecedor = models.ForeignKey(
        Fornecedor, on_delete=models.CASCADE, related_name="contratos"
    )
    valor_total = models.DecimalField(
        max_digits=14, decimal_places=2, null=True, blank=True
    )
    observacoes = models.TextField(blank=True)

    class Meta:
        unique_together = ("numero_arp", "edital")

    def __str__(self):
        return f"ARP {self.numero_arp} - {self.fornecedor.razao_social}"


class ItemLicitado(models.Model):
    """
    Representa um item que foi licitado em um edital.
    Pode ter fornecedor, contrato e dados de quantidade e valor.
    """

    edital = models.ForeignKey(Edital, on_delete=models.CASCADE, related_name="itens")
    fornecedor = models.ForeignKey(
        Fornecedor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="itens",
    )
    contrato = models.ForeignKey(
        ARPContrato,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="itens",
    )

    codigo = models.CharField(max_length=50, blank=True)
    descricao = models.TextField()
    unidade = models.CharField(max_length=50, blank=True)
    quantidade = models.PositiveIntegerField(default=0)
    valor_unitario = models.DecimalField(
        max_digits=14, decimal_places=4, null=True, blank=True
    )
    valor_total = models.DecimalField(
        max_digits=14, decimal_places=2, null=True, blank=True
    )

    centro_custo = models.CharField(max_length=100, blank=True)
    proponente_codigo = models.CharField(max_length=20, blank=True)
    proponente_nome = models.CharField(max_length=255, blank=True)

    # Campo para upload de NF-e (XML ou PDF)
    arquivo_nf = models.FileField(
        upload_to="notas_fiscais/",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=["xml", "pdf"])],
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["codigo", "edital"], name="unique_codigo_por_edital"
            )
        ]

    def __str__(self):
        base = f"{self.codigo or ''} {self.descricao[:60]}"
        return base.strip()


class Clausula(models.Model):
    texto = models.TextField(unique=True)

    def __str__(self):
        return self.texto[:50] + ("..." if len(self.texto) > 50 else "")


class Feriado(models.Model):
    data = models.DateField(unique=True)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.descricao} ({self.data})"


# =========================
# NOVA ESTRUTURA
# =========================


class Empresa(models.Model):
    nome_empresa = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    telefone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    edital_vencedor = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.nome_empresa} ({self.cnpj})"


class Produto(models.Model):
    codigo_item = models.CharField(max_length=50, default="SEM-CODIGO")
    descricao = models.TextField()
    tipo_item = models.CharField(
        max_length=20,
        choices=[("MEDICAMENTO", "Medicamento"), ("ENFERMAGEM", "Enfermagem")],
    )
    edital_origem = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.codigo_item} - {self.descricao[:50]}"


class Pedido(models.Model):
    """
    Representa um pedido feito por uma empresa.
    """

    numero_pedido = models.CharField(max_length=50, unique=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    data_pedido = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[
            ("EM_ANDAMENTO", "Em andamento"),
            ("ATRASADO", "Atrasado"),
            ("CONCLUIDO", "Concluído"),
        ],
    )

    def __str__(self):
        return f"Pedido {self.numero_pedido} - {self.empresa.nome_empresa}"


class ItemDoPedido(models.Model):
    """
    Representa um item dentro de um pedido.
    """

    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade_solicitada = models.PositiveIntegerField()
    quantidade_entregue = models.PositiveIntegerField(default=0)
    status_entrega = models.CharField(
        max_length=20,
        choices=[
            ("PENDENTE", "Pendente"),
            ("ENTREGUE_PARCIAL", "Entregue Parcial"),
            ("CONCLUIDO", "Concluído"),
        ],
    )

    def __str__(self):
        return f"{self.produto.descricao[:40]} ({self.quantidade_solicitada})"


class Usuario(AbstractUser):
    """
    Modelo de usuário personalizado.
    Herdamos de AbstractUser para manter autenticação padrão do Django,
    mas adicionamos campos extras como nome completo, RG, cargo e setor.
    Também ajustamos os relacionamentos com grupos e permissões para evitar conflitos.
    """

    nome_completo = models.CharField(max_length=255)
    rg = models.CharField(max_length=20, blank=True)
    cargo = models.CharField(max_length=100, blank=True)
    setor = models.CharField(max_length=100, blank=True)

    # Evita conflitos com o modelo padrão de User do Django
    groups = models.ManyToManyField(
        Group,
        related_name="usuario_set",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="usuario_set",
        blank=True,
    )

    def __str__(self):
        return self.nome_completo or self.username


class Auditoria(models.Model):
    """
    Registra ações realizadas no sistema para fins de auditoria.
    Guarda quem fez, o que fez e quando fez.
    """

    data_hora = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    tipo_acao = models.CharField(max_length=100)
    detalhes = models.TextField()

    def __str__(self):
        return f"{self.tipo_acao} - {self.data_hora:%d/%m/%Y %H:%M}"


class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
