FlightFinderKstop

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

3️⃣ Install project dependencies
    This project requires pytest for running unit tests.
    Install it with:

    ````bash
    pip install pytest
    ````

3️⃣ Running the Application

    The program loads data automatically from flight.json.

    ````bash
    python main.py
    ````


4️⃣ Running the test case

    ````bash
    pytest -v
    ````