FlightFinderKstop

🛠️ Setup Instructions

Make sure you already have Python installed on your laptop.

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

3️⃣ Install requirements

    ````bash
    pip install -r requirements.txt
    ````

4️⃣ Running the Application

    The program loads data automatically from flight.json.

    ````bash
    python main.py
    ````


5️⃣ Running the test case

    ````bash
    pytest -v
    ````