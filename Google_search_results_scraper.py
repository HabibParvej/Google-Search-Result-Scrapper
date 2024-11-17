import requests
import pandas as pd

def google_search_api(query, num_results=10):
    # Google Developer api key
    api_key = "API_KEY"
    # Custom google search engine cx
    cse_id = "2784d8970ce3f41b1"
    
    # URL encode the query term to handle special characters
    query = requests.utils.quote(query)
    
    # Construct the API URL
    url = f"CUSTOM ENGINE GOOGLE URL "
    
    # Make the request to the Google Custom Search API
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        results = []

        # Loop through items to get title, link, and snippet
        for item in data.get("items", [])[:num_results]:
            title = item.get("title")
            link = item.get("link")
            description = item.get("snippet")
            results.append({
                "Title": title,
                "Link": link,
                "Description": description
            })
        
        # Save results to a CSV file
        if results:
            df = pd.DataFrame(results)
            df.to_csv("google_search_results.csv", index=False)
            print("Results saved to google_search_results.csv")
        else:
            print("No results found.")
    else:
        print("Error:", response.status_code, response.text)

# User input for search query
if __name__ == "__main__":
    query = input("Enter the search term: ")
    google_search_api(query)
