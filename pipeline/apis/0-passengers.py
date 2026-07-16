#!/usr/bin/env python3
"""
"""
import requests


def availableShips(passengerCount):
    """
    """
    available_ships = []
    url = "https://swapi-api.hbtn.io/api/starships/"

    while url:

        response = requests.get(url)

        data = response.json()

        ships = data["results"]

        for ship in ships:
            passerngers = ship["passengers"]

            passerngers = passerngers.replace(",", "")
            if passerngers.isdigit():
                passerngers = int(passerngers)

                if passerngers >= passengerCount:
                    available_ships.append(ship["name"])

        url = data["next"]

    return available_ships
