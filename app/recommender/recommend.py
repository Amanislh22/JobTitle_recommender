from .matcher import Matcher
from .filters import Filter
from .ranker import Ranker

class Recommender:
    def __init__(self, user_profile, rules):
        self.user_profile = user_profile
        self.rules = rules

    def recommend_rules(self):
        matcher = Matcher(self.user_profile, self.rules)
        matched_rules = matcher.apply_forward_chaining()
        filter_ = Filter(self.user_profile,matched_rules)
        filtered_rules = filter_.apply_filters()
        ranker = Ranker(self.user_profile,filtered_rules)
        ranked_rules = ranker.rank_rules()

        return ranked_rules
