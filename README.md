# Python-Airlines-Prototype-Membership-System

This Python script simulates a prototype membership system for Python Airlines. The system calculates the membership tier based on the user's annual and lifetime flight metrics, and provides information about the associated rewards and benefits.

## Features

- Prompts the user to input their first name, annual miles flown, annual segments flown, annual spending, lifetime miles flown, upcoming flight information, and the cost of the coach class ticket for the next flight.
- Determines the user's annual membership tier (Diamond, Ruby, Emerald, Sapphire, or none) based on the provided annual metrics.
- Determines the user's lifetime membership tier (Diamond, Ruby, Emerald, or none) based on the provided lifetime miles.
- Displays a summary of the user's annual and lifetime flight metrics.
- Informs the user about their achieved annual and/or lifetime membership tiers.
- Provides information about the unlocked rewards and benefits based on the membership tier, including:
  - Free checked bags per flight
  - Free seat upgrades to the specified cabin class
  - Access to the club lounge in Chicago (if the next/upcoming flight is to or through Chicago)
  - Discounted ticket price for the upcoming flight

## Usage

1. Run the Python script.
2. Enter the requested information when prompted:
   - First name
   - Annual miles flown
   - Annual segments flown
   - Annual spending (in USD)
   - Lifetime miles flown
   - Whether the next/upcoming flight is to or through Chicago (yes/y or no/n)
   - Cost of the coach class ticket for the next flight (in USD)
3. The script will process the entered information and display the user's membership tier(s), unlocked rewards, and discounted ticket price (if applicable).

## Requirements

This Python script was written and tested with Python 3. No additional libraries or dependencies are required.
