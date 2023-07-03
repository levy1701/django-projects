from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Item
from .forms import NewItemForm


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)

    return render(request, 'item/detail.html', {
        'item': item
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Novo ativo',
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk,)
    item.delete()

    return redirect('core:index')