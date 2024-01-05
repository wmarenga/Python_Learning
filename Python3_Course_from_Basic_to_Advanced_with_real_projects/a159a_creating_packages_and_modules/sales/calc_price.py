from sales.my_format import price


def increase(value, percentage, my_format=False):
    r = value + (value * (percentage / 100))

    if my_format:
        return price.real(r)
    else:
        return r


def reduction(value, percentage, my_format=False):
    r = value - (value * (percentage / 100))

    if my_format:
        return price.real(r)
    else:
        return r


def format_price(value):
    return f"R$ {value.replace('.', ',')}"
