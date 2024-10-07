# Hiking Trails Scraper

This project scrapes hiking trail data from websites that provide information about trekking locations in Nepal. It gathers details like trail names, locations, and difficulty levels.

## Technologies Used

- Python
- BeautifulSoup (for web scraping)
- Pandas (for data handling)

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/crusty-crab/Hiking-Trail-Scrapper.git
   cd Hiking-Trails-Scrapper
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the scraper:

   ```bash
   python scripts/scraper.py
   scraper files may vary with the websites names
   ```

4. (Optional) Upload the data:
   ```bash
   python utils/upload.py
   ```

The scraped data is saved in the `Data/` directory as CSV files.
