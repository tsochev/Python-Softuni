from collections import deque

pizza_orders = deque([int(x) for x in input().split(", ") if int(x) > 0])
employees_capacity = [int(x) for x in input().split(", ")]

total_pizza = 0

while pizza_orders and employees_capacity:
    pizza = pizza_orders.popleft()
    capacity = employees_capacity.pop()

    if pizza > 10:
        employees_capacity.append(capacity)
        continue

    if pizza <= capacity:
        total_pizza += pizza
    elif pizza > capacity:
        total_pizza += capacity
        pizza -= capacity
        pizza_orders.appendleft(pizza)

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza}")
    print(f"Employees: {', '.join([str(x) for x in employees_capacity])}")

if not employees_capacity and pizza_orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in pizza_orders])}")
