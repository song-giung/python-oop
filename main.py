class Item:
    pay_rate = 0.8

    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0
        assert quantity >= 0, f"Quantity must be grater than 0 but {quantity}"

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        # self.pay_rate vs Item.pay_rate
        # sel_pay_rate로 선언할 경우 인스턴스 별로 pay_rate를 다르게 설정할 수 가 있다.
        self.price = self.price * self.pay_rate # instance level => class level 로 찾는다.


item1 = Item("Phone", 100, 0)
item1.apply_discount()
print(item1.price)

item2 = Item("Laptop", 1000, 0)
item2.pay_rate = 0.7 # 인스턴스 멤버를 추가한 것이지 class attribute를 변경한 것이 아니다.
item2.apply_discount()
print(item2.price)

