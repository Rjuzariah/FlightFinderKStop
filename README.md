✈️ FlightFinderKstop

Find the cheapest flight price between two cities with at most K stops, using a modified Dijkstra + Min Heap algorithm.

This project is a Python console application with full unit test coverage using pytest.

📌 Features

1. Reads input from a flight.json file

2. Builds a directed weighted graph of flights

3. Uses Dijkstra with a priority queue optimized for K-stop constraints

4. Includes pytest test suite

5. Fully isolated environment using python venv


🛠️ Setup Instructions
1️⃣ Create a virtual environment

    ````bash
    # Create a virtual environment
    python3 -m venv venv
    ````

2️⃣ Activate the virtual environment

    ````bash
    source venv/bin/activate   # macOS/Linux
    venv\Scripts\activate      # Windows
    ````

▶️ Running the Application

    The program loads data automatically from flight.json.

    ````bash
    python main.py
    ````


▶️ Running the test case

    ````bash
    pytest -v
    ````