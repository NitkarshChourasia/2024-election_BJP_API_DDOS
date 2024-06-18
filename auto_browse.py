import webbrowser
import random
import time
import pyautogui
import requests


def get_random_words(n):
    """Fetch a list of n random words from an API."""
    url = "https://random-word-api.herokuapp.com/word"
    response = requests.get(url, params={"number": n})
    if response.status_code == 200:
        return response.json()
    else:
        return []


def open_browser():
    """Open the default web browser."""
    webbrowser.get("windows-default").open("https://www.bing.com")


def type_search_query(word):
    """Type the search query into the browser's search bar."""
    # Commneted out the important line below
    # pyautogui.click(400, 50)  # Click on the browser's search bar
    pyautogui.hotkey("ctrl", "a")  # Select any existing text
    pyautogui.press("backspace")  # Clear the search bar
    search_query = f"{word} helero"
    pyautogui.write(
        search_query, interval=0.08
    )  # Type at ~50 WPM (0.12 seconds per character)
    pyautogui.press("enter")  # Press Enter to search
    time.sleep(2)  # Wait for the search results to load


if __name__ == "__main__":
    words_to_search = get_random_words(50)

    # Important code here
    # The issue is with the location of the mouse click
    # open_browser()
    time.sleep(5)  # Wait for the browser to open

    for word in words_to_search:
        type_search_query(word)
        time.sleep(2)  # Wait a bit between searches to allow the page to load

    # No need to close tabs in this script


# import webbrowser
# import random
# import string
# import pyautogui
# import time

# def random_string(length):
#     """Generate a random string of fixed length."""
#     letters = string.ascii_lowercase
#     return ''.join(random.choice(letters) for i in range(length))

# def search_random_substring():
#     """Perform a web search with a random string using Microsoft Edge."""
#     # Generate a random string of 5 characters
#     random_query = random_string(5)

#     # Construct the search URL for Bing (or any other search engine)
#     search_url = f"https://www.bing.com/search?q={random_query}"

#     # Open the search URL in Microsoft Edge
#     webbrowser.get("microsoft-edge").open(search_url)

# def close_tabs():
#     """Close tabs in Microsoft Edge after a delay."""
#     time.sleep(10)  # Adjust the sleep time if needed
#     for _ in range(5):  # Close 5 tabs
#         pyautogui.hotkey('ctrl', 'w')
#         time.sleep(1)  # Add a small delay between tab closings

# if __name__ == "__main__":
#     for _ in range(5):  # Perform 5 random searches
#         search_random_substring()
#         time.sleep(2)  # Wait a bit between searches to allow the page to load

#     close_tabs()
