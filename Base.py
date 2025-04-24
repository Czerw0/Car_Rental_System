from datetime import datetime
import random 

class Vehicle:
    def __init__(self, license_plate, brand=None, model=None, year=None, fuel=None, condition=None, price=None, availability=True, damaged = False):
        self.license_plate = license_plate
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel = fuel
        self.condition = condition
        self.price = price
        self.availability = availability
        self.damaged = damaged

    def __str__(self):
        return f"{self.brand} {self.model} ({self.license_plate})"


class Car(Vehicle):
    def __init__(self, license_plate, brand=None, model=None, year=None, fuel=None, condition=None, price=None, availability=True, damaged = False):    
        super().__init__(license_plate, brand, model, year, fuel, condition, price, availability, damaged)
        self.type = "car"

    def __str__(self):
        return f"{self.type.capitalize()} - {super().__str__()} | {self.year}, {self.fuel}, {self.condition}"


class Motorbike(Vehicle):
    def __init__(self, license_plate, brand=None, model=None, year=None, fuel=None, condition=None, price=None, availability=True, damaged = False):
        super().__init__(license_plate, brand, model, year, fuel, condition, price, availability, damaged)
        self.type = "motorbike"

    def __str__(self):
        return f"{self.type.capitalize()} - {super().__str__()} | {self.year}, {self.fuel}, {self.condition}"


class Person:
    def __init__(self, name, surname, age, gender, id):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.id = id


class Client(Person):
    def __init__(self, name, surname, age, gender, id, budget):
        super().__init__(name, surname, age, gender, id)
        self.budget = float(budget)

    def __str__(self):
        return f"{self.id} | {self.name} {self.surname} | Age: {self.age}, Budget: ${self.budget}"


class Worker(Person):
    def __init__(self, name, surname, age, gender, id, position):
        super().__init__(name, surname, age, gender, id)
        self.position = position

    def __str__(self):
        return f"{self.name} {self.surname} | {self.position}"


class Location:
    def __init__(self, address, city, country):
        self.address = address
        self.city = city
        self.country = country

    def __str__(self):
        return f"{self.address}, {self.city}, {self.country}"


class Rental:
    def __init__(self, client, vehicle, start_date, end_date, rental_id=None):
        self.start_date = start_date
        self.end_date = end_date
        self.client = client
        self.vehicle = vehicle
        self.rental_id = self.generate_rental_id()  

    id_counter = 1  
    def generate_rental_id(self):
        rental_id = f"RENT{Rental.id_counter:04d}" 
        Rental.id_counter += 1
        return rental_id

    def __str__(self):
        return f"Rental {self.rental_id}: {self.vehicle} to {self.client} from {self.start_date} to {self.end_date}"

class BalanceRecord:
    def __init__(self, description, amount, new_balance):
        self.description = description
        self.amount = amount
        self.new_balance = new_balance

    def __str__(self):
        return f"Description: {self.description}, Amount: {self.amount}, New Balance: {self.new_balance}"


    
class Company:
    def __init__(self, name):
        self.name = name
        self.vehicles = []
        self.locations = []
        self.clients = []
        self.workers = []
        self.rentals = []
        self.worker_cost = 0
        self.balance = 1000  # Initial balance
        self.balance_history = []


    
    # Add methods
    def add_vehicle(self):
        vehicle_type = input("Which type of vehicle do you want to add (car/motorbike): ").lower()

        license_plate = input("Enter license plate: ").strip()
        brand = input("Enter brand: ").strip()
        model = input("Enter model: ").strip()
        try:
            year = int(input("Enter year: "))
            price = float(input("Enter price: "))
        except ValueError:
            print("Error: Year must be an integer and price must be a float.")
            return

        fuel = input("Enter fuel type: ").strip()
        condition = input("Enter condition (e.g., new, used): ").strip()
        availability = True
        damaged = False

        if vehicle_type == "car":
            vehicle = Car(license_plate, brand, model, year, fuel, condition, price, availability, damaged)
        elif vehicle_type == "motorbike":
            vehicle = Motorbike(license_plate, brand, model, year, fuel, condition, price, availability, damaged)
        else:
            print("Invalid vehicle type.")
            return

        self.vehicles.append(vehicle)
        print(f"Vehicle added: {vehicle}; Availability: {availability}")

    def add_location(self):
        address = input("Enter address: ").strip()
        city = input("Enter city: ").strip()
        country = input("Enter country: ").strip()

        location = Location(address, city, country)
        self.locations.append(location)
        print(f"Location added: {location}")

    def add_worker(self):
        name = input("Enter worker's name: ").strip()
        surname = input("Enter worker's surname: ").strip()
        try:
            age = int(input("Enter worker's age: "))
        except ValueError:
            print("Error: Age must be an integer.")
            return

        gender = input("Enter gender: ").strip()
        worker_id = input("Enter ID: ").strip()
        position = input("Enter position: ").strip()

        worker = Worker(name, surname, age, gender, worker_id, position)
        self.workers.append(worker)
        print(f"Worker added: {worker}")

    def add_client(self):
        name = input("Enter client's name: ").strip()
        surname = input("Enter client's surname: ").strip()
        try:
            age = int(input("Enter client's age: "))
        except ValueError:
            print("Error: Age must be an integer.")
            return

        if age < 21:
            print("You must be at least 21 years old to register as a client.")
            return

        gender = input("Enter gender: ").strip()
        client_id = input("Enter ID: ").strip()
        try:
            budget = float(input("Enter budget: "))
        except ValueError:
            print("Error: Budget must be a float.")
            return

        client = Client(name, surname, age, gender, client_id, budget)
        self.clients.append(client)
        print(f"Client added: {client}")

    #Customize methods
    def customize_client(self, client_id):
        
        found_client = None
        for client in self.clients:
            if client.id == client_id:
                found_client = client
                break
        if not found_client:
            print("Client not found.")
            return

        while True:
            n_choice = input("What do you want to change?\n1. Name\n2. Surname\n3. Age\n4. Gender\n5. ID\n6. Budget\n0. Done\n Choose an option: ").strip()
            if n_choice == "1":
                found_client.name = input("Enter new name: ").strip()
            elif n_choice == "2":
                found_client.surname = input("Enter new surname: ").strip()
            elif n_choice == "3":
                found_client.age = int(input("Enter new age: "))
            elif n_choice == "4":
                found_client.gender = input("Enter new gender: ").strip()
            elif n_choice == "5":
                found_client.id = input("Enter new ID: ").strip()
            elif n_choice == "6":
                print(f"Current budget: {found_client.budget}")
                print("1. Top up")
                print("2. Withdraw")
                n_choice = input("Choose an option: ").strip()
                if n_choice == "1":
                    found_client.budget += int(input("Top up to your account: "))
                    print(f"New budget: {found_client.budget}")
                elif n_choice == "2":
                    found_client.budget -= int(input("Withdraw from your account: "))
                    print(f"New budget: {found_client.budget}")
            elif n_choice == "0":
                break
            else:
                print("Invalid option. Try again.")
        print("The account has been updated.")
    
    def customize_worker(self, worker_id):
        found_worker = None
        for worker in self.clients:
            if worker.id == worker_id:
                found_client = worker
                break
        if not found_worker:
            print("Client not found.")
            return

        while True:
            n_choice = input("What do you want to change?\n1. Name\n2. Surname\n3. Age\n4. Gender\n5. ID\n6. Budget\n0. Done\n Choose an option: ").strip()
            if n_choice == "1":
                found_worker.name = input("Enter new name: ").strip()
            elif n_choice == "2":
                found_worker.surname = input("Enter new surname: ").strip()
            elif n_choice == "3":
                found_worker.age = int(input("Enter new age: "))
            elif n_choice == "4":
                found_worker.gender = input("Enter new gender: ").strip()
            elif n_choice == "5":
                found_worker.id = input("Enter new ID: ").strip()
            elif n_choice == "6":
                found_worker.position = input("Enter new position: ").strip()
            elif n_choice == "0":
                break
            else:
                print("Invalid option. Try again.")
        print("Worker has been updated.")

    def customize_vehicle(self, license_plate):
        found_car = None
        for car in self.vehicles:
            if car.license_plate == license_plate:
                found_car = car
                break
        if not found_car:
            print("Car not found.")
            return

        while True:
            n_choice = input("What do you want to change?\n1. Brand\n2. Model\n3. Year\n4. Fuel\n5. Condition\n6. Price\n0. Done\n Choose an option: ").strip()
            if n_choice == "1":
                found_car.brand = input("Enter new brand: ").strip()
            elif n_choice == "2":
                found_car.model = input("Enter new model: ").strip()
            elif n_choice == "3":
                found_car.year = int(input("Enter new year: "))
            elif n_choice == "4":
                found_car.fuel = input("Enter new fuel type: ").strip()
            elif n_choice == "5":
                found_car.condition = input("Enter new condition: ").strip()
            elif n_choice == "6":
                found_car.price = float(input("Enter new price: "))
            elif n_choice == "0":
                break
            else:
                print("Invalid option. Try again.")
        print(" has been updated.")

    #Renting methods
    def rent_vehicle_by_plate(self, client_id, license_plate, start_date, end_date):
        client = next((c for c in self.clients if c.id == client_id), None)
        if not client:
            print(f"No client found with ID: {client_id}")
            return

        vehicle = next((v for v in self.vehicles if v.license_plate == license_plate), None)
        if not vehicle:
            print(f"No vehicle found with license plate: {license_plate}")
            return
        
        if not vehicle.availability:
            print(f"Vehicle {license_plate} is not available.")
            return

        total_days = (datetime.strptime(end_date, "%d-%m-%Y") - datetime.strptime(start_date, "%d-%m-%Y")).days + 1 
        total_cost = float(vehicle.price) * float(total_days)

        if float(client.budget) < total_cost:
            print(f"{client.name} {client.surname} does not have enough budget to rent for {total_days} days. Needed: ${total_cost:.2f}")
            return

       # Update balance after rental
        self.worker_cost += 0.2 * total_cost
        self.balance -= self.worker_cost

        rental = Rental(client, vehicle, start_date, end_date) 
        rental_id = rental.rental_id

        self.balance_history.append(BalanceRecord(
            f"Rental worker cost of {vehicle.brand} {vehicle.model} ({license_plate}) RENTAL ID:{rental_id}",
            self.worker_cost, 
            self.balance
        ))

        self.balance += total_cost
        self.worker_cost = 0

        self.balance_history.append(BalanceRecord(
            f"Rental of {vehicle.brand} {vehicle.model} ({license_plate})",
            total_cost,
            self.balance
        ))

        client.budget -= total_cost
        vehicle.availability = False

        self.rentals.append(rental)
        
        print(f"{client.name} {client.surname} successfully rented {vehicle.brand} {vehicle.model} ({vehicle.license_plate}) "
            f"from {start_date} to {end_date} for ${total_cost:.2f}. Remaining budget: ${client.budget:.2f}")
        print(f"Remember the rent id: {rental_id}")

    def return_vehicle(self, rental_id):
        rental = next((r for r in self.rentals if r.rental_id == rental_id), None)
        
        if not rental:
            print(f"No rental found with ID: {rental_id}.")
            return

        rental.vehicle.availability = True
        print(f"Vehicle {rental.vehicle.brand} {rental.vehicle.model} ({rental.vehicle.license_plate}) has been returned by {rental.client.name} {rental.client.surname}.")

        # Handle random damage
        if random.random() < 0.3:  
            rental.vehicle.damaged = True
            rental.vehicle.availability = False
            print(f"Note: {rental.vehicle.license_plate} has returned with damage.")

            # Deduct damage cost from the client
            rental.client.budget -= 100
            print(f"{rental.client.name} {rental.client.surname} has been charged $100 for the damage. Remaining budget: ${rental.client.budget:.2f}")
            if rental.client.budget < 0:
                print(f"Warning: {rental.client.name} {rental.client.surname} has insufficient funds after the damage charge.")
                print("Contact the company for further assistance.")
        else:
            print(f"{rental.vehicle.license_plate} returned successfully.")



    # Remove methods
    def remove_vehicle(self):
        print("Available vehicles:")
        for vehicle in self.vehicles:
            if vehicle.availability:
                print(vehicle)
        print()
        license_plate = input("Enter vehicle license plate: ").strip()
        if not license_plate:
            print("License plate cannot be empty.")
            return
        if not any(v.license_plate == license_plate for v in self.vehicles):
            print(f"No vehicle found with license plate: {license_plate}")
            return
        if not any(v.availability == True for v in self.vehicles):
            print(f"Vehicle {license_plate} is not available for removal.")
            return
        vehicle = next((v for v in self.vehicles if v.license_plate == license_plate), None)
        if not vehicle:
            print(f"No vehicle found with license plate: {license_plate}")
            return
        self.vehicles.remove(vehicle)
        print(f"Vehicle {license_plate} has been removed.")

    def remove_location(self):
        print("Available locations:")
        for location in self.locations:
            print(location)
        print()
        address = input("Enter location address: ").strip()
        if not address:
            print("Address cannot be empty.")
            return
        if not any(l.address == address for l in self.locations):
            print(f"No location found with address: {address}")
            return
        location = next((l for l in self.locations if l.address == address), None)
        if not location:
            print(f"No location found with address: {address}")
            return
        self.locations.remove(location)
        print(f"Location {address} has been removed.")

    def remove_client(self):
        print("Available clients:")
        for client in self.clients:
            if not client in self.rentals:
                print(client)
        print()
        id = input("Enter client ID: ").strip()
        if not id:
            print("ID cannot be empty.")
            return
        if not any(c.id == id for c in self.clients):
            print(f"No client found with ID: {id}")
            return
        client = next((c for c in self.clients if c.id == id), None)
        if not client:
            print(f"No client found with ID: {id}")
            return
        self.clients.remove(client)
        print(f"Client {client.name} {client.surname} has been removed.")

    def remove_worker(self):
        id = input("Enter worker ID: ").strip()
        if not id:
            print("ID cannot be empty.")
            return
        if not any(w.id == id for w in self.workers):
            print(f"No worker found with ID: {id}")
            return
        worker = next((w for w in self.workers if w.id == id), None)
        if not worker:
            print(f"No worker found with ID: {id}")
            return
        self.workers.remove(worker)
        print(f"Worker {worker.name} {worker.surname} has been removed.")


    #list methods
    def list_vehicles(self):
        for v in sorted(self.vehicles, key=lambda x: x.type):
            print(v, "; Availability:", v.availability, "; damaged:", v.damaged)

    def list_clients(self):
        for c in sorted(self.clients, key=lambda x: x.name):
            print(c)

    def list_workers(self):
        for w in sorted(self.workers, key=lambda x: x.name):
            print(w)

    def list_locations(self):
        for l in sorted(self.locations, key=lambda x: x.country):
            print(l)

    def list_rentals(self):
        for r in sorted(self.rentals, key=lambda x: x.start_date):
            print(r)

    def list_avaliable_vehicles(self):
        print("Available vehicles:")
        for v in sorted(self.vehicles, key=lambda x: x.type):
            if v.availability and not v.damaged:
                print(v, "; Availability:", v.availability)


    #balance methods 
    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

    def add_balance(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
            return
        self.balance += amount
        # Record the balance change
        self.balance_history.append(BalanceRecord("Added funds", amount, self.balance))
        print(f"Balance updated. New balance: ${self.balance:.2f}")

    def check_balance_history(self):
            n = 1
            if not self.balance_history:
                print("No balance history available.")
            else:
                print("\n--- Balance History ---")
                for record in self.balance_history:
                    print(f"Transaction {n}: {record.description}, Amount: {record.amount}, New Balance: {record.new_balance}")

    #damaged and repair methods
    def model_vehicle_damaged(self, license_plate):
        for vehicle in self.vehicles:
            if vehicle.license_plate == license_plate and vehicle.availability:
                if vehicle.damaged:
                    print("This vehicle is already modeled as damaged.")
                else:
                    vehicle.damaged = True
                    vehicle.availability = False  
                    print(f"{vehicle.license_plate} has been modeled as damaged.")
                return
        print("Vehicle not found.")

    def repair_vehicle(self, license_plate):
        print("Damaged vehicles:")
        for v in self.vehicles:
            if v.damaged and v.license_plate == license_plate:
                print(f"{v.model} {v.model} | {v.license_plate} is damaged.")
            else:
                print("There are no damaged vehicles.")
                return
        
        for vehicle in self.vehicles:
            if vehicle.license_plate == license_plate:
                if not vehicle.damaged:
                    print("This vehicle is not damaged.")
                else:
                    vehicle.damaged = False
                    vehicle.availability = True

                    self.balance -= 100

                    if self.balance < 0:
                        print("Insufficient funds for repair.")
                        print("Come back later.")
                        vehicle.damaged = True
                        vehicle.availability = False
                        return
                    else:
                        self.balance_history.append(BalanceRecord(
                            f"Repair cost for {vehicle.brand} {vehicle.model} {vehicle.license_plate}",
                            -100,
                            self.balance
                        ))

                        print(f"Repair cost deducted. New balance: ${self.balance:.2f}")
                        print(f"{vehicle.license_plate} has been repaired and is now available.")
                return
        print("Vehicle not found.")


    
