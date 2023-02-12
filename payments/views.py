from __future__ import annotations

import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import DetailView

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class SessionCreateView(DetailView):
    def get(self, request, *args, **kwargs):
        try:
            item = self.get_object()
        except Item.DoesNotExist:
            return JsonResponse({'error': 'Not found'}, status=404)

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'inr',
                        'product_data': {
                            'name': f'{item.name}',
                        },
                        'unit_amount': item.get_price,
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
        return JsonResponse({'id': session.id})
