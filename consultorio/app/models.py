from django.db import models

# Create your models here.

class Paciente(models.Model):
    nome = models.CharField(max_length=30)
    nascimento = models.DateField()
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=20)
    cep = models.CharField(max_length=9)
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=30)
    plano = models.CharField(max_length=20)

    def __str__(self):
        return self.cpf + " - " + self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=30)
    nascimento = models.DateField()
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=20)
    cep = models.CharField(max_length=9)
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=30)
    crm = models.CharField(max_length=10)

    def __str__(self):
        return self.crm + " - " + self.nome

class Consulta(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, blank=True, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=True, null=True)
    prontuario = models.CharField(max_length=500)

    def __str__(self):
        return str(self.data) + " " + str(self.hora)