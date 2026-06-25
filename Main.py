import json
import os

# Define the name of your database file
FILE_NAME = 'reaction_data.json'

def load_data():
    """Loads reaction data from the JSON file."""
    if not os.path.exists(FILE_NAME):
        print(f"Error: Could not find '{FILE_NAME}'. Please make sure it is in the same folder.")
        return []
    
    with open(FILE_NAME, 'r') as file:
        return json.load(file)

def save_data(data):
    """Saves the updated data back to the JSON file."""
    with open(FILE_NAME, 'w') as file:
        json.dump(data, file, indent=4)
    print("\n✅ Database updated successfully!")

def check_reaction(data):
    """Option 1: Check if a reaction exists."""
    print("\n--- Check a Reaction ---")
    u_react = input("Reactant (e.g., Zinc): ").strip().lower()
    u_reag = input("Acid/Base (e.g., HCl): ").strip().lower()
    u_c = input("Concentration (Dilute/Concentrated): ").strip().lower()
    u_t = input("Temperature (Cold/Room temp/Warm/Hot): ").strip().lower()
    
    for reaction in data:
        if (reaction["reactant"] == u_react and 
            reaction["reagent"] == u_reag and 
            reaction["concentration"] == u_c and 
            reaction["temp"] == u_t):
            print(f"\n✅ Reaction is Valid!")
            print(f"Main Produced Compound: {reaction['main_product']}")
            return

    print("\n❌ This reaction is not possible under these specific conditions, or it is not in the database.")

def add_reaction(data):
    """Option 2: Add a completely new reaction to the database."""
    print("\n--- Add a New Reaction ---")
    new_reaction = {
        "reactant": input("Enter Reactant: ").strip().lower(),
        "reagent": input("Enter Acid/Base: ").strip().lower(),
        "concentration": input("Enter Concentration: ").strip().lower(),
        "temp": input("Enter Temperature: ").strip().lower(),
        "main_product": input("Enter Main Product (e.g., Sodium Chloride (NaCl)): ").strip()
    }
    
    data.append(new_reaction)
    save_data(data)

def update_reaction(data):
    """Option 3: Modify an existing reaction in the database."""
    print("\n--- Update a Reaction ---")
    
    # Show all reactions with a number next to them
    for i, reaction in enumerate(data):
        print(f"[{i}] {reaction['reactant'].title()} + {reaction['reagent'].upper()} ({reaction['concentration']}, {reaction['temp']}) -> {reaction['main_product']}")
    
    try:
        choice = int(input("\nEnter the number of the reaction you want to modify: "))
        if 0 <= choice < len(data):
            print("\nEnter new values (leave blank to keep current value):")
            
            # Helper function to only update if the user types something new
            def update_field(field_name, current_value):
                new_val = input(f"{field_name} [{current_value}]: ").strip()
                return new_val.lower() if new_val else current_value
            
            # Keep the main product casing as the user types it, lower-case the rest
            data[choice]["reactant"] = update_field("Reactant", data[choice]["reactant"])
            data[choice]["reagent"] = update_field("Acid/Base", data[choice]["reagent"])
            data[choice]["concentration"] = update_field("Concentration", data[choice]["concentration"])
            data[choice]["temp"] = update_field("Temperature", data[choice]["temp"])
            
            new_prod = input(f"Main Product [{data[choice]['main_product']}]: ").strip()
            if new_prod:
                data[choice]["main_product"] = new_prod
                
            save_data(data)
        else:
            print("❌ Invalid reaction number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    """The main menu loop."""
    data = load_data()
    if not data:
        return # Exit if file is missing
    
    while True:
        print("\n" + "="*30)
        print(" CHEMICAL REACTION DATABASE ")
        print("="*30)
        print("1. Check reaction")
        print("2. Add reaction")
        print("3. Modify or update reaction data")
        print("0. Exit app")
        
        choice = input("\nChoose an option: ").strip()
        
        if choice == '1':
            check_reaction(data)
        elif choice == '2':
            add_reaction(data)
        elif choice == '3':
            update_reaction(data)
        elif choice == '0':
            print("Exiting app. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 0, 1, 2, or 3.")

# Run the app
if __name__ == "__main__":
    main()