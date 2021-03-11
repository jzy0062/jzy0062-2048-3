import unittest
import Tiles2048.create as create

class CreateTest(unittest.TestCase):

    #  The following is included only for illustrative purposes.  It tests nothing
    #  useful.  Please delete and replace with your own test code.
    def test_create_HappyPathTest010(self):
        userParms = {'op': 'create', 'size': '4'}
        actualResult = create._create(userParms)
        self.assertIsNotNone(actualResult)

    def test_init_loc_Should_different(self):
        test_times = 1000
        for i in range(test_times):
            loc1, loc2 = create.generate_init_loc()
            self.assertNotEqual(loc1, loc2, "initial location is same value: " + str(loc1))
            self.assertTrue(loc1 >= 0, "initial location out of range")
            self.assertTrue(loc2 >= 0, "initial location out of range")
            self.assertTrue(loc1 <= 15, "initial location out of range")
            self.assertTrue(loc2 <= 15, "initial location out of range")

    def test_init_grid_Should_valid(self):
        test_times = 1000
        for i in range(test_times):
            grid = create.generate_init_grid()
            self.assertEqual(16, len(grid), "initial grid invalid, len:" + str(grid))
            two_count = 0
            for ch in grid:
                if ch == '2':
                    two_count += 1
                else:
                    self.assertEqual('0', ch, "invalid character in grid :" + ch)



