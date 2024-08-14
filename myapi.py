from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class API:
    def __init__(self):
        pass
    
    def sentiment_analysis(self, text):

        sentence = text

        analyzer = SentimentIntensityAnalyzer()
        response = analyzer.polarity_scores(sentence)
        return response
