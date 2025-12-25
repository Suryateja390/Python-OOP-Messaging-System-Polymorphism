# Python OOP - Messaging System (Polymorphism & Inheritance)

This project demonstrates how **Polymorphism** and **Inheritance** work in Python using a simple messaging system example.

---

## 🧠 Concepts Covered
- Object-Oriented Programming (OOP)
- Inheritance
- Method Overriding
- Polymorphism
- Class and Object interaction

---

## 📱 Project Overview

A base class `Messenger` defines general messaging behavior.  
Different messaging platforms extend this class and provide their own implementations:

- `FMessage` → Facebook  
- `WMessage` → WhatsApp  
- `IMessage` → Instagram

The `Display` class demonstrates **polymorphism** by interacting with different message objects using a common interface.

---

## 🧾 Program Features

- Send and receive messages
- Platform-specific behavior
- Special feature for Instagram (Live Location sharing)
- Same function call, different behavior

