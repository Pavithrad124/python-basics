from datetime import datetime

class Travel:
    def __init__(self, team_id, destination, start_date, end_date, accommodation, expenses):
        self.team_id = team_id
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.accommodation = accommodation
        self.expenses = expenses

    def __repr__(self):
        return (f"Travel(team_id={self.team_id}, destination={self.destination}, "
                f"start_date={self.start_date}, end_date={self.end_date}, "
                f"accommodation={self.accommodation}, expenses={self.expenses})")


class Team:
    def __init__(self, team_id):
        self.team_id = team_id
        self.travels = []

    def add_travel(self, travel):
        self.travels.append(travel)

    def get_travels(self):
        return self.travels


class TravelManager:
    def __init__(self):
        self.teams = {}

    def create_team(self, team_id):
        if team_id not in self.teams:
            self.teams[team_id] = Team(team_id)
            print(f"Team {team_id} created.")
        else:
            print(f"Team {team_id} already exists.")

    def add_travel(self, team_id, destination, start_date, end_date, accommodation, expenses):
        if team_id in self.teams:
            travel = Travel(team_id, destination, start_date, end_date, accommodation, expenses)
            self.teams[team_id].add_travel(travel)
            print(f"Travel added for team {team_id}.")
        else:
            print(f"Team {team_id} does not exist.")

    def get_travels_by_team(self, team_id):
        if team_id in self.teams:
            travels = self.teams[team_id].get_travels()
            if travels:
                return travels
            else:
                return "No travel details found for this team."
        else:
            return "Team does not exist."


# Example usage
if __name__ == "__main__":
    travel_manager = TravelManager()

    # Create teams using user input
    while True:
        create_team_input = input("Do you want to create a team? (yes/no): ").strip().lower()
        if create_team_input == "yes":
            team_id = input("Enter the team ID: ").strip()
            travel_manager.create_team(team_id)
        elif create_team_input == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    # Add travel details using user input
    while True:
        add_travel_input = input("Do you want to add travel details? (yes/no): ").strip().lower()
        if add_travel_input == "yes":
            team_id = input("Enter the team ID: ").strip()
            destination = input("Enter the destination: ").strip()
            start_date = int(input("Enter travel date (YYYY-MM-DD): ")).strip()
            end_date = int(input("Enter the end date (YYYY-MM-DD): ")).strip()
            accommodation = input("Enter the accommodation: ").strip()
            expenses = float(input("Enter the expenses: ").strip())

            # Add travel details to the team
            travel_manager.add_travel(team_id, destination, start_date, end_date, accommodation, expenses)
        elif add_travel_input == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    # Get travel details for a specific team using user input
    team_id = input("Enter team ID to get travel details: ").strip()
    travels = travel_manager.get_travels_by_team(team_id)

    if isinstance(travels, str):
        print(travels)
    else:
        for travel in travels:
            print(travel)