#!/usr/bin/env python3
"""
This module displays the first launch.
"""
import requests


if __name__ == '__main__':
    """
    Displays the first launch with these information:
       Name of the launch
       The date (in local time)
       The rocket name
       The name (with the locality) of the launchpad.
    """
    launch_url = "https://api.spacexdata.com/v4/launches/"
    launch_response = requests.get(launch_url)
    print(launch_response.url)
    launches = launch_response.json()

    first_launch = min(
        launches, key=lambda launch: launch["date_unix"])

    launch_name = first_launch["name"]
    launch_date = first_launch["date_local"]
    rocket_id = first_launch["rocket"]
    launchpad_id = first_launch["launchpad"]

    rocket_url = f"https://api.spacexdata.com/v4/rockets/{rocket_id}"
    rocket_response = requests.get(rocket_url)
    rockets = rocket_response.json()

    rocket_name = rockets["name"]

    launchpad_url = f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}"
    launchpad_response = requests.get(launchpad_url)
    launchpads = launchpad_response.json()

    launchpad_name = launchpads["name"]
    launchpad_locality = launchpads["locality"]

    print(f"{launch_name} ({launch_date})"
          f"{rocket_name} - {launchpad_locality})")
