from django.db import models
import uuid


class Wallet(models.Model):

    name = models.CharField('Name wallet', max_length=255)
    uuid = models.UUIDField('UUID wallet', default=uuid.uuid4, editable=False)
    balance = models.DecimalField('Balance wallet', max_digits=10, decimal_places=2, default=0, editable=False)

    class Meta:
        verbose_name = 'Wallet'
        verbose_name_plural = 'Wallets'

    def __str__(self) -> str:
        return f"{self.name} - {self.uuid}"