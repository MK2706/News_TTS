import uvicorn
from backend.api import app
from frontend.streamlit_app import main as streamlit_main

if __name__ == "__main__":
    # Run FastAPI backend
    uvicorn.run(app, host="0.0.0.0", port=8000)

    # Run Streamlit frontend
    streamlit_main()