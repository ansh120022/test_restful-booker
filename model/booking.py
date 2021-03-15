import json
from common.base import BaseClass

import attr
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
        additional_needs = f"{fake.word()}{fake.random.randint(796,98876)}"
        check_in = fake.iso8601()[:10]
        checkout = fake.iso8601()[:10]
        return BookingData(first_name, last_name, total_price,
                           deposit_paid, check_in, checkout, additional_needs)

    def object_to_dict(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))


class RandomDate:
    date_in_past = fake.past_date()
    date_in_future = fake.future_date()


@attr.s
class BookingDates:
    checkin: str = attr.ib(default=None)
    checkout: str = attr.ib(default=None)

@attr.s
class BookingDataAttr(BaseClass):
    firstname: str = attr.ib(default=None)
    lastname: str = attr.ib(default=None)
    totalprice: int = attr.ib(default=None)
    depositpaid: bool = attr.ib(default=None)
    bookingdates: BookingDates = attr.ib(default=None)
    additionalneeds: str = attr.ib(default=None)

    @staticmethod
    def random():
        fake = faker.Faker()
        first_name = fake.first_name()
        last_name = fake.last_name()
        total_price = fake.pyint()
        deposit_paid = fake.pybool()
        additional_needs = fake.word()
        check_in = fake.iso8601()[:10]
        checkout = fake.iso8601()[:10]
        return BookingDataAttr(first_name, last_name, total_price,
                           deposit_paid, BookingDates(check_in, checkout), additional_needs)


@attr.s
class AddBookingResponse:
    bookingid: int = attr.ib()
    booking: BookingDataAttr = attr.ib()
