# from django.conf import settings

# from celery import shared_task

# from ..facades.facade_delivery_point import FacadeDeliveryPoint


# LOGGER = settings.LOGGER


# @shared_task
# def create_delivery_points_task(delivery_points_data: dict) -> None:
#     """Добавляет пункты выдачи | задача"""

#     facade_delivery_point = FacadeDeliveryPoint()
#     facade_delivery_point.create_delivery_points(
#         delivery_points_data=delivery_points_data,
#     )

#     return None
