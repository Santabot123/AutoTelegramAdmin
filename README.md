# What is AutoTelegramAdmin
This is a program for automatically writing posts in Telegram
# Quick start
### Prepare a Telegram bot

 1. Create a new bot
 2. Get the token of this bot
 3. Add this bot to your channel and give it the right to create new messages.

### Installation 

    git clone https://github.com/Santabot123/AutoTelegramAdmin.git
    cd AutoTelegramAdmin
    pip install requirements.txt

If you do not have [Ollama](https://ollama.com/), then install it.

    ollama pull mistral
    ollama pull openhermes
    ollama pull all-minilm
    
### Example

    from AutoTelegramAdmin.AutoTelegramAdmin import create_post
	
	create_post(  
	channel_name='@YOUR_CHANNEL_NAME',  
	token="YOUR_BOT_TOKEN",  
	number_of_words=50,  
	topic='description Bye Bye, Earth anime'  
	)


    
