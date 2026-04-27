from collections import deque
from unittest import TestCase , main

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self):
        self.station = RailwayStation("Central")

    def test_init(self):
        self.assertEqual("Central" , self.station.name)
        self.assertIsInstance(self.station.arrival_trains , deque)
        self.assertIsInstance(self.station.departure_trains, deque)

    def test_name_length_positive(self):
        self.assertEqual("Central", self.station.name)

    def test_name_length_smaller_than_three(self):
        with self.assertRaises(ValueError) as ex:
            self.station.name = "C"
        self.assertEqual(str(ex.exception), "Name should be more than 3 symbols!")

    def  test_name_length_equal_to_three(self):
        with self.assertRaises(ValueError) as ex:
            self.station.name = "Cen"
        self.assertEqual(str(ex.exception), "Name should be more than 3 symbols!")

    def test_new_arrival_on_board_adds_train_info(self):


        self.station.new_arrival_on_board("Train 101")

        self.assertEqual(len(self.station.arrival_trains), 1)
        self.assertEqual(self.station.arrival_trains[0], "Train 101")

    def test_no_trains_in_deq(self):
        self.station.arrival_trains = deque()
        train_info = "trainA"

        with self.assertRaises(IndexError):
            self.station.train_has_arrived(train_info)

    def test_train_first_in_deq(self):
        self.station.arrival_trains = deque(["trainA","trainB"])
        train_info = "trainA"
        result = self.station.train_has_arrived(train_info)
        self.assertEqual(result,"trainA is on the platform and will leave in 5 minutes." )
        self.assertEqual(len(self.station.departure_trains), 1)
        self.assertEqual(self.station.departure_trains[0], "trainA")
        self.assertEqual(len(self.station.arrival_trains), 1)

    def test_train_is_not_first(self):
        self.station.arrival_trains = deque(["trainB", "trainA"])
        train_info = "trainA"
        result = self.station.train_has_arrived(train_info)
        self.assertEqual(result,"There are other trains to arrive before trainA.")
        self.assertEqual(len(self.station.departure_trains),0)
        self.assertEqual(len(self.station.arrival_trains),2)

    def test_train_left_station(self):
        self.station.departure_trains = deque(["trainA", "trainB"])
        train_info = "trainA"
        result = self.station.train_has_left(train_info)
        self.assertEqual(self.station.departure_trains[0], "trainB")
        self.assertEqual(result , True)
        self.assertEqual(len(self.station.departure_trains),1)

    def test_train_has_not_left(self):
        self.station.departure_trains = deque(["trainC", "trainA"])
        train_info = "trainA"
        result = self.station.train_has_left(train_info)
        self.assertEqual(result, False)
        self.assertEqual(len(self.station.departure_trains), 2)


if __name__ == '__main__':
    main()