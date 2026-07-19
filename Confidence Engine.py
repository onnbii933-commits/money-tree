class ConfidenceEngine:

    def score(self, probability):

        if probability > 0.85:
            return "HIGH"

        if probability > 0.65:
            return "MEDIUM"

        return "LOW"
