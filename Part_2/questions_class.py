class Question:
    def __init__(self, question_txt, question_lvl, answer_right, question_ask=False, answer_user=None):
        """
        Инициализация вопроса
        :param question_txt: текст вопроса
        :param question_lvl: уровень сложности вопроса
        :param answer_right: правильный ответ
        :param question_ask: задан ли вопрос
        :param answer_user: ответ пользователя.
        :param score: баллы за вопрос.
        """
        self.question_txt = question_txt
        self.question_lvl = question_lvl
        self.question_ask = question_ask
        self.answer_right = answer_right
        self.answer_user = answer_user
        self.score = int(self.question_lvl) * 10

    def get_points(self):
        """
        Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return int(self.score)

    def is_correct(self):
        """
        Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        return self.answer_user == self.answer_right

    def build_question(self):
        """
        Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f"Вопрос: {self.question_txt}\n" \
               f"Сложность {self.question_lvl}/5"

    def build_feedback(self):
        """
        Возвращает:
        Ответ верный, получено __ баллов
        либо
        Ответ неверный, верный ответ __
        """
        if self.is_correct():
            return f"Ответ верный, получено {self.get_points()} баллов"
        return f"Ответ неверный, верный ответ {self.answer_right}"
