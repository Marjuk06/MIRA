# For Bojro Edition: MIRA Assistant

MIRA is a modular voice assistant capable of offline Speech-to-Text (Whisper), offline Intelligence (Llama 3 via LM Studio), and high-quality Text-to-Speech (Edge TTS).

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
2.  Install all required libraries using the requirements file:

    ```bash
    pip install -r requirements.txt
    ```

    *This automatically installs Faster-Whisper, Edge-TTS, OpenAI, PyGame, and other dependencies.*

---

## 3. Audio Driver Troubleshooting (Windows)

If you see an error related to `PyAudio` during the installation above, run these commands to fix the microphone driver:

```bash
pip install pipwin
pipwin install pyaudio

## 4. Setup The Brain (LM Studio)

1.  Download & Install **[LM Studio](https://lmstudio.ai/)**.
2.  Search for and download **Meta Llama 3 8B** (or any model you prefer).
3.  Go to the **Local Server** tab (`<->` icon on the left).
4.  Select your model at the top.
5.  Click **Start Server** (Green Button).
6.  Ensure it is running on **Port 1234**.

---

## 5. Run MIRA

To start the assistant, run:

```bash
python main.py
