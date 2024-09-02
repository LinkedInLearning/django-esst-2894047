from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, ListView

from .models import Notes

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html" #no es necesario ya que se usa el nombre correcto notes_list 

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"

#def lissource env/bin/activatet(request):
 #   all_notes = Notes.objects.all()
  #  return render(request, 'notes/notes_list.html', {'notes': all_notes})

def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist")
    return render(request, 'notes/notes_detail.html', {'note': note})
