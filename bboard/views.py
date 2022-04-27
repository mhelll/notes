
from django.views.generic.edit import CreateView

from .models import Notes
from .forms import NotesForm

class SelfIndex(CreateView):
    template_name = 'index.html'
    form_class = NotesForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["notes"] = Notes.objects.all()
        return context