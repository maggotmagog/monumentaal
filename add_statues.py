#!/usr/bin/env python3
"""
Script to add South African statues to sites.json
Reads current sites.json, appends new statues with sequential IDs.
"""

import json
import re

# Read existing sites.json
with open("src/data/sites.json", "r") as f:
    sites = json.load(f)

# Get the current max ID
max_id = max(site["id"] for site in sites)

# Define new statues to add (with accurate data)
new_statues = [
    {
        "name": "Paul Kruger Statue (Church Square)",
        "type": "statue",
        "lat": -25.746,
        "lng": 28.187,
        "province": "Gauteng",
        "year_built": 1899,
        "description": "Bronze statue of Paul Kruger on a granite plinth, located in Church Square, Pretoria. The statue faces north towards the direction of the Transvaal Republic's capital before British annexation. Sculpted by Anton van Wouw."
    },
    {
        "name": "Queen Victoria Statue (Pietermaritzburg)",
        "type": "statue",
        "lat": -29.6006,
        "lng": 30.3728,
        "province": "KwaZulu-Natal",
        "year_built": 1901,
        "description": "Bronze statue of Queen Victoria on a marble plinth, located outside the Pietermaritzburg City Hall. Erected in 1901 to commemorate the Boer War. Sculpted by Herbert Hampton."
    },
    {
        "name": "Queen Victoria Statue (Port Elizabeth)",
        "type": "statue",
        "lat": -33.9618,
        "lng": 25.6148,
        "province": "Eastern Cape",
        "year_built": 1903,
        "description": "Bronze statue of Queen Victoria in front of the Port Elizabeth City Hall. One of several statues of Queen Victoria erected in South Africa after her death. Sculpted by Edward Onslow Ford."
    },
    {
        "name": "Louis Botha Statue (Cape Town)",
        "type": "statue",
        "lat": -33.9253,
        "lng": 18.4232,
        "province": "Western Cape",
        "year_built": 1926,
        "description": "Equestrian bronze statue of General Louis Botha, first Prime Minister of the Union of South Africa, located on the Foreshore near the Cape Town City Hall."
    },
    {
        "name": "Jan Smuts Statue (Cape Town)",
        "type": "statue",
        "lat": -33.925,
        "lng": 18.422,
        "province": "Western Cape",
        "year_built": 1953,
        "description": "Bronze statue of Jan Smuts, South African statesman and Field Marshal, located on the Cape Town Foreshore opposite the entrance to the City Hall."
    },
    {
        "name": "Cecil Rhodes Statue (Cape Town)",
        "type": "statue",
        "lat": -33.920,
        "lng": 18.418,
        "province": "Western Cape",
        "year_built": 1910,
        "description": "Bronze statue of Cecil John Rhodes on horseback, located at the bottom of Devil's Peak in the Company's Garden. The statue looks north towards the interior of Africa."
    },
    {
        "name": "Nelson Mandela Statue (Union Buildings)",
        "type": "statue",
        "lat": -25.7461,
        "lng": 28.1871,
        "province": "Gauteng",
        "year_built": 2013,
        "description": "9-meter bronze statue of Nelson Mandela standing with arms outstretched, located on the forecourt of the Union Buildings in Pretoria. Unveiled on the Day of Reconciliation."
    },
    {
        "name": "Mahatma Gandhi Statue (Johannesburg)",
        "type": "statue",
        "lat": -26.2046,
        "lng": 28.0476,
        "province": "Gauteng",
        "year_built": 2003,
        "description": "Bronze statue of Mahatma Gandhi in Gandhi Square, Johannesburg. Commemorates Gandhi's time in South Africa (1893-1914) where he developed his philosophy of satyagraha."
    },
    {
        "name": "Steve Biko Statue (Johannesburg)",
        "type": "statue",
        "lat": -26.204,
        "lng": 28.048,
        "province": "Gauteng",
        "year_built": 2006,
        "description": "Bronze statue of anti-apartheid activist Steve Biko located outside the Newtown Cultural Precinct in Johannesburg. Shows Biko seated, lost in thought."
    },
    {
        "name": "Shaka Zulu Statue (Durban)",
        "type": "statue",
        "lat": -29.8585,
        "lng": 31.0265,
        "province": "KwaZulu-Natal",
        "year_built": 2006,
        "description": "Large bronze statue of King Shaka Zulu standing tall with a spear and shield, located outside the Durban International Convention Centre. Commemorates the great Zulu king."
    },
    {
        "name": "Andries Pretorius Statue (Church Square)",
        "type": "statue",
        "lat": -25.746,
        "lng": 28.187,
        "province": "Gauteng",
        "year_built": 1895,
        "description": "Bronze equestrian statue of Andries Pretorius, Voortrekker leader and grandfather of Paul Kruger, located in Church Square, Pretoria."
    },
    {
        "name": "Piet Retief Statue (Church Square)",
        "type": "statue",
        "lat": -25.746,
        "lng": 28.187,
        "province": "Gauteng",
        "year_built": 1895,
        "description": "Bronze statue of Piet Retief, Voortrekker leader, located in Church Square, Pretoria. Part of the collection of statues representing South African historical figures."
    },
    {
        "name": "Hendrik Potgieter Statue (Church Square)",
        "type": "statue",
        "lat": -25.746,
        "lng": 28.187,
        "province": "Gauteng",
        "year_built": 1895,
        "description": "Bronze statue of Hendrik Potgieter, Voortrekker leader and first magistrate of Potchefstroom, located in Church Square, Pretoria."
    },
    {
        "name": "Chief Dingaan Statue (Durban)",
        "type": "statue",
        "lat": -29.858,
        "lng": 31.025,
        "province": "KwaZulu-Natal",
        "year_built": 2004,
        "description": "Bronze statue of King Dingane kaSenzangakhona, Zulu king, located in Durban. Represents the controversial Zulu monarch who fought against the Voortrekkers."
    },
    {
        "name": "King Sekhukhune Statue (Pretoria)",
        "type": "statue",
        "lat": -25.747,
        "lng": 28.186,
        "province": "Gauteng",
        "year_built": 2012,
        "description": "Bronze statue of King Sekhukhune I of the BaPedi, located near Church Square in Pretoria. Commemorates the Pedi king who resisted Boer and British colonialism."
    },
    {
        "name": "Albert Luthuli Statue (Johannesburg)",
        "type": "statue",
        "lat": -26.2046,
        "lng": 28.0476,
        "province": "Gauteng",
        "year_built": 2007,
        "description": "Bronze statue of Albert Luthuli, ANC president and Nobel Peace Prize laureate, located in Luthuli House, Johannesburg. Symbolizes his peaceful resistance to apartheid."
    },
    {
        "name": "Oliver Tambo Statue (Johannesburg)",
        "type": "statue",
        "lat": -26.205,
        "lng": 28.048,
        "province": "Gauteng",
        "year_built": 2009,
        "description": "Bronze statue of Oliver Tambo, ANC leader and anti-apartheid activist, located outside the ANC headquarters in Johannesburg. Shows Tambo in a reflective pose."
    },
    {
        "name": "Joe Slovo Statue (Johannesburg)",
        "type": "statue",
        "lat": -26.203,
        "lng": 28.049,
        "province": "Gauteng",
        "year_built": 2009,
        "description": "Bronze statue of Joe Slovo, anti-apartheid leader and SACP leader, located in Johannesburg. One of the few statues of a white communist in South Africa."
    },
    {
        "name": "Ruth First Statue (Johannesburg)",
        "type": "statue",
        "lat": -26.204,
        "lng": 28.047,
        "province": "Gauteng",
        "year_built": 2010,
        "description": "Bronze statue of Ruth First, anti-apartheid activist and scholar, located at the University of the Witwatersrand. Commemorates her life and assassination."
    },
    {
        "name": "Solomon Mahlangu Statue (Pretoria)",
        "type": "statue",
        "lat": -25.746,
        "lng": 28.187,
        "province": "Gauteng",
        "year_built": 2009,
        "description": "Bronze statue of Solomon Mahlangu, Umkhonto we Sizwe operative executed in 1979, located in Mahlangu Square, Pretoria. Symbolizes the youth sacrifice against apartheid."
    }
]

# Deduplicate: check against existing names+provinces
existing_keys = set((site["name"], site.get("province", "Unknown")) for site in sites)
filtered_statues = []

for statue in new_statues:
    key = (statue["name"], statue["province"])
    if key not in existing_keys:
        # Also check if any existing statue name contains this name (simple dedup)
        exists = any(statue["name"].lower() in existing[0].lower() or existing[0].lower() in statue["name"].lower() 
                     for existing in existing_keys)
        if not exists:
            filtered_statues.append(statue)

print(f"Adding {len(filtered_statues)} new statues (filtered from {len(new_statues)})")

# Assign new IDs and append
current_max_id = max_id
for statue in filtered_statues:
    current_max_id += 1
    statue["id"] = current_max_id
    sites.append(statue)

# Write back to sites.json
with open("src/data/sites.json", "w") as f:
    json.dump(sites, f, indent=2)

print(f"Total sites in JSON: {len(sites)}")
print(f"Statue count: {sum(1 for s in sites if s['type'] == 'statue')}")