from stats import *

from plot_stat import *


def report_menu():
    while True:
        print("\n===== REPORT MENU =====")
        print("1. MIN")
        print("2. MAX")
        print("3. AVG")
        print("4. Stats Per Property")
        print("5. Total Consumption per Property")
        print("6. Most Energy-Intensive Property")
        print("7. Average Daily Consumption")
        print("8. Full Report")
        print("9. Detect Anomalies")
        print("10. Highest Daily Consumption")
        print("11. Daily Ranking")
        print("12. 3-Day Moving Average")
        print("0. Back")

        choice = input("Choose: ")

        if choice == "1":
            print_min_value()

        elif choice == "2":
            print_max_value()

        elif choice == "3":
            print_average_value()

        elif choice == "4":
            print_stats_per_property()

        elif choice == "5":
            print_total_consumption_per_property()

        elif choice == "6":
            print_most_energy_intensive_property()

        elif choice == "7":
            print_average_daily_consumption()

        elif choice == "8":
            print_full_report()

        elif choice == "9":
            print_detect_anomalies()

        elif choice == "10":
            print_highest_daily_consumption()

        elif choice == "11":
            print_daily_ranking()

        elif choice == "12":
            print_3day_moving_avg()

        elif choice == "0":
            break

        else:
            print("Invalid choice")


def chart_menu():
    while True:
        print("\n===== CHART MENU =====")
        print("1. Total Consumption")
        print("2. Average Daily")
        print("3. Highest Daily")
        print("4. 3-Day Moving Average")
        print("0. Back")

        choice = input("Choose: ")

        if choice == "1":
            plot_total_consumption()

        elif choice == "2":
            plot_average_daily()

        elif choice == "3":
            plot_highest_daily()

        elif choice == "4":
            plot_3day_moving_avg()

        elif choice == "5":
            plot_stats_per_property()

        elif choice == "0":
            break

        else:
            print("Invalid choice")

# main menu


def main():
    while True:
        print("\n===== ELECTRICITY MANAGEMENT SYSTEM =====")
        print("1. Reports")
        print("2. Charts")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            report_menu()

        elif choice == "2":
            chart_menu()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


# Run main() only when this file is executed directly, not when it is imported by another file
if __name__ == "__main__":
    main()
