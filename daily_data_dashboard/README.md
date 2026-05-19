# Project Title 
Daily Data Dashboard

## Description
Fetch data from multiple APIs (weather, crypto, GitHub) and export to csv.

## API

- Weather: OpenWeatherMap (free API key)
Endpoint: http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric

- Crypto Prices: CoinGecko (no API key needed)
Endpoint: https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd

- GitHub User Info: GitHub API (no key needed for public info)
Endpoint: https://api.github.com/users/{username}