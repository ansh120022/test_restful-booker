"""Проверка запроса на создание бронирования"""
from model.booking import BookingData
import pytest


class TestCreateBooking:
    def test_create_booking(self, client):
        """
        Отправка запроса 'create_booking' с рандомными валидными данными
        """
        data = BookingData().random()
        response = client.booking.create_booking(data)
        assert response.status_code == 200
        booking_info = response.json()
        assert booking_info.get('booking') == data

    @pytest.mark.parametrize('value',
                             [1, 0, True, False])
    def test_depositpaid(self, client, value):
        """Проверка допустимых значений параметра depositpaid"""
        data = BookingData().random()
        setattr(data, 'depositpaid', value)
        res = client.booking.create_booking(data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info.get('booking') == data

    @pytest.mark.parametrize("value",
                             [1, 1000, 1000000, 0, 1])
    def test_total_price(self, client, value):
        """Проверка допустимых значений параметра totalprice"""
        data = BookingData().random()
        setattr(data, 'totalprice', value)
        res = client.booking.create_booking(data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info.get('booking') == data