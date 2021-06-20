import random

import pandas as pd
import csv


class DfIterator():
    def __init__(self, df, cols=None):
        if not cols:
            cols = df.columns
        self.df = df[cols]
        self.num_rows, self.num_cols = self.df.shape

    def sample_question(self):
        random_row = self.df.iloc[random.choice(range(self.num_rows))]
        question_idx, answer_idx = random.sample(range(self.num_cols), 2)
        question_col, answer_col = self.df.columns[question_idx], self.df.columns[answer_idx]

        question, answer = random_row.iloc[[question_idx, answer_idx]]

        return (question_col, question), (answer_col, answer)


# if __name__ == 'main':
ex_path = '/home/louis/Documents/Etudes/Langues/Anglais/Vocabulary.ods'

ex_df = pd.read_excel(ex_path)

print(ex_df.head())

df_iterator = DfIterator(ex_df, cols=['English', 'French'])

for i in range(10):
    print(df_iterator.sample_question())
