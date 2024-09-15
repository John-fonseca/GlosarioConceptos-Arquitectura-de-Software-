class Strategy:
    def execute(self, data):
        raise NotImplementedError

class ConcreteStrategyA(Strategy):
    def execute(self, data):
        print(f"Estrategia A con datos: {data}")

class ConcreteStrategyB(Strategy):
    def execute(self, data):
        print(f"Estrategia B con datos: {data}")

class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self, data):
        self._strategy.execute(data)

if __name__ == "__main__":
    context = Context(ConcreteStrategyA())
    context.execute_strategy("Ejemplo de datos A")

    context.set_strategy(ConcreteStrategyB())
    context.execute_strategy("Ejemplo de datos B")
