from django.conf import settings

from .facade_delivery_create import FacadeDeliveryCreate
LOGGER = settings.LOGGER


class FacadeDeliveryCreateCdek(FacadeDeliveryCreate):
    """Фасад для регистрации доставки | СДЕК"""

    pass
