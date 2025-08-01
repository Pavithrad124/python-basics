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

    def remove_travel(self, travel):
        self.travels.remove(travel)

    def update_travel(self, travel_index, updated_travel):
        if 0 <= travel_index < len(self.travels):
            self.travels[travel_index] = updated_travel

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


class TeamMember:
    def __init__(self, team_id, travel_manager):
        self.team_id = team_id
        self.travel_manager = travel_manager

    def view_travels(self):
        travels = self.travel_manager.get_travels_by_team(self.team_id)
        if isinstance(travels, str):
            print(travels)
        else:
            for travel in travels:
                print(travel)


class Admin:
    def __init__(self, travel_manager):
        self.travel_manager = travel_manager

    def add_travel(self, team_id, destination, start_date, end_date, accommodation, expenses):
        self.travel_manager.add_travel(team_id, destination, start_date, end_date, accommodation, expenses)

    def remove_travel(self, team_id, travel_index):
        if team_id in self.travel_manager.teams:
            team = self.travel_manager.teams[team_id]
            if 0 <= travel_index < len(team.travels):
                travel_to_remove = team.travels[travel_index]
                team.remove_travel(travel_to_remove)
                print(f"Travel removed for team {team_id}.")
            else:
                print("Invalid travel index.")
        else:
            print("Team does not exist.")

    def update_travel(self, team_id, travel_index, updated_travel):
        if team_id in self.travel_manager.teams:
            team = self.travel_manager.teams[team_id]
            team.update_travel(travel_index, updated_travel)
            print(f"Travel updated for team {team_id}.")
        else:
            print("Team does not exist.")


# Example usage with user inputs
if __name__ == "__main__":
    travel_manager = TravelManager()
    admin = Admin(travel_manager)

    # Create teams
    while True:
        team_id = input("Enter team ID to create (or type 'exit' to finish): ")
        if team_id.lower() == 'exit':
            break
        travel_manager.create_team(team_id)

    # Add travels
    while True:
        team_id = input("Enter team ID to add travel (or type 'exit' to finish): ")
        if team_id.lower() == 'exit':
            break
        destination = input("Enter destination: ")
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        accommodation = input("Enter accommodation: ")
        expenses = float(input("Enter expenses: "))

        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
            admin.add_travel(team_id, destination, start_date, end_date, accommodation, expenses)
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    # Create team members and view travels
    while True:
        team_id = input("Enter team ID to view travels (or type 'exit' to finish): ")
        if team_id.lower() == 'exit':
            break
        member = TeamMember(team_id, travel_manager)
        print(f"\nTravels for team {team_id}:")
        member.view_travels()

    # Update a travel
    while True:
        team_id = input("Enter team ID to update travel (or type 'exit' to finish): ")
        if team_id.lower() == 'exit':
            break
        travel_index = int(input("Enter travel index to update: "))
        destination = input("Enter new destination: ")
        start_date = input("Enter new start date (YYYY-MM-DD): ")
        end_date = input("Enter new end date (YYYY-MM-DD): ")
        accommodation = input("Enter new accommodation: ")
        expenses = float(input("Enter new expenses: "))

        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end)