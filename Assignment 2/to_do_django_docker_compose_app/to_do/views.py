from django.shortcuts import get_object_or_404, redirect, render

from to_do.models import ToDoItem

# Create your views here.
def to_do_list(request):
    items = ToDoItem.objects.all()
    return render(request, 'to_do_list.html', {'items': items})

def add_to_do_item(request):
    text = request.POST['text']
    ToDoItem.objects.create(text=text)
    return redirect('to_do_list')

def toggle_to_do_completed(_, item_id):
    item = get_object_or_404(ToDoItem, id=item_id)
    item.completed = not item.completed
    item.save()
    return redirect('to_do_list')

def delete_to_do_item(_, item_id):
    item = get_object_or_404(ToDoItem, id=item_id)
    item.delete()
    return redirect('to_do_list')