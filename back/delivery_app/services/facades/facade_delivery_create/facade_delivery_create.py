from django.conf import settings

from delivery_app.services.utils.interfaces import FacadeInterface

LOGGER = settings.LOGGER


class FacadeDeliveryCreate(FacadeInterface):
    """Фасад для регистрации доставки"""

    pass
