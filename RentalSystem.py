from Base import *
from Storage import *


def client_interface(company):
    while True:
        print("\n--- CLIENT MENU ---")
        print("1. View Available Vehicles")
        print("2. Rent a Vehicle")
        print("3. Return a Vehicle")
        print("4. Register")
        print("5. Customize Your Account")
        print("0. Exit")

        choice = input("Choose an option: ").strip()
        print()

        match choice:
            case "1":
                company.list_avaliable_vehicles()

            case "2":
                if not company.vehicles:
                    print("No vehicles available.")
                    continue
                if not company.clients:
                    print("No clients registered.")
                    continue

                client_id = input("Enter your client ID: ").strip()
                company.list_avaliable_vehicles()
                license_plate = input("Enter vehicle license plate: ").strip()
                start_date = input("Enter rental start date (DD-MM-YYYY): ").strip()
                end_date = input("Enter rental end date (DD-MM-YYYY): ").strip()

                company.rent_vehicle_by_plate(client_id, license_plate, start_date, end_date)

            case "3":
                rental_id = input("Enter your rental ID: ").strip()
                company.return_vehicle(rental_id)

            case "4":
                name = input("Enter your name: ").strip()
                surname = input("Enter your surname: ").strip()
                try:
                    age = int(input("Enter your age: "))
                except ValueError:
                    print("Invalid input for age.")
                    continue

                if age < 21:
                    print("You must be at least 21 years old to register.")
                    continue

                gender = input("Enter your gender: ").strip()
                client_id = input("Enter your ID: ").strip()
                try:
                    budget = int(input("Enter your budget: "))
                except ValueError:
                    print("Invalid input for budget.")
                    continue

                client = Client(name, surname, age, gender, client_id, budget)
                company.clients.append(client)
                print(f"Client registered: {client}")

            case "5":
                client_id = input("Enter your client ID: ").strip()
                company.customize_client(client_id)

            case "0":
                print("Exiting client menu...")
                break

            case _:
                print("Invalid option. Try again.")


def manager_interface(company):
    while True:
        print("\n--- MANAGER MAIN MENU ---")
        print("1. Add Data")
        print("2. Remove Data")
        print("3. View Data")
        print("4. Finance")
        print("5. Repair Vehicle")
        print("6. Customize Data")
        print("0. Exit")

        main_choice = input("Choose an option: ").strip()
        print()

        match main_choice:
            case "1":  # Add Data
                while True:
                    print("\n--- ADD MENU ---")
                    print("1. Add Vehicle")
                    print("2. Add Client")
                    print("3. Add Worker")
                    print("4. Add Location")
                    print("0. Back to Main Menu")

                    add_choice = input("Choose an option: ").strip()
                    print()

                    match add_choice:
                        case "1":
                            company.add_vehicle()
                        case "2":
                            company.add_client()
                        case "3":
                            company.add_worker()
                        case "4":
                            company.add_location()
                        case "0":
                            break
                        case _:
                            print("Invalid option. Try again.")

            case "2":  # Remove Data
                while True:
                    print("\n--- REMOVE MENU ---")
                    print("1. Remove Vehicle")
                    print("2. Remove Client")
                    print("3. Remove Worker")
                    print("4. Remove Location")
                    print("0. Back to Main Menu")

                    remove_choice = input("Choose an option: ").strip()
                    print()

                    match remove_choice:
                        case "1":
                            company.remove_vehicle()
                        case "2":
                            company.remove_client()
                        case "3":
                            company.remove_worker()
                        case "4":
                            company.remove_location()
                        case "0":
                            break
                        case _:
                            print("Invalid option. Try again.")

            case "3":  # View Data
                while True:
                    print("\n--- VIEW MENU ---")
                    print("1. View Vehicles")
                    print("2. View Clients")
                    print("3. View Workers")
                    print("4. View Rentals")
                    print("5. View Locations")
                    print("0. Back to Main Menu")

                    view_choice = input("Choose an option: ").strip()
                    print()

                    match view_choice:
                        case "1":
                            company.list_vehicles()
                        case "2":
                            company.list_clients()
                        case "3":
                            company.list_workers()
                        case "4":
                            company.list_rentals()
                        case "5":
                            company.list_locations()
                        case "0":
                            break
                        case _:
                            print("Invalid option. Try again.")

            case "4":  # Finance
                while True:
                    print("\n--- FINANCE MENU ---")
                    print("1. Check balance")
                    print("2. Add balance")
                    print("3. Check balance history ")
                    print("0. Back to Main Menu")
                    finance_choice = input("Choose an option: ").strip()
                    print()

                    match finance_choice:
                        case "1":
                            company.check_balance()
                        case "2":
                            amount = int(input("Enter amount to add: "))
                            company.add_balance(amount)
                        case "3":
                            company.check_balance_history() 
                        case "0":
                            break
                        case _:
                            print("Invalid option. Try again.")

            case "5": #Repair Vehicle
                damaged_veh = [v for v in company.vehicles if v.damaged == True]
                if not company.vehicles:
                    print("No vehicles available.")
                    continue
                if not damaged_veh:
                    print("No damaged vehicles available.")
                    continue
                print("Damaged Vehicles:")
                for vehicle in damaged_veh:
                    print(f"{vehicle.brand} {vehicle.model} | {vehicle.license_plate} is damaged.")
                license_plate = input("Enter the license plate of the vehicle to repair: ").strip()
                company.repair_vehicle(license_plate)

            case "6": #Customize Data
                while True:
                    print("\n--- CUSTOMIZE MENU ---")
                    print("1. Customize Vehicle")
                    print("2. Customize Client")
                    print("3. Customize Worker")
                    print("0. Back to Main Menu")

                    customize_choice = input("Choose an option: ").strip()
                    print()

                    match customize_choice:
                        case "1":
                            if not company.vehicles:
                                print("No vehicles available.")
                                continue
                            print("Available Vehicles:")
                            company.list_vehicles()
                            license_plate = input("Enter the license plate of the vehicle to customize: ").strip()
                            company.customize_vehicle(license_plate)
                        case "2":
                            if not company.clients:
                                print("No clients available.")
                                continue
                            print("Available Clients:")
                            company.list_clients()
                            client_id = input("Enter the ID of the client to customize: ").strip()
                            company.customize_client(client_id)

                        case "3":
                            if not company.workers:
                                print("No workers available.")
                                continue
                            print("Available Workers:")
                            company.list_workers()
                            worker_id = input("Enter the ID of the worker to customize: ").strip()
                            company.customize_worker(worker_id)
                        case "0":
                            break
                        case _:
                            print("Invalid option. Try again.")
            case "0":
                print("Exiting manager menu...")
                break

            case _:
                print("Invalid option. Try again.")


if __name__ == "__main__":
    company = load_company_data()
    if not company:
        company = Company("DriveNow")

    while True:
        print("\nWelcome to DriveNow Car Rental System")
        print("1. Client")
        print("2. Manager")
        print("0. Save and Exit")
        print("9. Exit Without Saving")
        print("10. Delete all Savings")

        user_type = input("Choose your role: ").strip()
        print()

        if user_type == "1":
            client_interface(company)
        elif user_type == "2":
            manager_interface(company)
        elif user_type == "0":
            save_company_data(company)
            print("Goodbye!")
            break
        elif user_type == "9":
            print("Goodbye!")
            break
        elif user_type == "10":
            delete_company_data()
        else:
            print("Invalid option.")