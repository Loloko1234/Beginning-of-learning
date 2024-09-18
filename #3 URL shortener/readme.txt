# URL Shortener

This is a simple Python script that shortens a given URL using the `pyshorteners` library. The script prompts the user to input a URL and then returns a shortened version of the URL using the TinyURL service.

### Explanation

- **How It Works:** Explains the steps the script takes to shorten a URL.
- **Prerequisites:** Lists the requirements for running the script.
- **Installation:** Provides instructions for cloning the repository and installing the required library.
- **Usage:** Explains how to run the script and input a URL.
- **Example:** Shows an example of how the script works.

## How It Works

1. The script prompts the user to input a URL.
2. It initializes a `Shortener` object from the `pyshorteners` library.
3. It uses the TinyURL shortener to shorten the provided URL.
4. It prints the shortened URL.

## Prerequisites

- Python 3.x
- `pyshorteners` library

## Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```
2.Install the Required Library: 
    ```sh
    pip install pyshorteners
    ```
##Usage
    1.Run the Script:
    ```sh
    python starter.py
    ```
    Input the URL:
        When prompted, type or paste the URL you want to shorten and press Enter.

    
    Get the Shortened URL:
        The script will output the shortened URL.

##Example
    Type your link: https://www.example.com
    Shortened URL: http://tinyurl.com/abc123