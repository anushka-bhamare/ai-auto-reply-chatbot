# AI Auto Reply Chatbot

AI Auto Reply Chatbot is a Python-based project that automatically generates replies to messages using the OpenAI API. The project combines artificial intelligence with Python automation to create an automated reply system.

## About the Project

The main purpose of this project is to practice Python programming, API integration, and automation by building a simple AI-powered chatbot. The program takes a conversation as input and uses the OpenAI API to generate an appropriate reply.

## How the Chatbot Works

1. The program takes the conversation or message as input.
2. The conversation is sent to the OpenAI API.
3. The AI processes the given conversation.
4. The AI generates a suitable reply.
5. The generated reply is returned by the program.
6. Python automation can be used to work with the generated response.

## Features

- AI-generated automatic replies
- OpenAI API integration
- Processes conversation text
- Generates context-based responses
- Python-based automation
- Clipboard support
- Mouse and keyboard automation
- Secure API key handling using environment variables
- Simple and beginner-friendly implementation

## Technologies Used

- Python
- OpenAI API
- PyAutoGUI
- Pyperclip
- os module
- Environment variables
- Git
- GitHub

## Project Files

- `ai_chat.py` - Connects to the OpenAI API and generates AI-based replies
- `bot.py` - Handles chatbot automation
- `get_cursor.py` - Helps get the cursor position for automation
- `.gitignore` - Prevents unnecessary and sensitive files from being uploaded
- `README.md` - Project documentation

## How to Run

Clone the repository:

    git clone https://github.com/anushka-bhamare/ai-auto-reply-chatbot.git

Navigate to the project directory:

    cd ai-auto-reply-chatbot

Install the required Python libraries:

    pip install openai pyautogui pyperclip

Set your OpenAI API key as an environment variable:

### Windows PowerShell

    $env:OPENAI_API_KEY="your_api_key_here"

Run the program:

    python ai_chat.py

or:

    python bot.py

## Example

Input conversation:

    User: Hi, how are you?

The AI can generate a reply such as:

    I'm doing well, thank you! How are you?

The generated response depends on the conversation provided to the AI.

## Learning Outcomes

Through this project, I practiced and strengthened my understanding of:

- Python fundamentals
- Working with APIs
- OpenAI API integration
- Environment variables
- User input handling
- Text processing
- Python automation
- PyAutoGUI
- Pyperclip
- Git and GitHub
- Basic API key security

## Future Improvements

Possible improvements for the project include:

- Adding a graphical user interface
- Adding conversation history
- Adding different reply styles
- Adding voice input and output
- Improving error handling
- Adding customizable AI responses
- Supporting multiple AI models
- Improving automation features
- Adding logging functionality

## Security

The OpenAI API key should never be written directly inside the Python source code or uploaded to GitHub.

The project uses an environment variable:

    os.getenv("OPENAI_API_KEY")

Sensitive files such as `.env` should be added to `.gitignore`.

If an API key is accidentally uploaded to GitHub, it should be revoked or replaced immediately.

## Conclusion

AI Auto Reply Chatbot is a beginner-level Python project that demonstrates how artificial intelligence, APIs, and Python automation can be combined to create an automated reply system.

This project helped me gain practical experience with Python programming, API integration, automation, environment variables, and GitHub.

## Author

Anushka Bhamare
