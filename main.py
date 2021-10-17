class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # validate received arguments
        # can raise AssertionError
        assert price >= 0
        assert quantity >= 0, f"Quantity must be grater than 0 but {quantity}"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Phone", 100, -1)
# 다이나믹, 스크립팅 언어 객체를 생성한 이후에 필드를 추가할 수 있다.
item1.has_num_pad = False
print(item1.calculate_total_price())

# __method__ : magic method
# __init__ : 생성자 함수
# 생성자 함수에 기본 값을 설정하면 강제가 아니게 된다.
