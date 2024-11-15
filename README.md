
# Google Search Results Scraper

This project is a Python-based tool to scrape Google search results using the Google Custom Search JSON API. It allows users to retrieve search results programmatically and process them as needed.

## Features

- Query Google search programmatically.
- Retrieve and process the top search results.
- Easy-to-use and customizable.

## Requirements

- Python 3.x
- `requests` library
- `pandas` library

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your API keys:
   - Add your **Google API Key** and **Custom Search Engine ID (cx)** in the `google_search_api` function.

## Usage

1. Import the script or run it directly.
2. Call the `google_search_api` function with your desired query and number of results:
   ```python
   from Google_search_results_scraper import google_search_api

   query = "example search"
   results = google_search_api(query, num_results=10)
   ```

3. Process the returned results as needed (e.g., save them to a file, display them, etc.).

## Notes

- Ensure you have a valid Google API Key and a Custom Search Engine ID.
- Google API limits may apply depending on your subscription.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests.

---

Happy coding! 🚀
