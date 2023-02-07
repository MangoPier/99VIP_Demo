import pytest


class TestDemo():
    def test_add(self):
        c = 1+1
        assert c == 2

    @pytest.mark.smoke
    def test_demo02(self):
        msg = "i love u"
        assert "o" in msg

    @pytest.mark.skip
    def test_demo03(self):
        msg = "i love u"
        assert "oh" in msg

    def test_demo04(self):
        msg = "i love u"
        assert "oh" not in msg
