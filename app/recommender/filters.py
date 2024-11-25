class Filter:
    def __init__(self, user_profile, recommended_rules):
        self.user_profile = user_profile
        self.recommended_rules = recommended_rules

    def apply_filters(self):
        filtered_rules = self._filter_by_salary(self.recommended_rules)
        filtered_rules = self._filter_by_experience(filtered_rules)
        return filtered_rules

    def _filter_by_salary(self, rules):
        return [rule for rule in rules if int(rule['salary']) >= int(self.user_profile['min_salary'])]
    
    def _filter_by_experience(self, rules):
        return [ rule for rule in rules if int(rules[0]['experience'] )<= int(self.user_profile["experience"])]

    

