import os

def generate_project_ideas():
    ideas = [
        "AI-powered chatbot for customer support",
        "Image recognition system for medical diagnosis",
        "Music recommendation system based on user preferences",
        "Autonomous drone navigation using computer vision",
        "Predictive maintenance system for industrial machinery",
        "Natural language processing for sentiment analysis",
        "Fraud detection system using machine learning",
        "Virtual reality simulation for training purposes",
        "Autonomous driving system for vehicles",
        "Personalized news recommendation system"
    ]
    return ideas

def create_ideas_file():
    file_path = os.path.join("docs", "ideas.md")
    ideas = generate_project_ideas()

    with open(file_path, "w") as file:
        for idea in ideas:
            file.write(f"- {idea}\n")

create_ideas_file()
