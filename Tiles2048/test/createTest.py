import unittest
import hashlib
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
            self.assertEqual(2, two_count, "initial grid with wrong count of \'2\' :" + str(two_count))


    def test_create_output_Should_valid(self):
        test_time = 100
        userParms = {'op': 'create'}
        myHash = hashlib.sha256()
        for i in range(test_time):
            result = create._create(userParms)
            # score should be 0
            self.assertEqual(0, result['score'], 'score should be 0, current: '+str(result['score']))
            # status should be ok
            self.assertEqual('ok', result['status'], 'status should be ok, current: '+str(result['status']))
            # integrity should be valid
            myHash.update(result['grid'].encode())
            integrity = myHash.hexdigest().upper()
            self.assertEqual(integrity, result['integrity'], 'integrity should be same')
