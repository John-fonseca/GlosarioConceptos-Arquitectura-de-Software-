class Subject:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        raise NotImplementedError

class ConcreteObserver(Observer):
    def update(self, message):
        print(f"Observador notificado: {message}")

if __name__ == "__main__":
    subject = Subject()
    observer1 = ConcreteObserver()
    observer2 = ConcreteObserver()

    subject.register_observer(observer1)
    subject.register_observer(observer2)

    subject.notify_observers("Estado ha cambiado.")
