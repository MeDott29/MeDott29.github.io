import os

def create_project_plan():
    ideas_file_path = "ideas.md"
    plan_file_path = "plan.md"
    ideas = generate_project_ideas()

    with open(plan_file_path, "w") as plan_file:
        for idea in ideas:
            plan_file.write(f"Project Idea: {idea}\n")
            plan_file.write("Technologies: [Technologies involved]\n")

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
        "Personalized news recommendation system",
        "AI-powered project for audio engineering",
        "AI-based system for optimizing cable internet installation",
        "AI-driven lighting system for live events",
        "AI-powered analysis of ancient literature",
        "AI-assisted language learning program"
    ]
    return ideas

create_project_plan()
