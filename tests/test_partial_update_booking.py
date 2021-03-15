"""Частичное обновление запроса."""
from model.booking import BookingData

class TestUpdateBooking:
    def test_update_booking(self, client):
        """
        1. Создание бронирования
        2. Поиск его по фамилии клиента, чтобы узнать id
        3. Обновление фамилии по id
        4. Проверка, что новая фамилия сохранилась
        """
        data = BookingData().random()
        create_response = client.booking.create_booking(data)
        assert create_response.status_code == 200

        search_response = client.booking.get_booking_ids("lastname", data.lastname)
        assert search_response.status_code == 200
        booking: dict = search_response.json()
        booking_id = booking[0].get('bookingid')

        update_response = client.booking.update_booking_partial(booking_id, "lastname", "blah")
        assert update_response.status_code == 200

        search_response = client.booking.get_booking(booking_id).json()
        new_lastname = search_response.get('lastname')
        assert new_lastname == "blah"