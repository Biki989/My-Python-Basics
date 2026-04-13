from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return f"Processed credit card payment of ${amount}" 

def make_payment(payment_method, amount):
    print(payment_method.process_payment(amount))

credit_card_payment = CreditCardPayment()
make_payment(credit_card_payment, 100) # Processed credit card payment of $100