from flask import Markup


def _round_and_format_number(number_format, value):
    value = value if value is not None else 0
    value = value if value < 1 else format(value, '.0f')
    return number_format.format(value)


def money_formatter(value):
    return _round_and_format_number('R${},00', value)


def square_meters_formatter(value):
    return _round_and_format_number('{}m²', value)


def liter_formatter(value):
    return _round_and_format_number('{}L', value)


def centimeters_formatter(value):
    return _round_and_format_number('{}cm', value)


def link_formatter(url, text):
    return Markup(
        "<a href='{}'> {} </a>".format(url, text)
    ) if url is not None else ' - '


def phone_formatter(value):
    return value[:4] + '-' + value[4:] if value is not None else '-'