from django.conf import settings

from .facade_delivery_create import FacadeDeliveryCreate
LOGGER = settings.LOGGER


class FacadeDeliveryCreateYandex(FacadeDeliveryCreate):
    """Фасад для регистрации доставки | Яндекс"""

    pass
