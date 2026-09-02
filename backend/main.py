from fastapi import FastAPI

# FastAPI application create kar rahe hain
app = FastAPI()


# Ye hamara basic test endpoint hai
@app.get("/")
def home():
    return {
        "message": "WeatherGPT Backend is running!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "WeatherGPT Backend"
    }