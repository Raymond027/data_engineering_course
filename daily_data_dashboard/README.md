# Daily Data Dashboard

## Overview
Daily Data Dashboard is a simple Python project that fetches data from multiple APIs and exports the results. It currently retrieves:

- OpenWeatherMap weather data for a default city
- CoinGecko cryptocurrency prices for Bitcoin and Ethereum
- GitHub public user information

## Project Structure

- `src/`
  - `main.py` — application entry point that requests data from the configured APIs and prints results
  - `config.py` — loads environment variables and stores API URLs and default values
- `requirement.txt` — Python dependencies
- `README.md` — project documentation

## Features

- Weather data via OpenWeatherMap
- Crypto prices from CoinGecko
- GitHub public user details
- Environment-based configuration using `.env`

## Setup

1. Clone the repository.
2. Create a Python virtual environment.
3. Install dependencies:

```bash
pip install -r requirement.txt
```

4. Create a `.env` file in the project root with the following values:

```env
OPENWEATHER_API_KEY=your_openweather_api_key
DEFAULT_CITY=Las Vegas
```

> `OPENWEATHER_API_KEY` is required. `DEFAULT_CITY` defaults to `Las Vegas` if not provided.

## Usage

Run the dashboard script from the project root:

```bash
python -m src.main
```

This will make API requests and print the response data to the console.

## API Endpoints

- Weather: OpenWeatherMap
  - `https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric`
- Crypto: CoinGecko
  - `https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd`
- GitHub: GitHub public user API
  - `https://api.github.com/users/Raymond227`

## Notes

- The project currently prints API responses directly and does not yet export to CSV.
- Add your own GitHub user URL or enhance `src/main.py` to support dynamic usernames.

## Improvements

Potential next steps:

- export collected data to CSV or database
- add command-line arguments for city and GitHub username
- handle API errors and rate limits more robustly
- add tests for API integration and configuration
