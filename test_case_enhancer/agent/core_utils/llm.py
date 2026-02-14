import os
import sys
# Set up project root and add to sys.path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, PROJECT_ROOT)

# Import providers
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class GeminiFlashClient:
    """Legacy Gemini client for backward compatibility"""
    def __init__(self, api_key: str, model_name: str = "models/gemini-1.5-flash", system_prompt: str = "You are a helpful assistant."):
        if not GEMINI_AVAILABLE:
            raise ImportError("google-generativeai package not installed. Run: pip install google-generativeai")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)
        self.system_prompt = system_prompt

    def ask(self, user_prompt: str) -> str:
        """
        Sends a prompt to the model and returns the response.
        """
        prompt = f"{self.system_prompt}\n\nUser: {user_prompt}"
        response = self.model.generate_content(prompt)
        return response.text


class LLMClient:
    """
    Unified LLM client that supports both Gemini and OpenAI.
    """
    
    def __init__(
        self, 
        api_key: str, 
        provider: str = 'gemini',
        model_name: str = None,
        system_prompt: str = "You are a helpful assistant."
    ):
        """
        Initialize LLM client.
        
        Args:
            api_key: API key for the provider
            provider: 'gemini' or 'openai'
            model_name: Model name (auto-selected if not provided)
            system_prompt: System prompt for the model
        """
        self.provider = provider.lower()
        self.api_key = api_key
        self.system_prompt = system_prompt
        
        if self.provider == 'gemini':
            if not GEMINI_AVAILABLE:
                raise ImportError("google-generativeai package not installed. Run: pip install google-generativeai")
            self.model_name = model_name or "models/gemini-1.5-flash"
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel(self.model_name)
            
        elif self.provider == 'openai':
            if not OPENAI_AVAILABLE:
                raise ImportError("openai package not installed. Run: pip install openai")
            self.model_name = model_name or "gpt-4o"
            self.client = OpenAI(api_key=api_key)
            
        else:
            raise ValueError(f"Unknown provider: {provider}. Use 'gemini' or 'openai'")
    
    def ask(self, user_prompt: str, max_tokens: int = 4096) -> str:
        """
        Send a prompt to the model and return the response.
        
        Args:
            user_prompt: The prompt to send
            max_tokens: Maximum tokens in response
            
        Returns:
            Model's response as string
        """
        if self.provider == 'gemini':
            return self._ask_gemini(user_prompt)
        else:
            return self._ask_openai(user_prompt, max_tokens)
    
    def _ask_gemini(self, user_prompt: str) -> str:
        """Send prompt to Gemini"""
        prompt = f"{self.system_prompt}\n\nUser: {user_prompt}"
        response = self.model.generate_content(prompt)
        return response.text
    
    def _ask_openai(self, user_prompt: str, max_tokens: int) -> str:
        """Send prompt to OpenAI"""
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=max_tokens
        )
        return response.choices[0].message.content




