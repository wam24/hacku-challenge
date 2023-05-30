from django.urls import reverse_lazy
from django.views.generic import CreateView
from ..models import Person
from ..forms import PersonForm

__all__ = ['PersonCreateView']


class PersonCreateView(CreateView):
    template_name = "register/base-form.html"
    model = Person
    queryset = Person.objects.all()
    form_class = PersonForm
    success_url = reverse_lazy('register:person-create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.queryset.values_list('pk', flat=True))
        context['persons'] = self.queryset.order_by('-pk')
        return context

    def form_invalid(self, form):
        print(form.errors)
        # Agrega lógica adicional si es necesario
        return self.render_to_response(self.get_context_data(form=form))
