import datetime
from service.normalization import text_to_coordinate, text_to_date


def test_text_to_coordinate():
    result = text_to_coordinate("shanghai")
    assert result[0] == 31.222219
    assert result[1] == 121.458061


def test_text_to_date():
    result = text_to_date("tomorrow")

    today = datetime.datetime.now()
    one_more_day = datetime.timedelta(days=1)

    assert result == (today + one_more_day).date()
