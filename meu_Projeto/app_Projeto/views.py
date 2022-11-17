from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib import messages
from .models import UsuarioModel
from .forms import UsuarioForm


# Create your views here.

@login_required
def index(request):
    return render(request, 'app_Projeto/index.html')


@login_required
def lista(request):
    search = request.GET.get('search')

    if search:
        usuario = UsuarioModel.objects.filter(nome__icontains=search, user=request.user)
    else:
        usuario_list = UsuarioModel.objects.all().order_by('-data_Nasc').filter(user=request.user)
        paginator = Paginator(usuario_list, 3)
        page = request.GET.get('page')
        usuario = paginator.get_page(page)
    return render(request, 'app_Projeto/lista.html', {'usuario': usuario})


@login_required
def usuario(request, id):
    usuario = get_object_or_404(UsuarioModel, pk=id)
    return render(request, 'app_Projeto/projeto.html', {'usuario': usuario})


@login_required
def novoUsuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            UsuarioModel.user = request.user
            usuario.save()
            return redirect('/')
    else:
        form = UsuarioForm()
        return render(request, 'app_Projeto/novo.html', {'form': form})


@login_required
def editUsuario(request, id):
    usuario = get_object_or_404(UsuarioModel, pk=id)
    form = UsuarioForm(instance=usuario)
    if (request.method == 'POST'):
        form = UsuarioForm(request.POST, instance=usuario)

        if (form.is_valid()):
            usuario.save()
            return redirect('/')
        else:
            return render(request, 'app_Projeto/edit.html', {'form': form, 'usuario': usuario})
    else:
        return render(request, 'app_Projeto/edit.html', {'form': form, 'usuario': usuario})


@login_required
def delUsuario(request, id):
    usuario = get_object_or_404(UsuarioModel, pk=id)
    usuario.delete()
    messages.info(request, 'Usuario deletado com sucesso')
    return redirect('/')
