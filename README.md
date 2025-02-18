# AI-Scraper-crawl4AI

AI-Scraper-crawl4AI is a web scraping application built with Streamlit and Crawl4AI. It allows users to input a URL, scrape the content of the webpage, and download the scraped content as a Markdown file.

![Application Screenshot]("crawl4AI.png")

## Features

- Custom styling for a visually appealing interface
- URL input for specifying the webpage to scrape
- Button to trigger the web scraping process
- Error handling for request errors and general exceptions
- Download link for the scraped Markdown content

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/AI-Scraper-crawl4AI.git
   cd AI-Scraper-crawl4AI
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv myenv
   source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:

   ```sh
   streamlit run main.py
   ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter the URL of the webpage you want to scrape in the input field.

4. Click the "Run Web Scraper" button to start the scraping process.

5. Once the content is scraped, you can download it as a Markdown file by clicking the download button.

## Project Structure

- [main.py](http://_vscodecontentref_/0): The main script that runs the Streamlit app and handles the web scraping logic.
- [requirements.txt](http://_vscodecontentref_/1): The list of dependencies required for the project.
- [myenv](http://_vscodecontentref_/2): The virtual environment directory (not included in the repository).

## Dependencies

- Streamlit
- Requests
- Crawl4AI
- asyncio

## License

This project is for personal use only

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Crawl4AI](https://github.com/yourusername/crawl4AI)
