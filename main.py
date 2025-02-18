import streamlit as st
import requests 
import asyncio
from crawl4ai import AsyncWebCrawler,BrowserConfig, CrawlerRunConfig
# Helper Functions Overview:
    # Step 1: Custom Styling Function to enhance the app's visual appeal
    # Step 2: Scrape using Crawl4AI
    # Step 3: Function to transform HTML into Markdown
    # Step 4: Function to sanitize the markdown content
    # Step 5: Function to save the markdown file
    # Step 6: Main function to create the Streamlit app

# Step 1: Custom Styling Function to make the app more visually appealing
def apply_custom_styles():
    st.markdown(
        """
        <style>
        body {
            font-family: 'Helvetica Neue', sans-serif;
            background-color: #f9f9f9;
            color: #333;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
        }
        .stTextInput input {
            border-radius: 5px;
            padding: 10px;
            border: 1px solid #ddd;
            width: 100%;
            box-sizing: border-box;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def download_markdown(content, filename="extracted_content.md"):
    content_str = str(content)
    # Encode the content as Base64
    b64 = base64.b64encode(content_str.encode()).decode()

    # Create a download link with a button
    href = f"""
    <a href="data:file/markdown;base64,{b64}" download="{filename}">
        <button style="
            display: inline-block;
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            text-align: center;
            font-size: 16px;
            cursor: pointer;
            border-radius: 5px;
            border: none;">
            Download Markdown File
        </button>
    </a>
    """
    return href

#Crawl4AI scrapper
async def crawl4AI(url):

    browser_config = BrowserConfig(
    browser_type="chrome",
    headless=True,
    )
    
    user_config = CrawlerRunConfig(
    screenshot=True,
    wait_for_images=True,
    scan_full_page=True,  
    scroll_delay=2.0,    
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
       # Run the crawler on the specified URL
        result = await crawler.arun(
            url=url,
            config=user_config)

        html_content = result.html
    
        # Extract the screenshot as a PIL Image object
        screenshot = result.screenshot
    
    return html_content, screenshot

def main():
    # Apply custom styles to the app
    apply_custom_styles()

    # Step 6.1: URL input
    url = st.text_input("Enter the URL that you want to scrape:")



        # Step 6.2: Scrape button
    if st.button("Run Web Scraper"):
        if url:
            try:
                # Step 6.3: Send a GET request to the URL
                response = requests.get(url)
                print(response.status_code)
                response.raise_for_status()  # Raise an error for bad status codes
                html_content =   crawl4AI()
                st.markdown(html_content)
                
                # Step 6.10: Provide download link for scraped markdown content
                st.markdown(download_markdown(html_content), unsafe_allow_html=True)
            except requests.exceptions.RequestException as e:
                # Step 6.11: Error handling for request errors
                st.error(f"Error fetching the URL: {e}")
            except Exception as e:
                # Step 6.12: General error handling
                st.error(f"An unexpected error occurred: {e}")
        else:
            # Step 6.13: Warning for invalid URL input
            st.warning("Please enter a valid URL")

# Step 7: Run the app
if __name__ == "__main__":
    asyncio.run(main())




