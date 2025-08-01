# In-memory storage for travel details and expenses
travel_details = []
travel_expenses = []

# Function to Add Travel Details
def add_travel(team_id, destination, travel_date, transport, accommodation, activities):
    travel_detail = {
        "id": len(travel_details) + 1,
        "team_id": team_id,
        "destination": destination,
        "travel_date": travel_date,
        "transport": transport,
        "accommodation": accommodation,
        "activities": activities
    }
    travel_details.append(travel_detail)
    print("Travel details added successfully.")

def view_travel():
    if not travel_details:
        print("No travel details available.")
        return
    for travel in travel_details:
        print(travel)

# Function to Update Travel Details
def update_travel(travel_id, team_id, destination, travel_date, transport, accommodation, activities):
    for travel in travel_details:
        if travel["id"] == travel_id:
            travel.update({
                "team_id": team_id,
                "destination": destination,
                "travel_date": travel_date,
                "transport": transport,
                "accommodation": accommodation,
                "activities": activities
            })
            print("Travel details updated successfully.")
            return
    print("Travel ID not found.")

# Function to Delete Travel Details
def delete_travel(travel_id):
    global travel_details
    travel_details = [travel for travel in travel_details if travel["id"] != travel_id]
    print("Travel details deleted successfully.")

# Function to Add Travel Expenses
def add_expense(team_id, category, amount, description):
    expense = {
        "expense_id": len(travel_expenses) + 1,
        "team_id": team_id,
        "category": category,
        "amount": amount,
        "description": description
    }
    travel_expenses.append(expense)
    print("Expense recorded successfully.")

# Function to View All Expenses
def view_expenses():
    if not travel_expenses:
        print("No travel expenses available.")
        return
    for expense in travel_expenses:
        print(expense)

# Function to Get Total Expenses for a Team
def get_total_expenses(team_id):
    total = sum(expense["amount"] for expense in travel_expenses if expense["team_id"] == team_id)
    print(f"Total expenses for Team {team_id}: ${total:.2f}")

# Main Menu
while True:
    print("\nTeam Travel Planning Tool")
    print("1. Add Travel Details")
    print("2. View Travel Details")
    print("3. Update Travel Details")
    print("4. Delete Travel Details")
    print("5. Add Travel Expense")
    print("6. View Travel Expenses")
    print("7. Get Total Expenses for a Team")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        team_id = input("Enter Team ID: ")
        destination = input("Enter destination: ")
        travel_date = input("Enter travel date (YYYY-MM-DD): ")
        transport = input("Enter transport method: ")
        accommodation = input("Enter accommodation: ")
        activities = input("Enter planned activities: ")
        add_travel(team_id, destination, travel_date, transport, accommodation, activities)

    elif choice == "2":
        print("\nCurrent Travel Details:")
        view_travel()

    elif choice == "3":
        travel_id = int(input("Enter Travel ID to update: "))
        team_id = input("Enter new Team ID: ")
        destination = input("Enter new destination: ")
        travel_date = input("Enter new travel date (YYYY-MM-DD): ")
        transport = input("Enter new transport method: ")
        accommodation = input("Enter new accommodation: ")
        activities = input("Enter new planned activities: ")
        update_travel(travel_id, team_id, destination, travel_date, transport, accommodation, activities)

    elif choice == "4":
        travel_id = int(input("Enter Travel ID to delete: "))
        delete_travel(travel_id)

    elif choice == "5":
        team_id = input("Enter Team ID: ")
        category = input("Enter expense category (Flight, Hotel, Food, Transport, etc.): ")
        amount = float(input("Enter expense amount: "))
        description = input("Enter expense description: ")
        add_expense(team_id, category, amount, description)

    elif choice == "6":
        print("\nCurrent Travel Expenses:")
        view_expenses()

    elif choice == "7":
        team_id = input("Enter Team ID to get total expenses: ")
        get_total_expenses(team_id)

    elif choice == "8":
        print("Exiting... Safe Travels!")
        break

    else:
        print("Invalid choice. Please try again.")