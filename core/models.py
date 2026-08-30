"""
Trae-GodMode: Model Hyperparameters & Context Matrix
"""

MODEL_CAPABILITIES = {
    "gemini-3.1-pro-preview": {
        "context_window": 1000000,
        "max_output_tokens": 32000,
        "tool_turns": 500,
        "vision": True,
        "reasoning": "max"
    },
    "gemini-3-flash-preview": {
        "context_window": 1000000,
        "max_output_tokens": 32000,
        "tool_turns": 500,
        "vision": True,
        "reasoning": "max"
    },
    "seed-2.1-turbo": {
        "context_window": 1000000,
        "max_output_tokens": 32000,
        "tool_turns": 500,
        "vision": True,
        "reasoning": "max"
    },
    "gpt-5.4": {
        "context_window": 272000,
        "max_output_tokens": 32000,
        "tool_turns": 500,
        "vision": True,
        "reasoning": "max"
    },
    "custom-router-1m": {
        "context_window": 1048576,
        "max_output_tokens": 128000,
        "tool_turns": 500,
        "vision": True,
        "reasoning": "max"
    }
}
