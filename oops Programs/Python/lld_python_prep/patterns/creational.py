from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> str: ...


class Email(Notification):
    def send(self, message: str) -> str: return f"email: {message}"


class SMS(Notification):
    def send(self, message: str) -> str: return f"sms: {message}"


class NotificationFactory:
    """Factory: construction is centralised; callers depend on Notification."""
    TYPES = {"email": Email, "sms": SMS}

    @classmethod
    def create(cls, kind: str) -> Notification:
        try:
            return cls.TYPES[kind.lower()]()
        except KeyError as exc:
            raise ValueError(f"unknown notification: {kind}") from exc


class DatabaseConnection:
    """Singleton: use sparingly; dependency injection is usually easier to test."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


if __name__ == "__main__":
    print(NotificationFactory.create("email").send("Hello"))
    print(DatabaseConnection() is DatabaseConnection())
