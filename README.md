# Weather Copilot

A Weather Copilot that answers your weather-related questions using OpenAI's GPT-4o-mini model, powered by real-time weather data from the Open-Meteo API.

## Features

- **Real-time Weather Data**: Fetches current weather information for any location worldwide
- **AI-Powered Responses**: Uses OpenAI's GPT-4o-mini to provide intelligent answers to weather questions
- **Location-based Queries**: Accepts any city or location name and automatically geocodes it
- **Interactive CLI**: Simple command-line interface for easy interaction

## How It Works

1. The application first prompts for your location
2. It uses the Open-Meteo Geocoding API to convert your location name to coordinates
3. Weather data is fetched from the Open-Meteo Weather API using those coordinates
4. You can then ask any weather-related questions
5. The weather data and your question are sent to OpenAI's API for a contextual response

## Setup

### Prerequisites

- Python 3.7 or higher
- OpenAI API key
- Internet connection

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Weather_Copilot
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Create a `.env` file in the project root
   - Add your OpenAI API key:
```
OPENAI_KEY=your_openai_api_key_here
```

## Usage

Run the main application:

```bash
python gpt_API.py
```

The application will:
1. Ask for your location
2. Fetch current weather data
3. Prompt you to ask weather-related questions
4. Provide AI-powered answers based on the real weather data

Example interaction:
```
Where do you live?: London
What is your question?: Should I wear a jacket today?
```

## API Integration

### Open-Meteo API
- **Geocoding**: Converts location names to coordinates
- **Weather Data**: Provides current weather information
- **Free to use**: No API key required
- **Global coverage**: Works for locations worldwide

### OpenAI API
- **Model**: GPT-4o-mini
- **Purpose**: Processes weather data and answers user questions
- **Authentication**: Bearer token from environment variable

## File Structure

```
Weather_Copilot/
├── gpt_API.py                    # Main application with OpenAI integration
├── open_metro_API_integration.py # Weather data fetching functions
├── requirements.txt              # Python dependencies
├── .env                          # Environment variables (API keys)
├── .gitignore                    # Git ignore file
├── LICENSE                       # MIT License
└── README.md                     # This file
```

## Key Functions

### `open_metro_API_integration.py`
- `get_coordinates(location)`: Converts location name to latitude/longitude
- `get_weather_data(lat, lon)`: Fetches weather data for given coordinates
- `main()`: Orchestrates the weather data retrieval process

### `gpt_API.py`
- `main()`: Main application loop that handles user interaction
- Integrates weather data with OpenAI API for intelligent responses

## Dependencies

- `requests`: HTTP library for API calls
- `python-dotenv`: Environment variable management

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this project.

## Disclaimer

This application uses external APIs (Open-Meteo and OpenAI). Please ensure you comply with their respective terms of service and usage policies.
