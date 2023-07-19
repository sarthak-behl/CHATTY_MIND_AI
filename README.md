# CHATTY_MIND_AI

# Voice-Enabled AI Conversational Assistant

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/yourusername/voice-ai-conversational-assistant/blob/main/LICENSE)

## Overview

This project implements a Voice-Enabled AI Conversational Assistant that allows users to have interactive conversations with an AI language model. The script uses the OpenAI API, speech recognition, and text-to-speech technologies to provide a seamless voice-driven experience.

## Features

- Voice input recognition through the microphone
- Real-time speech-to-text conversion using Google's speech recognition service
- Interaction with the OpenAI API's `text-davinci-003` model for generating text responses
- Text-to-speech conversion to hear the AI-generated responses
- Continuous loop for an uninterrupted conversation until the user decides to exit

## Prerequisites

Before running the application, ensure you have the following:

- Python 3.x installed
- API key from OpenAI (Replace `YOUR_API_KEY` in the code with your valid API key)
- Required Python libraries:
  - OpenAI (`pip install openai`)
  - SpeechRecognition (`pip install SpeechRecognition`)
  - pyttsx3 (`pip install pyttsx3`)

## Installation

1. Clone this repository to your local machine:
   ```
   git clone https://github.com/yourusername/voice-ai-conversational-assistant.git
   ```
2. Install the required Python libraries as mentioned in the "Prerequisites" section.

## Usage

1. Obtain your API key from OpenAI and replace `YOUR_API_KEY` in the code with your key.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the script using the following command:
   ```
   python voice_ai_assistant.py
   ```
4. The script will prompt you to speak. Start a conversation with the AI by asking questions or making statements.
5. The AI will process your voice input, generate a response, and read it out loud to you.
6. The conversation will continue until you say "exit" or choose to stop asking questions.

## Examples

- **User**: "What is the capital of France?"
  - **AI**: "The capital of France is Paris."

- **User**: "Tell me a joke."
  - **AI**: "Why did the scarecrow win an award? Because he was outstanding in his field!"

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

The AI language model's responses are generated based on its training data and might not always be accurate or appropriate. Use the application responsibly and verify critical information from reliable sources.

## Contribution

Contributions to this project are welcome! Feel free to submit issues or pull requests.

---

