# app_principal/email_utils.py
import logging
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone

logger = logging.getLogger(__name__)


class EmailLog(models.Model):
    assunto = models.CharField(max_length=200)
    destinatarios = models.TextField()  # CSV de emails
    corpo = models.TextField()
    status = models.CharField(
        max_length=20, default="pendente"
    )  # pendente, enviado, erro
    tentativas = models.IntegerField(default=0)
    erro = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    enviado_em = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-criado_em"]


def send_mail_safe(assunto: str, corpo: str, destinatarios: list[str]) -> bool:
    """
    Envia e-mail e registra log. Em caso de falha, persiste para reprocesso.
    """
    log = EmailLog.objects.create(
        assunto=assunto,
        destinatarios=",".join(destinatarios),
        corpo=corpo,
        status="pendente",
        tentativas=0,
    )
    try:
        tentativas = log.tentativas + 1
        enviados = send_mail(
            subject=assunto,
            message=corpo,
            from_email=None,  # usa DEFAULT_FROM_EMAIL
            recipient_list=destinatarios,
            fail_silently=False,
        )
        if enviados > 0:
            log.status = "enviado"
            log.enviado_em = timezone.now()
            log.tentativas = tentativas
            log.save(update_fields=["status", "enviado_em", "tentativas"])
            return True
        else:
            raise RuntimeError("SMTP não retornou sucesso")
    except Exception as e:
        logger.exception("Falha ao enviar e-mail")
        log.status = "erro"
        log.erro = str(e)[:1000]
        log.tentativas = log.tentativas + 1
        log.save(update_fields=["status", "erro", "tentativas"])
        return False
