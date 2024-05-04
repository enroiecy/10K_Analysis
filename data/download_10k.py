import os
from datetime import datetime
from sec_edgar_downloader import Downloader # pip install sec-edgar-downloader

def create_output_directory(output_directory):
    '''
    Create output directory if it doesn't exist
    Args:
        output_directory: str, directory to save the filings
    Returns:
        None
    '''
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

def download_10k_filings(ticker, form, start_period, end_period, output_directory):
    '''
    Download 10-K filings for a given company ticker for the years 1995-2023
    Args:
        ticker: str, company ticker
        output_directory: str, directory to save the filings
    Returns:
        None
    '''

    create_output_directory(output_directory)

    try:
        # Create a downloader object
        dl = Downloader('Georgia Tech', 'syeon31@gatech.edu', output_directory)

        # Get the list of 10-K filings
        filings = dl.get(form=form, ticker_or_cik=ticker, after=start_period, before=end_period, download_details=True)

        if filings is None:
            print(f"No {form} filings found for {ticker}")
            return
        
        print(f"Successfully downloaded {filings} {form} filings for {ticker} from {start_period} to {end_period}")

    except Exception as e:
        print(f"Error downloading {form} filings for {ticker}: {e}")

def main():
    # Prompt user to enter company ticker
    ticker = input("Enter company ticker: ").strip().upper()

    # Specify form type
    form = "10-K"

    # Specify start and end period
    start_period = "1995-01-01"
    end_period = "2023-01-01"

    # Specify output directory
    output_directory = f"data/{form}_filings"

    # Download 10-K filings
    download_10k_filings(ticker, form, start_period, end_period, output_directory)

if __name__ == "__main__":
    main()