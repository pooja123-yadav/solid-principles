"""
https://realpython.com/solid-principles-python/

Clients should not be forced to depend upon methods that they do not use. Interfaces belong to clients,
 not to hierarchies.

In this case, clients are classes and subclasses, and interfaces consist of methods and attributes.
In other words, if a class doesn’t use particular methods or attributes, then those methods and attributes 
should be segregated into more specific classes.

"""

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

    def fax(self, document):
        raise NotImplementedError("Fax functionality not supported")

    def scan(self, document):
        raise NotImplementedError("Scan functionality not supported")

class ModernPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")
