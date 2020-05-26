import pytest


SETUP = 0
TEARDOWN = 0


def setup():
    global SETUP
    SETUP += 1


def teardown():
    global TEARDOWN
    TEARDOWN += 1


class TestItWorks:
    def setup(self):
        if not getattr(self, 'count_setup', None):
            setattr(self, 'count_setup', 0)

        if not getattr(self, 'count_teardown', None):
            setattr(self, 'count_teardown', 0)

        self.value = True
        self.count_setup += 1

    def teardown(self):
        self.count_teardown += 1

    @pytest.mark.skip("You shall not pass")
    def test_it_really_works(self):
        assert self.value == False

    def test_count_setup(self):
        # This class is reinstantiated every test, so the counter is reset
        assert self.count_setup == 1

    def test_count_teardown(self):
        # This class is reinstantiated every test, so the counter is reset
        assert self.count_teardown == 0



def test_dict_compare():
    expected = {"fuzzy": "bear"}

    with pytest.raises(AssertionError):
        assert {"foo": "bar"} == expected


def test_setup():
    # One for each module-level test already called, including this one, but
    # not including the test class
    assert SETUP == 2


def test_teardown():
    # One for each module-level test already called, not including this, or the
    # test class
    assert TEARDOWN == 2
