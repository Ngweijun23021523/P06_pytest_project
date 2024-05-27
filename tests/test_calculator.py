from Calculator.calculator import Calculator
class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        c =2
        d =1
        cal = Calculator()

        # act
        result = cal.subtract(c, d)

        # assert
        expected = 1
        assert result == expected

    def test_multiply(self):
        e =2
        f =1
        cal = Calculator()

        # act
        result = cal.multiply(e, f)

        # assert
        expected = 2
        assert result == expected

    def test_divide(self):
        g =2
        h =1
        cal = Calculator()

        # act
        result = cal.divide(g, h)

        # assert
        expected = 2
        assert result == expected