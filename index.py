import random
import webbrowser

def generate_random_topic():
    ai_topics = [
        "artificial+intelligence",
        "machine+learning",
        "neural+networks",
        "deep+learning",
        "natural+language+processing",
        "computer+vision"
    ]
    return random.choice(ai_topics)

def main():
    for _ in range(5000):
        topic = generate_random_topic()
        search_url = f"https://www.bing.com/search?q={topic}"
        webbrowser.open_new_tab(search_url)

if __name__ == "__main__":
    main()
