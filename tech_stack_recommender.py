import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Dataset: career roles with required skills
data = {
    "Role": [
        "Data Scientist",
        "Machine Learning Engineer",
        "Backend Developer",
        "Frontend Developer",
        "DevOps Engineer",
        "Cloud Engineer",
        "AI Engineer",
        "Cyber Security Analyst"
    ],
    "Skills": [
        "python statistics machine learning data analysis sql pandas numpy",
        "python machine learning deep learning tensorflow pytorch algorithms",
        "java python sql api database spring nodejs backend",
        "html css javascript react angular ui web design",
        "linux docker kubernetes aws ci cd automation deployment",
        "aws azure cloud docker kubernetes networking linux",
        "python artificial intelligence machine learning nlp deep learning",
        "network security linux encryption firewall ethical hacking"
    ]
}

df = pd.DataFrame(data)

print("===== Tech Stack Recommender =====")
print("Enter at least 3 skills/interests separated by commas")
print("Example: python, machine learning, sql\n")

user_input = input("Enter your skills/interests: ")

# Convert user input into same format as dataset
user_profile = user_input.replace(",", " ")

# Combine role skills + user profile
all_text = df["Skills"].tolist() + [user_profile]

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(all_text)

# Last row is user profile
user_vector = tfidf_matrix[-1]
role_vectors = tfidf_matrix[:-1]

# Cosine Similarity
similarity_scores = cosine_similarity(user_vector, role_vectors).flatten()

df["Similarity Score"] = similarity_scores

# Sort recommendations
recommendations = df.sort_values(by="Similarity Score", ascending=False)

print("\n===== Top 3 Recommended Career Paths =====\n")

for index, row in recommendations.head(3).iterrows():
    print(f"Role: {row['Role']}")
    print(f"Required Skills: {row['Skills']}")
    print(f"Similarity Score: {round(row['Similarity Score'] * 100, 2)}%")
    print("-" * 50)