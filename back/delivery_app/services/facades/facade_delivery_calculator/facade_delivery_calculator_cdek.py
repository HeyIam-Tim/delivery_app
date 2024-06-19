from django.conf import settings

from delivery_app.services.facades.facade_base_delivery import FacadeBaseDeliveryCdek

from delivery_app.services.utils.interfaces import FacadeInterface

LOGGER = settings.LOGGER


class FacadeDeliveryCalculatorCdek(FacadeInterface, FacadeBaseDeliveryCdek):
    """Фасад для калькуляции СДЕК"""

    pass
