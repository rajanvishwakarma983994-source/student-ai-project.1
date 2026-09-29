"""A small offline study chatbot."""

import re


TOPICS = (
    ("hello|hi|hey", "Hello! Ask me about HTML, CSS, JavaScript, Python, AI, computers, the internet, Git, or studying."),
    ("html", "HTML structures web pages with headings, paragraphs, links, and images."),
    ("css", "CSS styles web pages with colors, fonts, spacing, and layouts."),
    ("javascript|js", "JavaScript adds interactivity to web pages, such as menus and dynamic content."),
    ("python", "Python is a beginner-friendly language used for apps, automation, data analysis, and AI."),
    ("ai|artificial intelligence", "AI enables computers to understand language, recognize patterns, and answer questions."),
    ("machine learning|ml", "Machine learning is a type of AI that learns patterns from data to make predictions."),
    ("computer", "A computer processes data according to instructions and produces results."),
    ("internet", "The internet connects computers worldwide and provides websites, email, and online services."),
    ("git|github", "Git tracks code changes; GitHub hosts and shares Git repositories online."),
    ("study|focus", "Study without distractions for 25 minutes, then take a 5-minute break. Repeat as needed."),
    ("math", "Solve math problems step by step: understand the question, note the values, choose a formula, and check your answer."),
    ("science", "Science uses observation and experiments to understand the natural world."),
)

TOPIC_LIST = "HTML, CSS, JavaScript, Python, AI, machine learning, computers, internet, Git, math, science, or studying"


def get_response(message):
    """Return an answer for a supported topic."""
    text = message.lower().strip()
    if re.search(r"(?<!\w)help(?!\w)", text):
        return f"I'm an offline chatbot. Ask me about {TOPIC_LIST}."

    for keywords, response in TOPICS:
        if any(re.search(rf"(?<!\w){re.escape(word)}(?!\w)", text) for word in keywords.split("|")):
            return response

    return f"I don't have an answer for that yet. Try asking about {TOPIC_LIST}."


def main():
    print("Student Study Bot (offline)")
    print("Ask about a topic, such as Python or math. Type 'bye' to quit.")
    while True:
        message = input("You: ").strip()
        if message.lower() in {"bye", "exit", "quit"}:
            print("Bot: Good luck with your studies. Bye!")
            break
        response = get_response(message) if message else "Type a question or 'help'."
        print(f"Bot: {response}")


if __name__ == "__main__":
    main()
