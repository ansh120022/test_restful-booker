"""Удаление бронирования."""
from model.booking import BookingData

class TestDeleteBooking:
    def test_update_booking(self, client):
        """
        1. Создание бронирования
        2. Получение его id
        3. Удаление бронирования по id
        4. Попытка найти удалённую запись
        """
        data = BookingData().random()
        create_response = client.booking.create_booking(data)
        assert create_response.status_code == 200

        search_response = client.booking.get_booking_ids("lastname", data.lastname)
        assert search_response.status_code == 200
        booking: dict = search_response.json()
        booking_id = booking[0].get('bookingid')

        delete_response = client.booking.delete_booking(booking_id)
        assert delete_response.status_code == 201

        search_response = client.booking.get_booking(booking_id)
        assert search_response.status_code == 404