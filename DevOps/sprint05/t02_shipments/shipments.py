






class Cargo:
    def __init__(self, destination, weight):
        self.destination = destination
        self.weight = weight

class Container:
    def __init__(self, cargo=None, weight_limit=None):
        self.weight_limit = weight_limit
        self.cargo = cargo

    def set_cargo(self, cargo):
        if self.weight_limit >= cargo.weight:
            self.cargo = cargo


class Ship:
    def __init__(self, route, containers):
        self.route = route
        self.containers = containers

    def add_containers():