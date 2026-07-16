#!/usr/bin/env python3
"""
This module displays the number of launches per rocket.
"""
import requests


if __name__ == '__main__':
    """
    Displays the number of launches per rocket.
    """
    launch_url = "https://api.spacexdata.com/v4/launches"
    rocket_url = f"https://api.spacexdata.com/v4/rockets"

    launch_response = requests.get(launch_url)
    rocket_response = requests.get(rocket_url)

    launches = launch_response.json()
    rockets = rocket_response.json()

    # Connect every rocket ID with name its name
    rockets_data = {}

    for rocket in rockets:
        rocket_id = rocket["id"]
        rocket_name = rocket["name"]

        rockets_data[rocket_id] = rocket_name

    # Count launches for every rocket
    frequency = {}

    for launch in launches:
        rocket_id = launch["rocket"]
        rocket_name = rockets_data[rocket_id]
        frequency[rocket_name] = frequency.get(rocket_name, 0) + 1

    # Sort by launch count, then alphabetically
    sorted_rockets = sorted(frequency.items(),
                            key=lambda i: (-i[1], i[0]))

    for rocket_name, launch_count in sorted_rockets:
        print(f"{rocket_name}: {launch_count}")
