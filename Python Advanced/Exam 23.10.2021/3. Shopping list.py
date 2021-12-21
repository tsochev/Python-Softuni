def shopping_list(budget, **kwargs):
    products_basket = []
    basket = 0
    total_products = len(kwargs)
    curr_budget = budget
    if budget < 100:
        return "You do not have enough budget."

    for product, price_qty in kwargs.items():
        price = price_qty[0]
        qty = price_qty[1]
        total_price = price * qty
        if total_price < curr_budget:
            basket += 1
            curr_budget -= total_price
            products_basket.append(f"You bought {product} for {total_price:.2f} leva.")

        if basket >= 5:
            return "\n".join(products_basket)
        if basket == total_products:
            return "\n".join(products_basket)

    return "\n".join(products_basket)


print(shopping_list(100, microwave=(70, 2), skirts=(15, 4), coffee=(1.50, 10)))
print(shopping_list(20, jeans=(19.99, 1),))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2), juice=(2, 3),
                    eggs=(3, 1),
                    ))

