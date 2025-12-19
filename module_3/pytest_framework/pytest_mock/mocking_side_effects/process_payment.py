def process_payment(payment_gateway, amount):
    response = payment_gateway(amount)
    if response == "Success":
        return "Payment processed successfully"
    else:
        raise ValueError("Payment failed")