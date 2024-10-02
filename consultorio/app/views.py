from os import rename

from django.shortcuts import render, redirect, get_object_or_404
from .forms import PacienteForm, MedicoForm, ConsultaForm
from .models import Paciente, Medico, Consulta


# Create your views here.

def home(request):
    return render(request, 'index.html')

def second(request):
    return render(request, 'second.html')

def createpac(request):
    form = PacienteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        paciente = form.save(commit=False)
        paciente.save()
        return redirect('/consultorio/readpac/')
    return render(request, 'createpac.html', {'form':form})

def createmed(request):
    form = MedicoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        medico = form.save(commit=False)
        medico.save()
        return redirect('/consultorio/readmed/')
    return render(request, 'createmed.html', {'form':form})

def createcons(request):
    form = ConsultaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        consulta = form.save(commit=False)
        consulta.save()
        return redirect('/consultorio/readcons/')
    return render(request, 'createcons.html', {'form':form})

def readpac(request):
    pacientes = Paciente.objects.all()
    return render(request, 'readpac.html', {'pacientes':pacientes})

def readmed(request):
    medicos = Medico.objects.all()
    return render(request, 'readmed.html', {'medicos':medicos})

def readcons(request):
    consultas = Consulta.objects.all()
    return render(request, 'readcons.html', {'consultas':consultas})

def updatepac(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    form = PacienteForm(request.POST or None, request.FILES or None, instance=paciente)
    if form.is_valid():
        paciente = form.save(commit=False)
        paciente.save()
        return redirect('/consultorio/readpac/')
    return render(request, 'createpac.html', {'form':form})

def updatemed(request, id):
    medico = get_object_or_404(Medico, pk=id)
    form = MedicoForm(request.POST or None, request.FILES or None, instance=medico)
    if form.is_valid():
        medico = form.save(commit=False)
        medico.save()
        return redirect('/consultorio/readmed/')
    return render(request, 'createmed.html', {'form':form})

def updatecons(request, id):
    consulta = get_object_or_404(Consulta, pk=id)
    form = ConsultaForm(request.POST or None, request.FILES or None, instance=consulta)
    if form.is_valid():
        consulta = form.save(commit=False)
        consulta.save()
        return redirect('/consultorio/readcons/')
    return render(request, 'createcons.html', {'form':form})

def deletepac(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    paciente.delete()
    return redirect('/consultorio/readpac/')

def deletemed(request, id):
    medico = get_object_or_404(Medico, pk=id)
    medico.delete()
    return redirect('/consultorio/readmed/')

def deletecons(request, id):
    consulta = get_object_or_404(Consulta, pk=id)
    consulta.delete()
    return redirect('/consultorio/readcons/')