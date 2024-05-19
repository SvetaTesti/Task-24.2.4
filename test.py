import pytest

from app.calc import Calculator

class TestCalc:
    def setup_class(self):
        self.calc = Calculator

    def test_adding(self):
        assert self.calc.adding(self, 2, 1) == 3

    def test_adding_unsuccess(self):
        assert self.calc.adding(self, 1, 1) == 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self,1, 0)

    def test_adding(self):
        assert self.calc.subtraction(self, 5, 1) == 4

    def test_adding(self):
            assert self.calc.division(self, 8, 4) == 2

    def teardown_class(self):
        print('Выполнение метода Teardown')



    def test_adding(self):
        assert self.calc.multiply(self, 3, 7) == 21

