"""Получение запроса по id."""


class TestGetBooking:
    def test_get_booking(self, client):
        """
        Запрос с id=1 всегда существует в системе, поэтому ищём его.
        """
        response = client.booking.get_booking(1)
        assert response.status_code == 200, "Запрос не найден"

    def test_get_unexisting_booking(self, client):
        """
        Поиск по несуществующему id
        """
        response = client.booking.get_booking("euhls")
        assert response.status_code == 404 and response.text == "Not Found"

