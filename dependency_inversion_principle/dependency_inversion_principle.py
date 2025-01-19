"""
The Dependency Inversion Principle states that high-level modules must not depend on low-level modules. 
Instead, both should depend on abstractions. This principle promotes decoupling, meaning concrete classes
are loosely coupled with high-level classes. To achieve this, classes should depend on interfaces or abstract classes,
not on concrete classes or functions
"""

# voildate dependency Inversion Principle:

class FileSession:
    def save(self, session_data):
        with open('session.txt', 'w') as file:
            file.write(session_data)
        print("Session saved to file.")

class RedisSession:
    def save(self, session_data):
        # Simulate saving session to Redis (using a mock)
        print("Session saved to Redis.")

class DatabaseSession:
    def save(self, session_data):
        # Simulate saving session to a database (using a mock)
        print("Session saved to Database.")

class User:
    def __init__(self, session_type):
        if session_type == "file":
            self.session = FileSession()  # Direct dependency on FileSession
        elif session_type == "redis":
            self.session = RedisSession()  # Direct dependency on RedisSession
        elif session_type == "database":
            self.session = DatabaseSession()  # Direct dependency on DatabaseSession

    def save_session(self, session_data):
        self.session.save(session_data)

# Usage
user = User("file")
user.save_session("User session data.")  # Session saved to file.

user = User("redis")
user.save_session("User session data.")  # Session saved to Redis.

# Correction of DIP
from abc import ABC, abstractmethod

# Abstraction layer (interface)
class SessionStorage(ABC):
    @abstractmethod
    def save(self, session_data):
        pass

# Concrete classes implementing the abstraction
class FileSession(SessionStorage):
    def save(self, session_data):
        with open('session.txt', 'w') as file:
            file.write(session_data)
        print("Session saved to file.")

class RedisSession(SessionStorage):
    def save(self, session_data):
        # Simulate saving session to Redis
        print("Session saved to Redis.")

class DatabaseSession(SessionStorage):
    def save(self, session_data):
        # Simulate saving session to a database
        print("Session saved to Database.")

# High-level module (User class)
class User:
    def __init__(self, session_storage: SessionStorage):
        self.session_storage = session_storage  # Now depends on abstraction

    def save_session(self, session_data):
        self.session_storage.save(session_data)

# Usage
file_session = FileSession()
user = User(file_session)
user.save_session("User session data.")  # Session saved to file.

redis_session = RedisSession()
user = User(redis_session)
user.save_session("User session data.")  # Session saved to Redis.

db_session = DatabaseSession()
user = User(db_session)
user.save_session("User session data.")  # Session saved to Database.


