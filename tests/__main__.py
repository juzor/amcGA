import unittest

if __name__ == "__main__":
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover("tests")

    test_runner = unittest.runner.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)