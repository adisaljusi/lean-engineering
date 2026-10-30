"""Proposed customer lookup design. Review only."""
class Repository:
    def __init__(self, customers):
        self.customers = customers

    def get(self, customer_id):
        return self.customers.get(customer_id)


class Strategy:
    def __init__(self, repository):
        self.repository = repository

    def get(self, customer_id):
        return self.repository.get(customer_id)


class StrategyFactory:
    def __init__(self, strategy):
        self.strategy = strategy

    def get(self, customer_id):
        return self.strategy.get(customer_id)


class Manager(Strategy):
    pass


class Coordinator(Strategy):
    pass


class Facade(Strategy):
    pass


class Controller(Strategy):
    pass


def endpoint(customer_id, customers):
    return Controller(Facade(Coordinator(Manager(StrategyFactory(Strategy(Repository(customers))))))).get(customer_id)
