# For Bojro Edition: MIRA Assistant

MIRA is a modular voice assistant capable of offline Speech-to-Text (Whisper) and high-quality Text-to-Speech (Edge TTS). For the "Brain," you can choose between **Google Gemini** (Online/Fast) or **LM Studio** (Offline/Private).

## 1. Prerequisites

### Install Python
* **Download:** [Python 3.10+](https://www.python.org/downloads/)
* **Important:** Check the box **"Add Python to PATH"** during installation.

### Install FFmpeg (Required for Hearing)
* **Option A (Chocolatey):** Run terminal as Admin: `choco install ffmpeg`
* **Option B (Manual):**
    1. Download "release-essentials" from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/).
    2. Extract the zip.
    3. Copy `ffmpeg.exe` (from the `bin` folder) into this `MIRA/` folder.

---

## 2. Installation

1.  Open your terminal inside the `MIRA` folder.
2.  Install all required libraries:

    ```bash
    pip install -r requirements.txt
    ```

---

## 3. Audio Driver Troubleshooting (Windows)

If you see an error related to `PyAudio` during installation, run these commands to fix the microphone driver:

```bash
pip install pipwin
pipwin install pyaudio

## 4. Configuration: Choose Your Brain

MIRA can run in two modes. Open `MIRA/brain.py` to switch between them.

### Option A: Google Gemini (Online & Fast)
*Best for speed and accuracy. Requires an internet connection.*

1.  Get a free API Key from [Google AI Studio](https://aistudio.google.com/).
2.  Open the `.env` file and paste your key:
    ```ini
    GEMINI_API_KEY=your_key_here
    ```
3.  **Edit `brain.py`**:
    * **Uncomment** the Gemini section (remove `'''` quotes).
    * **Comment out** the LM Studio section (add `'''` quotes).

### Option B: LM Studio (Offline & Private)
*Best for privacy. Runs 100% on your PC.*

1.  Download & Install **[LM Studio](https://lmstudio.ai/)**.
2.  Download a model (e.g., **Meta Llama 3 8B**).
3.  Go to the **Local Server** tab (`<->` icon).
4.  Select your model and click **Start Server**.
5.  Ensure it is running on **Port 1234**.
6.  **Edit `brain.py`**:
    * **Uncomment** the LM Studio section.
    * **Comment out** the Gemini section.

---

## 5. Run MIRA

To start the assistant, run:

```bash
python main.py