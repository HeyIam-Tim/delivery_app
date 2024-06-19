from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response

from .services.utils.delivery_handler import DeliveryPointsHandler
from .services.utils.delivery_calculator_handler import DeliveryCalculatorHandler
from .services.utils.delivery_cancel_handler import CancelDeliveryHandler
from .services.utils.delivery_create_handler import CreateDeliveryHandler
from .services.utils.delivery_intake_handler import IntakeDeliveryHandler
from .services.utils.delivery_return_handler import ReturnDeliveryHandler
from .services.utils.delivery_status_handler import StatusDeliveryHandler

LOGGER = settings.LOGGER


class DeliveryPoints(APIView):
    """Получение пунктов выдачи"""

    def post(self, request):
        delivery_data = request.data

        handler = DeliveryPointsHandler()

        delivery_points_data = handler.get_delivery_points(
            delivery_data=delivery_data,
        )

        return Response(delivery_points_data)


class Calculator(APIView):
    """Для расчета стоимости и сроков доставки"""

    def post(self, request):
        delivery_data = request.data

        handler = DeliveryCalculatorHandler()

        delivery_data_to_front = handler.calculate(
            delivery_data=delivery_data,
        )

        return Response(delivery_data_to_front)


class DeliveryCreate(APIView):
    """Регистрация заказа"""

    # request example
    # {
    #     "tariff_code": 22,
    #     "sender": {
    #         "company": "Компания Отправитель",
    #         "name": "Иванов Иван Иванович",
    #         "email": "sender@example.com",
    #         "phones": [
    #             {
    #                 "number": "+79161234567"
    #             }
    #         ]
    #     },
    #     "recipient": {
    #         "name": "Петров Петр Петрович",
    #         "phones": [
    #             {
    #                 "number": "+79217654321"
    #             }
    #         ]
    #     },
    #     "from_location": {
    #         "address": "г. Москва, ул. Примерная, д.10"
    #     },
    #     "to_location": {
    #         "address": "г. Санкт-Петербург, ул. Набережная, д.20"
    #     },
    #     "packages": [
    #         {
    #             "number": "1",
    #             "weight": 1000,
    #             "length": 10,
    #             "width": 10,
    #             "height": 10,
    #             "comment": "Картонная коробка",
    #             "items": [
    #                 {
    #                     "name": "Наименование товара",
    #                     "ware_key": "123456",
    #                     "payment": {
    #                         "value": 0
    #                     },
    #                     "cost": 500,
    #                     "weight": 500,
    #                     "amount": 2
    #                 }
    #             ]
    #         }
    #     ]
    # }

    def post(self, request):
        delivery_data = request.data

        handler = CreateDeliveryHandler()

        delivery_data_to_front = handler.create_delivery(
            delivery_data=delivery_data,
        )

        return Response(delivery_data_to_front)


class DeliveryStatus(APIView):
    """Получение статуса заказа"""

    # request example
    # {
    #    order_id: "72753034-b745-401a-aae6-b8395a94f349"
    # }

    def post(self, request):
        delivery_data = request.data

        handler = StatusDeliveryHandler()

        delivery_data_to_front = handler.delivery_status(
            delivery_data=delivery_data,
        )

        return Response(delivery_data_to_front)


class DeliveryCancel(APIView):
    """Отмена  заказа"""

    # request example
    # {
    #    order_id: "72753034-b745-401a-aae6-b8395a94f349"
    # }

    def post(self, request):
        delivery_data = request.data

        handler = CancelDeliveryHandler()

        delivery_data_to_front = handler.delivery_cancel(
            delivery_data=delivery_data,
        )

        return Response(delivery_data_to_front)


class DeliveryReturn(APIView):
    """Оформление возврата заказа"""

    # request example
    # {
    #     "tariff_code": 22,
    #     "sender": {
    #         "company": "Компания Отправитель",
    #         "name": "Иванов Иван Иванович",
    #         "email": "sender@example.com",
    #         "phones": [
    #             {
    #                 "number": "+79161234567"
    #             }
    #         ]
    #     },
    #     "recipient": {
    #         "name": "Петров Петр Петрович",
    #         "phones": [
    #             {
    #                 "number": "+79217654321"
    #             }
    #         ]
    #     },
    #     "from_location": {
    #         "address": "г. Москва, ул. Примерная, д.10"
    #     },
    #     "to_location": {
    #         "address": "г. Санкт-Петербург, ул. Набережная, д.20"
    #     },
    #     "packages": [
    #         {
    #             "number": "1",
    #             "weight": 1000,
    #             "length": 10,
    #             "width": 10,
    #             "height": 10,
    #             "comment": "Картонная коробка",
    #             "items": [
    #                 {
    #                     "name": "Наименование товара",
    #                     "ware_key": "123456",
    #                     "payment": {
    #                         "value": 0
    #                     },
    #                     "cost": 500,
    #                     "weight": 500,
    #                     "amount": 2
    #                 }
    #             ]
    #         }
    #     ]
    # }

    def post(self, request):
        delivery_data = request.data

        handler = ReturnDeliveryHandler()

        delivery_data_to_front = handler.delivery_return(
            delivery_data=delivery_data,
        )

        return Response(delivery_data_to_front)



class DeliveryIntake(APIView):
    """Оформление вызова курьера"""

    # request example
    # {
    #     "tariff_code": 22,
    #     "sender": {
    #         "company": "Компания Отправитель",
    #         "name": "Иванов Иван Иванович",
    #         "email": "sender@example.com",
    #         "phones": [
    #             {
    #                 "number": "+79161234567"
    #             }
    #         ]
    #     },
    #     "recipient": {
    #         "name": "Петров Петр Петрович",
    #         "phones": [
    #             {
    #                 "number": "+79217654321"
    #             }
    #         ]
    #     },
    #     "from_location": {
    #         "address": "г. Москва, ул. Примерная, д.10"
    #     },
    #     "to_location": {
    #         "address": "г. Санкт-Петербург, ул. Набережная, д.20"
    #     },
    #     "packages": [
    #         {
    #             "number": "1",
    #             "weight": 1000,
    #             "length": 10,
    #             "width": 10,
    #             "height": 10,
    #             "comment": "Картонная коробка",
    #             "items": [
    #                 {
    #                     "name": "Наименование товара",
    #                     "ware_key": "123456",
    #                     "payment": {
    #                         "value": 0
    #                     },
    #                     "cost": 500,
    #                     "weight": 500,
    #                     "amount": 2
    #                 }
    #             ]
    #         }
    #     ]
    # }

    def post(self, request):
        delivery_data = request.data

        handler = IntakeDeliveryHandler()

        delivery_data_to_front = handler.delivery_intake(
            delivery_data=delivery_data,
        )

        return Response(delivery_data_to_front)
