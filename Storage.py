import pickle
import os 

SAVE_FILE = "company_data.pkl"

def save_company_data(company):
    with open(SAVE_FILE, "wb") as f:
        pickle.dump(company, f)
    print("Data saved successfully.")

def load_company_data():
    try:
        with open('company_data.pkl', 'rb') as file:
            company = pickle.load(file)
            if not hasattr(company, 'balance_history'):
                print("Company data is incomplete. Initializing balance history.")
                company.balance_history = []
            print("Data loaded successfully.")
            return company
    except FileNotFoundError:
        print("No saved company data found, starting with a new company.")
        return None
    except EOFError:
        print("Error: Company data file is empty or corrupted. Starting with a new company.")
        return None
    except Exception as e:
        print(f"Unexpected error while loading company data: {e}")
        return None

def delete_company_data():
    try:
        os.remove(SAVE_FILE)
        print("Data deleted successfully.")
    except FileNotFoundError:
        print("No saved data found to delete.")