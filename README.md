Home Garden & Mushroom Tracker
A desktop utility to manage agricultural inventory and calculate growth cycles for home cultivation.

Note: Embed a GIF of your desktop GUI in action or a screenshot of your script's terminal output executing successfully.

🎯 Objective
A desktop application built to streamline the management of a home cultivation farm. It currently specializes in automating the inventory and cycle tracking for white oyster mushrooms (Pleurotus ostreatus), calculating precise incubation and fructification dates, with the underlying database architecture designed to expand into broader vegetable garden management.

✨ Key Features
Cycle Tracking: Automatically calculates and tracks critical dates for agricultural batches, transitioning from incubation to fruiting phases.

Inventory Management: Logs specific cultivation parameters, including substrate ratios and spawn sources, into a local database.

Visual Interface: Intuitive graphical user interface built for fast data entry of new crop batches and quick status checks on active growth cycles.

🛠️ Tech Stack
Language: Python 3.10+

Frameworks & Libraries: Tkinter, SQLAlchemy

Architecture: Event-driven GUI application integrated with a local SQLite database for persistent batch tracking.

🚀 Installation & Setup
To run this project locally, follow these steps:

Clone the repository:
git clone [https://github.com/EdgarKorsin-cloud/hongos_ostra.git](https://github.com/EdgarKorsin-cloud/hongos_ostra.git)

Navigate to the directory:
cd hongos_ostra

Create a virtual environment:
python -m venv venv

Activate the virtual environment:

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

Install required dependencies:
pip install -r requirements.txt

💻 Usage
To launch the application, run the following command from the root directory:
python main.py

(Once the GUI opens, you can log a new batch by inputting your substrate details, spawn source, and inoculation date. The application will automatically save the record and calculate the projected dates for the incubation and fructification cycles.)

🗺️ Roadmap & Issue Tracking
Development is tracked via GitHub Issues.
Upcoming milestones include:

Expanding cultivation profiles to support new mushroom varieties like Shiitake and Lion's Mane.

Adding tracking parameters for traditional backyard vegetable crops, starting with carrots, green tomatoes, cayenne chili peppers, and turnips.

Integrating the OpenWeatherMap API to provide automated, weather-based watering alerts for outdoor crops.
