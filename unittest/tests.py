import unittest
from activities import eat, nap, is_funny, laugh


class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        self.assertEqual(
            eat("broccoli", is_healthy = True),
            "I'm eating broccoli, because my body is a temple"
        )
    def test_eat_unhealthy(self):
        self.assertEqual(
            eat("pizza", is_healthy = False),
            "I'm eating pizza, because YOLO" #you only live once
        )
    
    def test_eat_healthy_boolean(self):
        """ is_healthy must be a bool"""
        with self.assertRaises(ValueError):
            eat('pizza', is_healthy="who cares?")

    def test_short_nap(self):
        self.assertEqual(
            nap(1),
            "I'm feeling refreshed after my 1 hour nap"
        )
    def test_long_nap(self):
        self.assertEqual(
            nap(3),
            "Ugh I overslept. I did not mean to nap for 3 hours",
            "Three hour must be overslept"
        )
    
    def test_is_funny_tim(self):
        self.assertFalse(is_funny("tim"))

    def test_is_funny_anyone_else(self):
        """ anyone except `tim` should be funny """
        self.assertTrue(is_funny("blue"), "blue should be funny")
        self.assertTrue(is_funny("tammy"), "tammpy should be funny")
        self.assertTrue(is_funny("john"), "tammpy should be funny")
        self.assertTrue(is_funny("sai"), "tammpy should be funny")

    def test_laugh(self):
        self.assertIn(laugh(), ('lol', 'haha', 'tehehe'))

if __name__ == '__main__': #make sure we are calling this file
    unittest.main()

#we can run with: python tests.py -v
        


