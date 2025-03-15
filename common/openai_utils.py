import openai
from openai import OpenAI
from tenacity import retry, stop_after_attempt, wait_exponential
from common.settings import settings

openai_client = OpenAI(api_key=settings.openai_api_key)

@retry(
    stop=stop_after_attempt(0), wait=wait_exponential(multiplier=1, min=4, max=10)
)
def response(messages: list[dict]) -> str:
    """
    Make a request to the OpenAI API with retry logic.
    """
    try:
        response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.6,
            max_tokens=1000,
            timeout=10,
        )
        _response_str = response.choices[0].message.content
        
        return _response_str
    except openai.APITimeoutError as e:
        print(f"Error occurred while making OpenAI request: {str(e)}")
        # logger.error(f"Error occurred while making OpenAI request: {str(e)}")

@retry(
    stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10)
)
def stream_response(messages: list[dict]) -> str:
    """
    Make a request to the OpenAI API with retry logic.
    """
    try:
        stream = openai_client.chat.completions.create(
            model="gpt-4o-2024-08-06",
            messages=messages,
            temperature=0.0,
            max_tokens=1000,
            timeout=10,
            stream=True,
        )
                
        for chunk in stream:
            s = chunk.choices[0].delta.content
            if s is not None:
                yield s
    except Exception as e:
        raise Exception(f"Error occurred while making OpenAI request: {str(e)}")
    
def pretty_print_openai_messages(messages: list[dict]) -> None:
    """
    Display the messages in a readable format.
    """
    for message in messages:
        if message.get("role") == "user":
            print("\nUSER:")
            if message.get("content"):
                if isinstance(message.get("content"), list):
                    for content in message["content"]:
                        if content.get("type") == "text":
                            print(content.get("text"))
                else:
                    print(message.get("content"))
        if message.get("role") == "system":
            print("\nSYSTEM:")
            print(message.get("content"))
            
            
if __name__ == "__main__":
    """
    Usage:
    poetry run python common/openai_utils.py
    """
    
    # Test the make_openai_request function
    print(response(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the capital of France?"},
        ]
    ))
    
    # Test the make_openai_request_stream function
    for s in stream_response(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Please cuont 1 to 20"},
        ]
    ):
        print(s, end="", flush=True)
