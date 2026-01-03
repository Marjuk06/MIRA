##  Setup Instructions

### 1. Clone the Repository

git clone https://github.com/Marjuk06/MIRA.git
cd MIRA 



### 2. Create Virtual Environment

python -m venv venv


Activate:

   Windows: venv\Scripts\activate


### 3. Install Dependencies
pip install -r requirements.txt


### 4. Configure Secrets

Create a .env file in the root directory:

GEMINI_API_KEY=your_actual_api_key_here


### 5. Run MIRA
python main.py
