class word:
    def __init__(self, word, ex1, ex2, answer):
        self.word = word
        self.ex1 = ex1
        self.ex2 = ex2
        self.answer = answer
    
    def show_question(self):
        print(f'\"{self.word}\"の意味は?')
        print(f'1. {self.ex1}')
        print(f'2. {self.ex2}')

    def check_answer(self, user_input, correct_keys):
        if user_input == self.answer:
            print('正解です！')
            correct_keys.append(user_input)
            return correct_keys

        else:
            print('違います！')