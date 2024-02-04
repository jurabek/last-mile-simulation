import random

import simpy


class Depot:
    def __init__(self, env, num_amrs):
        self.env = env
        self.amrs = [AMR(i, self) for i in range(num_amrs)]
        self.orders = simpy.PriorityStore(env)

    # Method to accept and prioritize orders
    def accept_order(self, order):
        priority = order.priority
        self.orders.put((priority, order))


def calculate_travel_time():
    # Return a simulated travel time. Here we just return a random number for simplicity
    return random.randint(20, 60)  # Simulate travel time between 20 to 60 minutes


class AMR:
    def __init__(self, id, depot):
        self.id = id
        self.depot = depot
        self.capacity = 5  # Set based on input
        self.load = 0

    # Method to load and deliver orders
    def manage_orders(self):
        while True:
            if self.load < self.capacity:
                # Wait for an order to be available
                priority, order = yield self.depot.orders.get()
                print(f'AMR #{self.id} has started processing order #{order.id} at time {self.depot.env.now}')
                # Simulate loading time
                yield self.depot.env.timeout(10)  # Assuming 10 minutes loading time
                self.load += 1  # Assuming each order takes 1 unit of capacity
                print(f'AMR #{self.id} has loaded order #{order.id} at time {self.depot.env.now}')

                # Check if the AMR is full or if the order is high priority to leave immediately
                if self.load == self.capacity or order.priority == 1:
                    yield self.depot.env.timeout(calculate_travel_time())  # Simulate travel time
                    self.load = 0  # Reset load after delivery
                    print(
                        f'AMR #{self.id} has delivered order #{order.id} and returned to depot at time {self.depot.env.now}')
                else:
                    # Wait for more orders for up to 1 hour if not full
                    yield self.depot.env.timeout(60)  # Waiting for more orders
                    if self.load > 0:  # Check if any orders were picked up during waiting
                        yield self.depot.env.timeout(calculate_travel_time())  # Simulate travel time
                        self.load = 0  # Reset load after delivery
                        print(f'AMR #{self.id} has delivered orders and returned to depot at time {self.depot.env.now}')
            else:
                # If for some reason the load is over capacity, reset
                self.load = 0


class Order:
    def __init__(self, id, category, priority, customer_id):
        self.id = id
        self.category = category
        self.priority = priority
        self.customer_id = customer_id


def place_orders(env, depot, num_customers):
    order_types = [("groceries", 1), ("pharmaceutics", 1), ("flowers", 2), ("electronics", 3), ("clothes", 4),
                   ("organic waste", 1), ("residual waste", 2),
                   ("other waste", 3)]  # Define all order types and priorities
    for i in range(num_customers):
        # Generate orders for customers
        order_type, priority = random.choice(order_types)
        order = Order(i, order_type, priority, i)
        depot.accept_order(order)
        yield env.timeout(random.randint(1, 10))  # Random time between orders


def simulation(env, num_amrs, num_customers):
    depot = Depot(env, num_amrs)
    env.process(place_orders(env, depot, num_customers))
    # Start AMRs to manage orders
    for amr in depot.amrs:
        env.process(amr.manage_orders())
    env.run(until=300)  # Run simulation for 300 time units


env = simpy.Environment()

simulation(env, num_amrs=3, num_customers=10)
