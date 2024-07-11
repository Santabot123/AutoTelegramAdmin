from crewai import Task

class Taskss_for_blogposts():
    def research_task(agent):
        return Task(
            description="""
            Search the internet for the {research_topic}.
            """,
            expected_output="""
            A details about {research_topic}.
            """,
            agent=agent
            )
    def write_task(agent):
        return Task(
            description="""
            Write a structured blog post using the information provided.
            Make it sound simple, and avoid complex words so it doesn't sound AI generated.
            Optimal length - {number_of_words} words.
            """,
            expected_output="""
            Cool and structured blog post.
            """,
            agent=agent
            )
    def image_resercher_task(agent,search_for):
        return Task(
            description=f"""
            Search the Internet for URL link to the images depicting {search_for}.
            """,
            expected_output="""
            One URL link to the image.
            example of output: https://example.com/pics/image.jpeg
            """,
            agent=agent
        )


class Taskss_for_topics():
    def news_researcher_task(agent):
        return Task(
            description="""
            Find some information about the {subject}.
            """,
            expected_output="""
            A details about {subject}.
            """,
            agent=agent
            )
    def analyst_task(agent):
        return Task(
            description="""
            Chose only one the most interesting topic. And if it is longer than 5 words, it should be summarized so that the length is 3-5 words.
            """,
            expected_output="""
            JUST ONE TOPIC. Without any explanation.
            """,
            agent=agent
            )

    def alt_analyst_task(agent):
        return Task(
            description="""
            Chose 3-5 the most interesting topics. And if it is longer than 5 words, it should be summarized so that the length is 3-5 words.
            """,
            expected_output="""
            LIST OF TOPICS. Without any explanation.
            example:
            1. Topic №1 
            2. Topic №2 
            3. Topic №3 
            """,
            agent=agent
        )


