from model.booking import BookingData
from common.logging import log


class BookingApi:
    def __init__(self, client):
        self.client = client

    @log("Get booking ids")
    def get_booking_ids(self, field: str, value: str):
        """Returns the ids of all the bookings that exist within the API"""
        response = self.client.request.get(self.client.url + '/booking/', params={field: value})
        return response

    @log("Get booking by id")
    def get_booking(self, uid: int):
        """Returns a specific booking based upon the booking id provided"""
        return self.client.request.get(self.client.url + f"/booking/{uid}")

    @log("Create booking")
    def create_booking(self, data: BookingData):
        """Creates a new booking in the API"""
        data = data.object_to_dict()
        return self.client.request.post(self.client.url + "/booking", json=data)

    @log("Update booking")
    def update_booking(self, uid: int, data: BookingData):
        """Updates a current booking"""
        data = data.object_to_dict()
        return self.client.request.put(self.client.url + f"/booking/{uid}", json=data)

    @log("Update booking partially")
    def update_booking_partial(self, uid, field: str, value: str,):
        """Updates current booking with a partial payload"""
        return self.client.request.patch(self.client.url + f"/booking/{uid}", json={field:
                                                                                           value})

    @log("Delete booking")
    def delete_booking(self, uid: int):
        """Returns the ids of all the bookings that exist within the API"""
        return self.client.request.delete(self.client.url + f"/booking/{uid}")

