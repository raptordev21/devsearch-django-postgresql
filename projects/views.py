from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects': projects})


def project(request, id):
    project = Project.objects.get(id=id)
    return render(request, 'projects/single-project.html', {'project': project})


def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def updateProject(request, id):
    project = Project.objects.get(id=id)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def deleteProject(request, id):
    project = Project.objects.get(id=id)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_confirm.html', context)
