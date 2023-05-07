import os
import openai
import discord
# print(os.path.dirname(__file__))
# sys.path.append(os.path.join(os.path.dirname(__file__), "./app"))
from dotenv import load_dotenv
from autogpt.agent.agent_manager import AgentManager
from autogpt.cli import main
from autogpt.main import run_auto_gpt

# Load environment variables from .env file
load_dotenv()

AGENT_MANAGER = AgentManager()

# Load credentials from environment variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
model = os.getenv("FAST_LLM_MODEL")
token_limit = int(os.getenv("FAST_TOKEN_LIMIT"))
# Initialize OpenAI and Discord clients
openai.api_key = OPENAI_API_KEY
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = False
intents.messages = True

async def query_openai(prompts):
    response = openai.ChatCompletion.create(
        model=model,
        messages=prompts,
        max_tokens=token_limit - 1000, # leave 1000 for response
        temperature=0.5,
    )
    return response

class ChatBot(discord.Client):
    async def on_ready(self):
        print(f'We have logged in as {self.user}')
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        if self.user not in message.mentions:
            return 
        print(f'Message mention from author: {message.author}, mentions: {message.mentions}, \n content: {message.content}')
        input_content = message.content.replace(f'<@{self.user.id}>', '').strip()
        # prompts = [{"role": "user", "content": input_content}]
        # print(f'Prompts: {prompts}')
    

        await run_auto_gpt(continuous=True, skip_reprompt=True, continuous_limit=1, skip_news=True, ai_name="Super-gpt", ai_role="an AI designed to autonomously develop and run businesses with the", ai_goals=[input_content], ai_buget=0.1, discord_message=message)
       # response_text = await query_openai(prompts)
    #     print(f'Response from {model}: {response_text}')
    #    # assistant_response = response_text['choices'][0]['message']['content']
    #     await message.channel.send(response_text)

chatbot = ChatBot(intents=intents)

chatbot.run(DISCORD_TOKEN)
