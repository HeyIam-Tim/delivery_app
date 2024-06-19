from django.conf import settings

from delivery_app.services.utils.interfaces import FacadeInterface

LOGGER = settings.LOGGER


class FacadeDeliveryReturnCdek(FacadeInterface):
    """Фасад для возврата заказа"""

    pass
