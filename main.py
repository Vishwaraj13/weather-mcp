from fastmcp import FastMCP
import requests
import os
from dotenv import load_dotenv

from fastmcp import FastMCP
from fastmcp.server.auth.providers.jwt import StaticTokenVerifier


load_dotenv()
BEARER_TOKEN = os.getenv("MCP_BEARER_TOKEN")
# Configure authentication with StaticTokenVerifier
verifier = StaticTokenVerifier(
    tokens={
        BEARER_TOKEN: {
            "client_id": "name@company.com",
        }
    }
)

# Load your WeatherAPI key (store in env variable for safety)
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "your_api_key_here")
print("Using Weather API Key:", WEATHER_API_KEY)
# Create MCP app with authentication
mcp = FastMCP(name="weather-mcp", auth=verifier)

@mcp.tool()
def get_weather(city: str) -> dict:
    """
    Get current weather for a given city using WeatherAPI.com.
    """
    base_url = "https://api.weatherapi.com/v1/current.json"
    params = {"key": WEATHER_API_KEY, "q": city, "aqi": "no"}

    response = requests.get(base_url, params=params)

    if response.status_code != 200:
        return {"error": f"Failed to fetch weather: {response.text}"}

    data = response.json()
    location = data.get("location", {})
    current = data.get("current", {})

    return {
        "city": location.get("name"),
        "region": location.get("region"),
        "country": location.get("country"),
        "temperature_c": current.get("temp_c"),
        "condition": current.get("condition", {}).get("text"),
        "humidity": current.get("humidity"),
        "wind_kph": current.get("wind_kph"),
        "last_updated": current.get("last_updated")
    }

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0",port=8001)
