"""Получение запроса по id."""
from model.booking import AddBookingResponse, BookingData


class TestGetBooking:
    def test_get_booking(self, client):
        """
        1. Создаём запрос
        2. Узнаём его id
        3. Ищем по id
        """

        data = BookingData().random()
        create_response = client.booking.create_booking(data, type_response=AddBookingResponse)
        assert create_response.status_code == 200

        search_response = client.booking.get_booking_ids("lastname", data.lastname)
        assert search_response.status_code == 200
        booking: dict = search_response.json()
        booking_id = booking[0].get('bookingid')

        response = client.booking.get_booking(booking_id)
        assert response.status_code == 200, "Запрос не найден"

    def test_get_unexisting_booking(self, client):
        """
        Поиск по несуществующему id
        """
        response = client.booking.get_booking("euhls")
        assert response.status_code == 404 and response.text == "Not Found"

