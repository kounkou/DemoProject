import unittest

class DemoTest(unittest.TestCase):
    
    # Returns True or False
    def testTrue(self):
        self.assertTrue(True)

    # Returns True or False
    def testNumber(self):
        self.assertFalse(False)

if __name__ == '__main__':
    unittest.main()
