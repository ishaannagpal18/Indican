from django.db import models
from jsignature.fields import JSignatureField

class SignatureModel(models.Model):
    signature = JSignatureField()
