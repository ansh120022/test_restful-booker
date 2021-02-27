from model.booking import BookingData


class BookingApi:
    def __init__(self, client):
        self.client = client

    def create_booking(self, data: BookingData):
        data = data.object_to_dict()
        return self.client.s.post(self.client.url + "/booking", json=data)

    def update_booking(self, uid: int, data: BookingData):
        data = data.object_to_dict()
        return self.client.s.put(self.client.url + f"/booking/{uid}", json=data)

    def get_booking(self, uid: int):
        return self.client.s.get(self.client.url + f"/booking/{uid}")