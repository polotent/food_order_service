def calc_total_price(items):
    """
    Calculates total price for list of menu items
    """
    total_price = 0
    for item in items:
        total_price += item.get('price') * item.get('quantity')
    return total_price
