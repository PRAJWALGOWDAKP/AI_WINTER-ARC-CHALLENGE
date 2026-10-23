1. S — Single Responsibility Principle (SRP)
Definition: A class should have only one reason to change.

This means a class should focus on one specific responsibility rather than handling multiple unrelated tasks.

Example: In an employee management system, salary calculation, database storage, and email notifications are separate responsibilities. If all three are handled by one class, a change in any one area could affect the others.

The better design is to separate these responsibilities into different classes.

Why is SRP important?
- Makes code easier to understand and maintain.
- Reduces the impact of changes.
- Makes individual components easier to test.
- Improves separation of concerns.
Key point: One class can have multiple methods, provided they all contribute to the same responsibility.
2. O — Open/Closed Principle (OCP)
Definition: Software entities should be open for extension but closed for modification.

This means we should be able to introduce new functionality without repeatedly changing existing, working code.

Example: Consider an online shopping application that supports credit card payments. Later, the application needs to support UPI and digital wallets.

A poorly designed system might require changes to the same payment-processing logic every time a new payment method is introduced. A better design allows each new payment method to be added independently through a common interface.

Why is OCP important?
- Makes adding new features easier.
- Reduces the risk of breaking existing functionality.
- Improves flexibility and scalability.
- Supports maintainable software architecture.
Key point: Extend existing behavior through suitable abstractions instead of constantly modifying stable code.
3. L — Liskov Substitution Principle (LSP)
Definition: Objects of a subclass should be replaceable for objects of their parent class without breaking the expected behavior of the program.

In simple terms, a child class must honor the expectations established by its parent class.

Example: Consider a bird management system. A general bird abstraction might be designed around flying. However, penguins cannot fly.

If the system assumes every bird can fly, treating a penguin as an ordinary flying bird will cause incorrect behavior.

A better design separates the general concept of a bird from the capability of flying. Only birds that can fly should be treated as flying birds.

Why is LSP important?
- Prevents unexpected behavior in inheritance hierarchies.
- Improves reliability and correctness.
- Makes polymorphism work as intended.
- Encourages meaningful class relationships.
Key point: Inheritance should represent a valid behavioral relationship, not merely a similarity between two objects.
4. I — Interface Segregation Principle (ISP)
Definition: A class should not be forced to depend on methods it does not use.

This means interfaces should be small, focused, and specific to the needs of their users.

Example: Imagine a multifunction office machine that can print, scan, and fax. A basic printer only needs to print.

If every machine must implement printing, scanning, and faxing because they share one large interface, a basic printer is forced to support operations that are irrelevant to it.

A better design separates printing, scanning, and faxing into distinct capabilities. Each device implements only the capabilities it actually supports.

Why is ISP important?
- Avoids unnecessary dependencies.
- Reduces unnecessary implementation work.
- Makes components easier to maintain and test.
- Supports modular and flexible system design.
Key point: Prefer several small, focused interfaces over one large interface that attempts to serve every possible use case.
5. D — Dependency Inversion Principle (DIP)
Definition: High-level modules should not depend directly on low-level modules. Both should depend on abstractions.

Additionally, abstractions should not depend on implementation details; implementation details should depend on abstractions.

Let's understand the terminology:
- High-level module: Contains important business logic, such as processing an order.
- Low-level module: Performs technical operations, such as saving an order to a database or sending a notification.
- Abstraction: Defines what a component should do without specifying all the details of how it does it.
Example: An order-processing system needs to send notifications. If its business logic is tightly connected to one specific email provider, switching to SMS or another notification service may require changing the order-processing logic.

A better design makes the order-processing component depend on a general notification abstraction. Email, SMS, or push notifications can then provide their own implementations.

Why is DIP important?
- Reduces tight coupling between components.
- Makes replacing implementations easier.
- Improves testability through mock dependencies.
- Supports flexible application architecture.
- Makes external services easier to integrate or replace.