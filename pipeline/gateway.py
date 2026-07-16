"""Kilo gateway — thin OpenAI-compatible LLM client.

The demo talks to models through Kilo's OpenAI-compatible gateway rather than
the Anthropic SDK. Everything is configured from the environment; no endpoint,
key, or model name is hard-coded.

Required env (see .env.example):
    KILO_BASE_URL   OpenAI-compatible base URL, e.g. http://host:11434/v1
    KILO_API_KEY    gateway API key
    KILO_MODEL      default model id (must be vision-capable to read menu photos)
"""

from __future__ import annotations

import base64
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class GatewayConfigError(RuntimeError):
    """Raised when the gateway is missing required configuration."""


def _require(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise GatewayConfigError(
            f"{name} is not set. Copy .env.example to .env and fill it in."
        )
    return value


def get_client() -> OpenAI:
    """Build an OpenAI-compatible client pointed at the Kilo gateway."""
    return OpenAI(api_key=_require("KILO_API_KEY"), base_url=_require("KILO_BASE_URL"))


def default_model() -> str:
    return _require("KILO_MODEL")


def image_content(prompt: str, image_bytes: bytes, media_type: str = "image/jpeg") -> list[dict]:
    """Build a vision message content list: a text part plus a base64 image.

    Uses the OpenAI chat-completions `image_url` data-URI form, which
    OpenAI-compatible gateways accept for vision-capable models.
    """
    b64 = base64.b64encode(image_bytes).decode("ascii")
    return [
        {"type": "text", "text": prompt},
        {"type": "image_url", "image_url": {"url": f"data:{media_type};base64,{b64}"}},
    ]


def complete(messages: list[dict], model: str | None = None, **kwargs) -> str:
    """Send a chat completion through the gateway and return the text reply."""
    client = get_client()
    response = client.chat.completions.create(
        model=model or default_model(),
        messages=messages,
        **kwargs,
    )
    return response.choices[0].message.content or ""


if __name__ == "__main__":
    # Manual smoke test: python -m pipeline.gateway
    reply = complete([{"role": "user", "content": "Reply with the single word: ok"}])
    print(f"Gateway reply: {reply!r}")
