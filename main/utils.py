from django.shortcuts import get_object_or_404, render
from .models import *


class DetailObjectMixin:
    model = None
    template = None

    def get(self, request):
        obj = get_object_or_404(self.model)
        return render(request, self.template, context={self.model.__name__.lower(): obj})
