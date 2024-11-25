from recommender.recommend import Recommender
import json
import csv

def load_facts():
    with open("/home/ameni/job-recommendation-system/app/data/facts.json", "r") as f:
        data = json.load(f)
        return data.get("user_profile", []) 


def load_rules():
    with open("/home/ameni/job-recommendation-system/app/data/rules.json", "r") as f:
        return json.load(f)

def load_rules():
    with open("/home/ameni/job-recommendation-system/app/data/rules.csv", "r") as f:
        reader = csv.DictReader(f)
        rules = []
        for row in reader:
            row["skills"] = set(row["skills"].split(","))
            rules.append(row)
        return rules

def load_user_profile(facts, user_id):
    """Load user profile from facts.json based on the given user ID."""
    return next((fact for fact in facts if fact.get("id") == user_id), None)



def main():
    print("Job Recommendation System")
    facts = load_facts()
    rules = load_rules()
    user_id = int(input("Enter user ID: "))
    
    user_profile = load_user_profile(facts, user_id)
    if not user_profile:
        print(f"No user found with ID {user_id}. Please try again.")
        return
    
    recommender = Recommender(user_profile, rules)
    recommended_rules = recommender.recommend_rules()

    print("\nRecommended rules:")
    if recommended_rules:
        for job in recommended_rules:
            print(f"- {job['title']} (Salary: ${job['salary']})")
    else:
        print("No suitable rules found.")

if __name__ == "__main__":
    main()
