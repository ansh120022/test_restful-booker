"""Проверка запроса на поиск бронирований по разным полям."""
from model.booking import AddBookingResponse, BookingData
import pytest

data = BookingData().random()


class TestGetBookingIds:

    @pytest.mark.parametrize(
        "field,value",
        [
            ("firstname", data.firstname),
            ("lastname", data.lastname),
            ("checkin", data.bookingdates.checkin),
            ("checkout", data.bookingdates.checkout),
        ],
    )
    def test_get_booking(self, client, field, value):
        """
        Создаём бронирование, затем ищем его по имени и фамилии клиента.
        """
        client.booking.create_booking(data, type_response=AddBookingResponse)
        request = client.booking.get_booking_ids(field, value)
        assert request.status_code == 200, "Созданный запрос не найден"

    @pytest.mark.parametrize(
        "field",
        [
            "firstname",
            "lastname",
        ],
    )
    def test_get_unexisting_booking(self, client, field):
        """
        Поиск несуществующего бронирования.
        """
        new_data = BookingData().random()
        response = client.booking.get_booking_ids(field, new_data.additionalneeds)
        assert response.status_code == 200
        assert response.json() == [], "Ожидалось пустое тело ответа"
