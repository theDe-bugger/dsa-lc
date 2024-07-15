# implement limit order book
# buy only when price goes below limit, or sell at least when limit price
# keep track of outstanding orders

from enum import Enum
from heapq import heappop, heappush
# order is a type, amount/quantity of stock, and limit price
class order_type(Enum):
    BUY = 'buy'
    SELL = 'sell'

class order():
    def __init__(self, amount, type, price):
        self.amount = amount
        self.type = type
        self.price = price
    def __eq__(self, other):
        return self.price == other.price
    def __lt__(self,other):
        return self.price < other.price
    def __repr__(self):
        return f"Order of {self.amount} stocks of limit {self.price * -1 if self.type == order_type.SELL else self.price} of type {'sell' if self.type == order_type.SELL else 'buy'}"
    
class limit_order_book():
    def __init__(self,):
        self.buy_orders = []
        self.sell_orders = []
        
    def place_order(self, order):
        if order.type == order_type.BUY:
            # check sell orders
            while self.sell_orders and order.amount:
                lowest_price_order = heappop(self.sell_orders)
                if lowest_price_order.price <= order.price:
                    difference_in_amount = lowest_price_order.amount - order.amount
                    if difference_in_amount > 0:
                        lowest_price_order.amount = difference_in_amount
                        order.amount = 0
                        heappush(self.sell_orders,lowest_price_order)
                    else:
                        lowest_price_order.amount = 0
                        order.amount = -difference_in_amount
                else:
                    heappush(self.sell_orders, lowest_price_order)   
                    break  
            # update buy orders
            if order.amount: heappush(self.buy_orders, order)
        else:
            # check buy orders
            while self.buy_orders and order.amount:
                highest_price_buy_order = heappop(self.buy_orders)
                if highest_price_buy_order.price >= order.price:
                    difference_in_amount = highest_price_buy_order.amount - order.amount
                    if difference_in_amount > 0:
                        highest_price_buy_order.amount = difference_in_amount
                        order.amount = 0
                        heappush(self.buy_orders, highest_price_buy_order)
                    else:
                        highest_price_buy_order.amount = 0
                        order.amount = -difference_in_amount
                else:
                    heappush(self.buy_orders,highest_price_buy_order)
                    break    
            # update sell orders
            if order.amount: heappush(self.sell_orders, order)
        print(list(self.buy_orders))
        print(list(self.sell_orders))
        print('')
            

# # order 1: 10, buy, 150
lob = limit_order_book()
o1 = order(10,order_type.BUY,150)
lob.place_order(o1)
# (order1)


# # order 2: 5, sell, 140

o2 = order(5,order_type.SELL,140)
lob.place_order(o2)

# (order1: 5, buy, 150)


# # order 3: 10, buy, 100
o3 = order(10,order_type.BUY,100)
lob.place_order(o3)


# (order1, order3)

# # order 4: 5, sell, 110
print("selling starts here")
o4 = order(5,order_type.SELL,200)
lob.place_order(o4)

# (order3)
o5 = order(16,order_type.SELL,50)
lob.place_order(o5)

