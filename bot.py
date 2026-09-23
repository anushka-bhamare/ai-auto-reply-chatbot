import time
import pyautogui
import pyperclip
from openai import OpenAI
import re
import os
# Give yourself a few seconds to switch to the target window

client=OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def is_last_message_from_sender(text, sender_name="Sakshi Kolekar Skn"):
    # split the chat log into individual messages
    messages=text.strip().split("/2026]")[-1]
    if sender_name in messages:
        return True
    return False

time.sleep(3)

# Click the icon
pyautogui.click(990, 1049)

# Wait for the application to respond
time.sleep(0.5)

while True:

    # Drag to select the text
    pyautogui.moveTo(689, 239)
    pyautogui.dragTo(719, 927, duration=0.8, button='left')

    # Small delay to ensure selection is complete
    time.sleep(0.2)

    # Copy the selected text
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(725, 241)

    # Wait for clipboard to update
    time.sleep(0.2)

    # Get clipboard contents
    chat_history = pyperclip.paste()

    print("Copied text:")
    print(chat_history)

    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system",
                "content": "You are a person named anushka who speaks hindi as well as english. You are from India and you are a coder. You analyze chat history and respond like anushka. Output should be the next chat response (text message only)"},
            {"role": "user",
                "content": chat_history}
        ]
    )

        response=completion.choices[0].message.content
        pyperclip.copy(response)

        # Click where you want to paste the text
        pyautogui.click(1338, 975)

        time.sleep(0.2)

    # Paste the copied text
        pyautogui.hotkey('ctrl', 'v')

        time.sleep(0.2)

        # press enter
        pyautogui.press('enter')

     