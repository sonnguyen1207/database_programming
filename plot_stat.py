import matplotlib.pyplot as plt
from stats import *


def plot_total_consumption():
    rows = get_total_consumption_per_property()

    names = [row[0] for row in rows]
    totals = [row[1] for row in rows]

    plt.bar(names, totals)
    plt.title("Total Consumption per Property")
    plt.xlabel("Property")
    plt.ylabel("kWh")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_average_daily():
    rows = get_average_daily_consumption()

    names = [row[0] for row in rows]
    avgs = [row[1] for row in rows]

    plt.bar(names, avgs)
    plt.title("Average Daily Consumption")
    plt.show()


def plot_highest_daily():
    rows = get_highest_daily_consumption()

    names = [row[0] for row in rows]
    values = [row[2] for row in rows]

    plt.bar(names, values)
    plt.title("Highest Daily Consumption")
    plt.show()


def plot_3day_moving_avg():
    rows = get_3day_moving_avg()

    dates = [row[1] for row in rows]
    values = [row[2] for row in rows]

    plt.plot(dates, values, marker="o")
    plt.title("3-Day Moving Average")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_stats_per_property():
    rows = get_stats_per_property()

    names = [row[0] for row in rows]
    avgs = [row[3] for row in rows]

    plt.bar(names, avgs)
    plt.title("AVG per Property")
    plt.show()
