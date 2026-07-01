# AI Recommendation System

recommendation_data = {
    "movies": {
        "action": ["Avengers", "John Wick", "The Dark Knight"],
        "comedy": ["3 Idiots", "Golmaal", "Jumanji"],
        "horror": ["The Conjuring", "Insidious", "Annabelle"],
        "romance": ["Titanic", "The Notebook", "La La Land"]
    },

    "books": {
        "technology": ["Python Crash Course", "Artificial Intelligence Basics", "Machine Learning with Python"],
        "fiction": ["Harry Potter", "The Hobbit", "The Alchemist"],
        "motivation": ["Atomic Habits", "Rich Dad Poor Dad", "Ikigai"]
    },

    "music": {
        "pop": ["Shape of You", "Perfect", "Flowers"],
        "rock": ["Believer", "Numb", "Thunder"],
        "classical": ["Moonlight Sonata", "Canon in D", "Four Seasons"]
    }
}

print("=" * 40)
print("     AI RECOMMENDATION SYSTEM")
print("=" * 40)

while True:

    category = input("\nEnter Category (movies/books/music): ").lower()
    interest = input("Enter Interest: ").lower()

    if category in recommendation_data:

        if interest in recommendation_data[category]:

            print("\nRecommended Items:")

            for item in recommendation_data[category][interest]:
                print("-", item)

        else:
            print("\nInterest not found!")

    else:
        print("\nCategory not found!")

    choice = input("\nDo you want another recommendation? (yes/no): ").lower()

    if choice != "yes":
        print("\nThank you for using the AI Recommendation System!")
        break