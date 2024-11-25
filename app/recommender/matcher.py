class Matcher:
    def __init__(self, user_profile, rules):
        self.user_profile = user_profile
        self.rules = rules

    def apply_forward_chaining(self):
        matched_rules = []

        for rule in self.rules:
            if self._matches(user_profile=self.user_profile, rule=rule):
                matched_rules.append(rule)

        return matched_rules

    def _matches(self, user_profile, rule):
        skills_match = any(skill in rule['skills'] for skill in user_profile['skills'])
        interests_match = any(interest in rule["interests"] for interest in user_profile['interests'])
        return skills_match or interests_match

