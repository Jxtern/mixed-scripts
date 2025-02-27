import math

def count_text_stats(text):
    characters = len(text)
    words = len(text.split())
    paragraphs = text.count("\n") + 1 if text.strip() else 0
    
    reading_time_seconds = words / 3.33  # Average reading speed: 200 words per minute
    
    return {
        "Characters": characters,
        "Words": words,
        "Paragraphs": paragraphs,
        "Reading Time (seconds)": round(reading_time_seconds, 2)
    }

if __name__ == "__main__":
    text_input = input("Enter your text:\n")
    stats = count_text_stats(text_input)
    
    for key, value in stats.items():
        print(f"{key}: {value}")
