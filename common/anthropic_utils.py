import anthropic
from common.settings import settings
client = anthropic.Anthropic(api_key=settings.anthropic_api_key)

def count_tokens(system: str, messages: list[dict]):
    response = client.messages.count_tokens(
        model="claude-3-5-sonnet-20241022",
        system=system,
        messages=messages,
    )

    return response

def stream_response(client: anthropic.Anthropic, messages: list[dict], **kwargs):
    stream = client.messages.stream(
        messages=messages,
        **kwargs,
    )
    
    return stream

def response(client: anthropic.Anthropic, messages: list[dict], **kwargs):
    response = client.messages.create(
        messages=messages,
        **kwargs,
    )
    
    return response

if __name__ == "__main__":
    """
    Usage:
    
    poetry run python common/anthropic_utils.py
    """
    # stream response
    messages = [{"role": "user", "content": "Hi"}]
    response_config = {
        "model": "claude-3-5-sonnet-20241022",
        "max_tokens": 1024,
        "temperature": 0.0,
        "system": "You are a nice person",
    }
    resp = response(client, messages, **response_config)
    print(resp.content[0].text)