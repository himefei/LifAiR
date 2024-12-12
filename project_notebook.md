# LifAi2 Project Notebook

This notebook provides an overview of the LifAi2 project structure and key functionalities.

## Project Structure

```
lifai2/
├── assets/
│   └── hub2.png
├── config/
│   ├── app_settings.json
│   ├── prompts.py
│   └── saved_prompts.py
├── core/
│   ├── app_hub.py
│   └── toggle_switch.py
├── modules/
│   ├── advagent/
│   │   ├── __init__.py
│   │   ├── advagent_window.py
│   │   ├── api_client.py
│   │   ├── office_connector.py
│   │   └── performance_monitor.py
│   ├── agent_workspace/
│   │   ├── config.json
│   │   └── workspace.py
│   ├── AI_chat/
│   │   ├── ai_chat.py
│   │   └── chat_history/
│   │       ├── chat_session_20241101_213342.json
│   │       ├── chat_session_20241101_213345.json
│   │       ├── chat_session_20241101_213346.json
│   │       ├── chat_session_20241101_225254.json
│   │       └── chat_session_20241101_225301.json
│   ├── floating_toolbar/
│   │   └── toolbar.py
│   ├── prompt_editor/
│   │   └── editor.py
│   ├── rag/
│   └── text_improver/
│       └── improver.py
├── utils/
│   ├── clipboard_utils.py
│   ├── lmstudio_client.py
│   ├── logger_utils.py
│   └── ollama_client.py
├── .gitignore
├── CHANGELOG.md
├── LICENSE
├── README.md
├── requirements.txt
└── run.py

```

## Key Elements

* **`run.py`**: Main application entry point. Sets up DPI awareness (especially for Windows), initializes the PyQt6 application, and runs the `LifAiHub` class. Handles cross-platform compatibility for DPI scaling.
* **`app_settings.json`**: Contains application-wide settings, including the last used model (`"last_model": "qwen2.5-7b-instruct"`) and backend (`"backend": "lmstudio"`).
* **`prompts.py`**: Defines a dictionary `default_prompts` containing pre-written prompts for various tasks (text correction, improvement, translation, summarization, analysis, etc.). Attempts to load user-defined prompts from `saved_prompts.py`, falling back to defaults if the file is not found or an error occurs. `improvement_options` list is derived from the keys of the loaded prompts.
* **`saved_prompts.py`**: Likely handles saving and loading user-defined prompts.
* **`app_hub.py`**: The central application hub. Initializes and manages various modules, handles settings (loading and saving from `app_settings.json`), provides a Tkinter-based UI, and configures logging. Uses Ollama and LMStudio clients for model interaction. Includes a debug log panel with controls for changing log levels, clearing logs, and saving logs to a file.
* **`advagent` module**: Implements a PyQt6-based advanced agent interface. Interacts with a backend API (likely for managing workspaces and sending/receiving messages), displays chat history, and provides performance monitoring.  The UI includes a workspace selector, chat display, message input, send button, and performance metrics display (GPU usage, VRAM usage, response times, success rate, token usage, and a response time graph). Uses custom logging.
* **`advagent_window.py`**: Implements the main window for the advanced agent, using PyQt6.  It interacts with a backend API to manage workspaces and handle chat messages.  Includes a performance monitoring section that displays GPU/VRAM usage, response times, success rate, and token usage. Uses custom logging and error handling.
* **`agent_workspace` module**:  Likely manages the user's workspace or context.
* **`AI_chat` module**: Handles AI chat functionality using PyQt6.  Manages user input, sends prompts to the Ollama client, displays responses, and manages chat history (saving and loading from JSON files). Includes file upload and progress bar features. Uses custom logging.
* **`ai_chat.py`**: Implements the AI chat window with a user-friendly interface using PyQt6.  Handles user input, sends prompts to the Ollama client, displays responses using custom message bubbles, and manages chat history (saving and loading from JSON files). Includes features for file uploads and a progress bar.  Uses custom logging for error handling and debugging.
* **`floating_toolbar` module**:  Implements a floating toolbar for easy access to features.
* **`prompt_editor` module**:  Provides an interface for editing prompts.
* **`text_improver` module**: Implements a PyQt6-based text improver window. Allows users to select from various text improvement options (defined in `prompts.py`), process text using the Ollama client, and display the results. Includes a rich text editor with formatting tools. Uses custom logging.
* **`improver.py`**: Implements the text improver window using PyQt6.  Provides a user interface with a rich text editor, improvement option selection, and processing functionality using the Ollama client.  Handles markdown conversion for output and includes error handling. Uses custom logging.
* **`utils` module**: Contains various utility functions. `ollama_client.py` provides a client for interacting with an Ollama server, with methods for fetching models and generating responses. Uses custom logging.  `lmstudio_client.py` provides a client for interacting with an LM Studio server, with methods for fetching models and generating responses. Includes error handling and logging.
* **`ollama_client.py`**: Provides a client for interacting with an Ollama server. It has methods for fetching available models and generating text responses using the Ollama API. Uses custom logging for error handling and debugging.
* **`lmstudio_client.py`**: Provides a client for interacting with an LM Studio server. It has methods for fetching available models and generating text responses using the LM Studio API. Includes error handling and logging.


## Further Analysis

A more detailed analysis would require inspecting the code within each module to understand the specific implementation details. This notebook provides a high-level overview of the project's structure and key components.
