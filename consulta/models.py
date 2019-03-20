from django.db import models

class EmailAcademico(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    cpf = models.BigIntegerField(primary_key=True)

    class Meta():
        db_table = "email_academico"
        verbose_name_plural = "Emaisl acadêmicos"

    def __str__(self):
        return "{} ({})".format(self.email, self.nome)

    def __repr__(self):
        return str(self)



