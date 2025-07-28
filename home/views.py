from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Project, Tag


from .models import Project, Tag

def index(request):
    projects = Project.objects.prefetch_related('images', 'tags').all()
    tags = Tag.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/#contact')
    else:
        form = ContactForm()

    return render(request, 'index.html', {
        'projects': projects,
        'tags': tags,
        'form': form,
    })


def project(request):
    projects = Project.objects.prefetch_related('images', 'tags').all()
    return render(request, 'project.html', {'projects': projects})
