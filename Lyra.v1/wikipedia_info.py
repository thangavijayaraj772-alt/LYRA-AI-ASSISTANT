import wikipedia
from speech import speak
def get_info(topic, lines=2):
    try:
        return wikipedia.summary(topic, sentences=lines)
    except wikipedia.DisambiguationError as e:
        speak(f"The topic '{topic}' has multiple meanings. For example: {', '.join(e.options[:3])}")
        return f"The topic '{topic}' has multiple meanings like: {', '.join(e.options[:5])}."
    except wikipedia.PageError:
        return "Sorry, I couldn't find any information."
    except Exception as ex:
        return f"An error occurred: {str(ex)}"
