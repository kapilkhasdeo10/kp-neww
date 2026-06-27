from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Training data: product reviews
reviews = [
    ("This product is amazing! I love it.", 1),
    ("great quality and fast shipping.", 1),
    ("excellent value for the price.", 1),
    ("loved it! highly recommend.", 1),
    ("Superb product, will buy again.", 1),
    ("Fantastic! Exceeded my expectations.", 1),
    ("Terrible product, very disappointed.", 0),
    ("worst purchase ever, do not buy.", 0),
    ("very disappointed, not worth the money.", 0),
    ("morrible experience, will not recommend.", 0)
]

texts, labels = zip(*reviews)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)
Y = list(labels)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=42)

clf = LogisticRegression()
clf.fit(X_train, Y_train)
print(f'Training Accuracy: {accuracy_score(Y_train, clf.predict(X_train))*100:.0f}%')

# Test on new reviews
new = ['This product is fantastic! I love it.', 'This is a terrible product.']

X_new = vectorizer.transform(new)
for review, prediction, prob in zip(new, clf.predict(X_new), clf.predict_proba(X_new)):
    sentiment = 'Positive' if prediction == 1 else 'Negative'
    confidence = max(prob) * 100
    print(f'[{sentiment} {confidence:.0f}%] {review[:45]}...')