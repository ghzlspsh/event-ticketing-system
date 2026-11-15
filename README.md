# Event Ticketing System

A small console app I wrote in Python to practice OOP. You can create events, reserve tickets, buy them, and check your purchase history. There is also an admin menu to manage the events.

Everything runs in the terminal and nothing is saved to a file, so all data is gone when you close the program.

## How to run

You just need Python 3.

```
python event_ticketing.py
```

Then pick Login or Register from the menu.

## What it does

**As a user**
- register and log in
- see the list of events and the details of each one
- reserve tickets (the program checks the free seats)
- cancel a reservation and the seats go back to the event
- buy what you reserved and see the total price
- see your purchase history

**As admin**
- add, edit and delete events
- see the statistics (users, events, sold tickets, revenue)
- see the most popular event

An event that already has sold or reserved tickets can't be edited or deleted.

## Admin login

The admin is created in the code, near the bottom of the file:

```
admin1 = Admin('admin1', 'admin1', 'example@gmail.com', '123456789')
```

Log in with that email and password. Change them if you want your own.

## Rules for the inputs

- the email has to end with `@gmail.com`
- the password needs at least 8 characters
- the date format is `YYYY/MM/DD` and it can't be in the past
- capacity and price must be positive numbers
- the same username or email can't be registered twice

## What I used

Classes (`User`, `Admin`, `Event`, `Reservation`, `Buy`), inheritance (`Admin` inherits from `User`), properties with setters for validation, a static method, and `try/except` for bad inputs.

## Things I want to do next

- save the data in a JSON file or a database
- hash the passwords (right now they are stored as plain text)
- clean up the variable names and break the menus into smaller functions
