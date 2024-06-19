from django.conf import settings

from delivery_app.services.utils.interfaces import FacadeInterface

LOGGER = settings.LOGGER


class FacadeDeliveryIntakeCdek(FacadeInterface):
    """Фасад для вызова курьера"""

    pass
