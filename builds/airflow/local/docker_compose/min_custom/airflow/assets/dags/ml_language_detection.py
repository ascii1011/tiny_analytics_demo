
"""
src: https://thecleverprogrammer.com/2021/10/30/language-detection-with-machine-learning/
"""

import pendulum
from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

# A DAG represents a workflow, a collection of tasks #
with DAG(dag_id="ml_language_detection", start_date=pendulum.datetime(2022, 11, 28, tz="UTC"), schedule=None) as dag:

    @task()
    def simple_ml():
        
        import pandas as pd
        import numpy as np
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.model_selection import train_test_split
        from sklearn.naive_bayes import MultinomialNB

        #data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/dataset.csv")
        file_path = "/opt/mnt/raw_data/dna/language_corpus_dataset.csv"
        print('++')
        print(f"{file_path=}")

        data = pd.read_csv(file_path)
        print('++')
        print(f"{data.head()=}")

        print('++')
        print(f"data is null? {data.isnull().sum()}")

        print('++')
        print(f"language counts: {data['language'].value_counts()}")


        # Language Detection Model
        # Now let’s split the data into training and test sets:
        x = np.array(data["Text"])
        y = np.array(data["language"])

        cv = CountVectorizer()
        X = cv.fit_transform(x)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, 
            test_size=0.33, 
            random_state=42)

        print('++')
        print(f"{X_train=}, {X_test=}, {y_train=}, {y_test=}")

        # As this is a problem of multiclass classification, 
        # so I will be using the Multinomial Naïve Bayes algorithm 
        # to train the language detection model as this algorithm 
        # always performs very well on the problems based on 
        # multiclass classification:
        model = MultinomialNB()
        model.fit(X_train,y_train)

        print('++')
        print(f"score: {model.score(X_test,y_test)}")

        # Now let’s use this model to detect the language of a text by taking a user input:
        ### sub user input for static value for now...

        #user = input("Enter a Text: ")
        #data = cv.transform([user]).toarray()

        words = 'hello there'
        print('++')
        print(f"{words=}")

        data = cv.transform([words]).toarray()
        output = model.predict(data)
        print('++')
        print(f"output:{output}")

        print('===end===')

    simple_ml()