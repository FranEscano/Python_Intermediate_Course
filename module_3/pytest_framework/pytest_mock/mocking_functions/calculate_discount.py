def calculate_discount(price, discount_provider):
    discount = discount_provider.get_discount()
    return price - (price * discount / 100)