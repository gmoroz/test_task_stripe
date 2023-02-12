from __future__ import annotations

from django.urls import path
from django.views.generic import TemplateView

from . import views
from .models import Item

urlpatterns = [
    path('buy/<int:pk>', views.SessionCreateView.as_view(), name='checkout'),
    path('cancel/', TemplateView.as_view(template_name='cancel.html'), name='cancel'),
    path(
        'success/',
        TemplateView.as_view(
            template_name='success.html',
        ),
        name='success',
    ),
    path(
        '',
        TemplateView.as_view(
            template_name='items.html',
            extra_context={'items': Item.objects.all()},
        ),
        name='items',
    ),
    path(
        'item/<int:pk>',
        views.ItemDetailView.as_view(),
        name='item',
    ),
]
