# pytest project
def func(x):
    return x+1

# test 1 and 3 pass and 2 will failed
# def test_1():
#     assert func(3) == 4
#
# def test_2():
#     assert func(4) == 6
#
# def test_3():
#     assert func(5) == 6

class TestCases: # this below fun is part of class if we run it failed we have to pass parameter self used bydefault in python
    def test_1(self):
        assert func(3) == 4

    def test_2(self):
        assert func(4) == 6

    def test_3(self):
        assert func(5) == 6
        # export the html test report