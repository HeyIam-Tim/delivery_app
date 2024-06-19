from django.conf import settings

from delivery_app.services.utils.interfaces import FacadeInterface

LOGGER = settings.LOGGER


class FacadeDeliveryCalculatorYandex(FacadeInterface):
    """Фасад для калькуляции ЯНДЕКС"""

    pass
