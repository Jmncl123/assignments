from colorama import Fore, Style, init
init(autoreset=True)

class Event:
    def __init__(self, event_id, name, date, capacity):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.capacity = capacity
        self.tickets_sold = 0

    def has_tickets(self):
        return self.tickets_sold < self.capacity

    def sell_ticket(self):
        if self.has_tickets():
            self.tickets_sold += 1
            return True
        return False

    def available_tickets(self):
        return self.capacity - self.tickets_sold

class Attendee:
    def __init__(self, attendee_id, name, email):
        self.attendee_id = attendee_id
        self.name = name
        self.email = email
        self.tickets = []

    def add_ticket(self, event_id):
        self.tickets.append(event_id)

class TicketTransaction:
    def __init__(self, event_id, attendee_id):
        self.event_id = event_id
        self.attendee_id = attendee_id

class EventManager:
    def __init__(self):
        self.events = {}
        self.attendees = {}
        self.transactions = []

    def add_event(self, event_id, name, date, capacity):
        if event_id in self.events:
            print(Fore.RED + f"Event ID '{event_id}' already exists.")
            return
        self.events[event_id] = Event(event_id, name, date, capacity)
        print(Fore.GREEN + f"Event '{name}' added successfully!")

    def register_attendee(self, attendee_id, name, email):
        if attendee_id in self.attendees:
            print(Fore.RED + f"Attendee ID '{attendee_id}' already registered.")
            return
        self.attendees[attendee_id] = Attendee(attendee_id, name, email)
        print(Fore.GREEN + f"Attendee '{name}' registered successfully!")

    def sell_ticket(self, event_id, attendee_id):
        if event_id not in self.events:
            print(Fore.RED + f"No event found with ID '{event_id}'.")
            return
        if attendee_id not in self.attendees:
            print(Fore.RED + f"No attendee found with ID '{attendee_id}'.")
            return

        event = self.events[event_id]
        attendee = self.attendees[attendee_id]

        if event.sell_ticket():
            attendee.add_ticket(event_id)
            self.transactions.append(TicketTransaction(event_id, attendee_id))
            print(Fore.CYAN + f"Ticket sold to '{attendee.name}' for '{event.name}'.")
        else:
            print(Fore.YELLOW + f"No tickets left for event '{event.name}'.")

    def check_availability(self, event_id):
        if event_id not in self.events:
            print(Fore.RED + f"Event ID '{event_id}' does not exist.")
            return
        event = self.events[event_id]
        print(Fore.BLUE + f"Available tickets for '{event.name}': {event.available_tickets()}")

    def run_program(self):
        while True:
            print(Style.BRIGHT + "\n🎟️  EVENT MANAGER MENU")
            print("1. Add Event")
            print("2. Register Attendee")
            print("3. Sell Ticket")
            print("4. Check Availability")
            print("5. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                eid = input("Event ID: ")
                name = input("Event Name: ")
                date = input("Event Date (e.g., 2025-08-10): ")
                cap = int(input("Capacity: "))
                self.add_event(eid, name, date, cap)

            elif choice == "2":
                aid = input("Attendee ID: ")
                name = input("Name: ")
                email = input("Email: ")
                self.register_attendee(aid, name, email)

            elif choice == "3":
                eid = input("Event ID: ")
                aid = input("Attendee ID: ")
                self.sell_ticket(eid, aid)

            elif choice == "4":
                eid = input("Event ID: ")
                self.check_availability(eid)

            elif choice == "5":
                print(Fore.MAGENTA + "Thank you for using Event Manager. Goodbye!")
                break
            else:
                print(Fore.RED + "Invalid choice. Try again.")

# To run the program
if __name__ == "__main__":
    manager = EventManager()
    manager.run_program()
