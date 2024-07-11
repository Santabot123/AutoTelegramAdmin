from crewai import Agent


class Agents_for_blogposts():
    def researcher(tools,llm):
        return Agent(
            role='Researcher',
            goal='Search the internet for the information requested',
            backstory="""
            You are a researcher. You provide a lot of information thereby allowing a choice in the content.
            You can use a tool only once, so after that you should give a final answer.
            """,
            verbose=True,
            allow_delegation=False,
            tools=tools,
            llm=llm,
            memory=True,
            )

    def writer(llm):
        return Agent(
            role='Blog writer',
            goal='Write a cool blog post.',
            backstory="""
            You are a writer known for your humorous and structured way of writing short blog posts.
            You always follow this rules:
            - No greetings and goodbyes, just straight to the point
            - You never write about yourself
            - You never deviate from the topic
            - The text should be divided into short paragraphs.
            - You always use emojis
            """,
            verbose=True,
            allow_delegation=False,
            llm=llm
            )

    def image_resercher(tools,llm):
        return Agent(
            role=
            'picture finder',
            goal=
            'Search for image on the Internet and provide link to it.',
            backstory=
            "You are a researcher. Using the information from the task, find image and provide link to it.",
            tools=tools,
            llm=llm,
            verbose=True,
            allow_delegation=False
            )

class Agents_for_topics():
    def news_researcher(tools,llm):
        return Agent(
            role='Researcher',
            goal='Search the internet.',
            backstory="""
            You are a researcher. You provide a lot of information thereby allowing a choice in the content.
            You can use a tool only once, so after that you should give a final answer.
            """,
            verbose=True,
            memory=True,
            allow_delegation=False,
            tools=tools,
            llm=llm
            )

    def analyst(llm):
        return Agent(
            role='Analyst',
            goal='Analyze the information provided and choose one topic.',
            backstory="""
            You are an experienced analyst, you are very intelligent, also you are an expert in all fields.
            """,
            verbose=True,
            allow_delegation=False,
            llm=llm
            )
