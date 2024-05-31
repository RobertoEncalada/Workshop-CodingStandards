from VacationPackage.Vacation import Vacation

class main:
    def main():
        destination = "Paris"
        num_passengers = 5
        duration = 10

        vacation = Vacation(destination, num_passengers, duration)
        total_cost = vacation.calculate_total_cost()

        if total_cost == -1:
            print("Invalid input.")
        elif num_passengers > 80:
            print("The vacation package is not available for groups of more than 80 people.")
        else:
            print(f"The total cost of the vacation package is: ${total_cost}")


    main()  



    