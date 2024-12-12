import requests
import json
import logging

class LMStudioClient:
    def __init__(self, base_url="http://localhost:1234/v1"):
        self.base_url = base_url

    def fetch_models(self):
        """
        Fetch available models from LM Studio API
        """
        try:
            response = requests.get(f"{self.base_url}/models")
            if response.status_code == 200:
                models_data = response.json()
                model_names = []
                for model in models_data.get('data', []):
                    model_id = model.get('id', '')
                    if model_id:
                        model_names.append(model_id)
                logging.info(f"Found {len(model_names)} models in LM Studio")
                return model_names if model_names else ["No models found"]
            else:
                logging.error(f"Failed to fetch models from LM Studio: {response.status_code}")
                return ["LM Studio connection error"]
        except Exception as e:
            logging.error(f"Error connecting to LM Studio: {e}")
            return ["LM Studio not running"]

    def generate_response(self, prompt, model=None, temperature=0.7):
        """
        Generate a response using LM Studio's API
        """
        try:
            messages = [{"role": "user", "content": prompt}]
            response = requests.post(
                f"{self.base_url}/chat/completions",
                json={
                    "messages": messages,
                    "temperature": temperature,
                    "stream": False
                }
            )
            response.raise_for_status()
            result = response.json()
            
            # Extract the response text from the completion
            if 'choices' in result and len(result['choices']) > 0:
                return result['choices'][0]['message']['content'].strip()
            else:
                raise Exception("No response content received from LM Studio")
                
        except Exception as e:
            logging.error(f"Error generating response from LM Studio: {e}")
            raise

    def chat_completion(self, messages, model=None, temperature=0.7):
        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                json={
                    "messages": messages,
                    "temperature": temperature,
                    "stream": False
                }
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logging.error(f"Error in LM Studio chat completion: {e}")
            raise 