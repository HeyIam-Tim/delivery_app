from rest_framework import serializers
# from ...models import DeliveryPoint
from delivery_app.models import DeliveryPoint


class DeliveryPointSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeliveryPoint

        fields = (
            'code',
            'uuid',
            'name',
            'address_comment',
            'nearest_station',
            'work_time',
            'phones',
            'email',
            'type',
            'owner_code',
            'take_only',
            'is_handout',
            'is_reception',
            'is_ltl',
            'have_cashless',
            'have_cash',
            'allowed_cod',
            'weight_min',
            'weight_max',
            'postamat_width',
            'postamat_height',
            'postamat_depth',
            'postal_code',
            'latitude',
            'longitude',
            'address',
            'address_full',
        )
