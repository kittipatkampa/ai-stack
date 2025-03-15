import os
import json
from dotenv import dotenv_values
import streamlit as st

###############################################
# Load environment variables from .env file
###############################################

# We have logic to pull the environment variables from different sources
ENV_FILE_PATHS = [
    # If you want to deploy on Streamlit Cloud, use this file
    os.path.join(os.path.dirname(__file__), "..", ".streamlit", "secrets.toml"),
    
    # Usually for Kubernetes, use this file
    "/app/system_configs/.env",
    
    # For local development, use this file
    os.path.join(os.path.dirname(__file__), "..", ".env"),
]

for env_path in ENV_FILE_PATHS:
    print(f"Checking environment file: {env_path}")
    if os.path.exists(env_path):
        print(f"Use environment file from: {env_path}")
        if env_path.endswith("secrets.toml"):
            config = st.secrets
        else:
            config = dotenv_values(env_path)
        break
    else:
        print(f"Environment file not found: {env_path}")
else:
    raise ValueError("No environment file found. Please add your env file to one of the following paths: " + str(ENV_FILE_PATHS))


class Settings:
    def __init__(self):

        self.env = config.get("ENV")
        
        # Endpoint
        self.endpoint_host = config.get("ENDPOINT_HOST")
        self.endpoint_port = config.get("ENDPOINT_PORT")
        
        self.embedding_model_name = config.get("EMBEDDING_MODEL_NAME")
        
        # AWS credentials
        self.aws_access_key_id = config.get("AWS_ACCESS_KEY_ID")
        self.aws_secret_access_key = config.get("AWS_SECRET_ACCESS_KEY")
        self.aws_session_token = config.get("AWS_SESSION_TOKEN")
        self.aws_region = config.get("AWS_REGION")        
                
        # LLM API keys
        self.openai_api_key = config.get("OPENAI_API_KEY")
        self.anthropic_api_key = config.get("ANTHROPIC_API_KEY")
        self.pinecone_api_key = config.get("PINECONE_API_KEY")

        ###########################################
        # Temp directory
        ###########################################
        self.temp_directory = config.get("TEMP_DIRECTORY")
        self.temp_directory = os.path.expanduser(self.temp_directory)

# Create an instance of Settings
settings = Settings()

if __name__ == "__main__":
    """
    Usage:
    
    poetry run python common/settings.py
    """
    print(settings.__dict__)
