import json

import faker
fake = faker.Faker()


class _BookingDates:
    def __init__(self, checkin, checkout):
        self.checkin = checkin
        self.checkout = checkout


class BookingData:
    def __init__(self, firstname=None, lastname=None, totalprice=None,
                 depositpaid=None, checkin=None, checkout=None,
                 additionalneeds=None):
        self.firstname = firstname
        self.lastname = lastname
        self.totalprice = totalprice
        self.depositpaid = depositpaid
        self.bookingdates = _BookingDates(checkin, checkout)
        self.additionalneeds = additionalneeds

    def __eq__(self, other):
        return self.object_to_dict() == other

    @staticmethod
    def random():
        first_name = fake.first_name()
        last_name = fake.last_name()
        total_price = fake.pyint()
        deposit_paid = fake.pybool()
        additional_needs = fake.word()
        check_in = fake.iso8601()[:10]
        checkout = fake.iso8601()[:10]
        return BookingData(first_name, last_name, total_price,
                           deposit_paid, check_in, checkout, additional_needs)

    def object_to_dict(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))


class RandomDate:
    date_in_past = fake.past_date()
    date_in_future = fake.future_date()
