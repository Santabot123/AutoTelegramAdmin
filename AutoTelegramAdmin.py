import os
from poster import Telegram_potser
from crewai import Crew
from tools import  Tools_handler
from agents import Agents_for_topics, Agents_for_blogposts
from tasks import Taskss_for_topics, Taskss_for_blogposts
from langchain_community.llms import Ollama
from similarity import get_similarity_score,add_new


mistral_llm = Ollama(model="mistral")
openhermes_llm = Ollama(model="openhermes")

def create_topic(subject:str):
    ddsearch=Tools_handler.search()
    news_researcher=Agents_for_topics.news_researcher(tools=[ddsearch],llm=openhermes_llm)
    analyst=Agents_for_topics.analyst(llm=mistral_llm)

    news_researcher_task=Taskss_for_topics.news_researcher_task(agent=news_researcher)
    analyst_task=Taskss_for_topics.analyst_task(agent=analyst)
    # analyst_task = Taskss_for_topics.alt_analyst_task(agent=analyst)

    topic_crew= Crew(
        agents=[news_researcher,analyst],
        tasks=[news_researcher_task,analyst_task],
        verbose=2,
    )

    topic= topic_crew.kickoff(inputs={
    "subject" : subject
    })
    return topic

def create_caption(topic,number_of_words):
    ddsearch = Tools_handler.search()
    researcher = Agents_for_blogposts.researcher(tools=[ddsearch],llm=openhermes_llm)
    writer=Agents_for_blogposts.writer(llm=mistral_llm)

    researcher_task=Taskss_for_blogposts.research_task(agent=researcher)
    writer_task=Taskss_for_blogposts.write_task(agent=writer)

    blogpost_crew= Crew(
        agents=[researcher, writer],
        tasks=[researcher_task, writer_task],
        verbose=2,
    )
    content = blogpost_crew.kickoff(inputs={
        'research_topic': topic,
        'number_of_words' : number_of_words,
    })
    return content

#Find image
def find_image(topic:str) -> str:
    ddsearch_for_image=Tools_handler.search_for_imahes()
    image_resercher=Agents_for_blogposts.image_resercher(tools=[ddsearch_for_image],llm=openhermes_llm)
    image_resercher_task=Taskss_for_blogposts.image_resercher_task(agent=image_resercher,search_for=topic)

    image_url = image_resercher_task.execute()
    return image_url

def create_post(channel_name:str, token:str, number_of_words:int, channel_theme:str = None,topic= None):
        os.environ["TELEGRAM_POSTER_TOKEN"]=token
        if topic == None:
            similarity=1
            bad_topics='\n - Empty topic'
            while similarity >0.5 :
                topic = create_topic(subject=channel_theme+" Note: Don't answer with:"+bad_topics)
                similarity=get_similarity_score(topic,'all-minilm:33m','./chroma_db')
                if similarity>0.5:
                    bad_topics=bad_topics + "\n - " +  topic
                print(f'____________________________Created topic with simularity {similarity}______________________________')

            add_new(topic,'all-minilm:33m','./chroma_db')
            print(f'_________________________________Added new topic :{topic}_______________________________________________')

        caption = create_caption(topic=topic, number_of_words=number_of_words)
        while len(caption) > 1024:
            number_of_words = number_of_words - 5
            caption = create_caption(topic=topic)

        image_url = find_image(topic=topic)

        result = Telegram_potser(channel_name=channel_name, image_url=image_url, content=caption)
        return result, image_url, caption


# if __name__ == '__main__':
#
#
#     create_post(
#         channel_name='@YOUR_CHANNEL_NAME',
#         token="YOUR_BOT_TOKEN",
#         number_of_words=50,
#         topic='description Bye Bye, Earth anime'  # PUT YOUR OWN TOPIC HERE
#     )
