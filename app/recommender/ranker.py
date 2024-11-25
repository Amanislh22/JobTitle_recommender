class Ranker:
    def __init__(self,user_profile, filtered_rules):
        self.filtered_rules = filtered_rules
        self.user_profile = user_profile

    def rank_rules(self):
        ranked_rules = sorted(self.filtered_rules, key=self._calculate_match_score, reverse=True)
        return ranked_rules

    def _calculate_match_score(self, rule):
        score = 0
        if 'languages' in rule and 'English' in rule['languages']:
            score += 30
        if 'certifications' in rule and any(certif in rule["certifications"] for certif in self.user_profile['certifications']):
            score += 20
        return score

