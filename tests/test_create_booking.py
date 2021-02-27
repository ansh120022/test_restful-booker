from model.booking import BookingData, RandomDate
import pytest


class TestBooking:

    def test_get_booking(self, client, create_booking):
        """
           1. Add new booking
           2. Get created booking by id
           3. Check data and status
           4. Validate schema
        """
        id_booking = create_booking.get('bookingid')
        res = client.get_booking(id_booking)
        assert res.json() == create_booking.get('booking')


class TestCreateBookingPositive:
    def test_create_booking(self, client):
        """
        Отправка запроса 'create_booking' с валидными данными
        """
        data = BookingData().random()
        res = client.create_booking(data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info.get('booking') == data

    @pytest.mark.parametrize('value', [1, 0, True, False])
    def test_depositpaid(self, client, value):
        data = BookingData().random()
        setattr(data, 'depositpaid', value)
        res = client.create_booking(data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info.get('booking') == data

    @pytest.mark.parametrize("value",
                             [1, 1000, 1000000, 0, 1])
    def test_total_price(self, client, value):
        data = BookingData().random()
        setattr(data, 'totalprice', value)
        res = client.create_booking(data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info.get('booking') == data


class TestCreateBookingNegative:
    @pytest.mark.parametrize("field, value", [
        ['blah', 12],
        ['blah', 56],
        ['blah-blah', 45]
    ])
    def test_customer_data(self, field, value, client):
        """
        Невалидные данные клиента
        """
        data = BookingData().random()
        setattr(data, field, value)
        res = client.create_booking(data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info.get('booking') == data

    def test_dates(self, client):
        """
        Даты бронирования в прошлом
        """
        data = BookingData().random()
        data.bookingdates.checkin = RandomDate.date_in_past
        data.bookingdates.checkout = RandomDate.date_in_past
        res = client.create_booking(data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info.get('booking') != data

    @pytest.mark.parametrize("value",
                             [0.15, 10000000000000000000000000, 'String'])
    def test_total_price(self, client, value):
        data = BookingData().random()
        setattr(data, 'totalprice', value)
        res = client.create_booking(data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info.get('booking') != data

    @pytest.mark.parametrize('value', [-1, 'string', 'True'])
    def test_depositpaid(self, client, value):
        data = BookingData().random()
        setattr(data, 'depositpaid', value)
        res = client.create_booking(data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info.get('booking') != data
