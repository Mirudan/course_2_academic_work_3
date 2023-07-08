from utils import load_questions, get_statistics
import random
import os

PATH = os.path.join('data/questions.json')


def main():
    """
    Основная функция:
    выводит вопросы, принимает ответы, выводит статистику
    """
    # загружаем список экземпляров
    questions = load_questions(PATH)

    # перемешиваем список в случайном порядке
    random.shuffle(questions)

    # цикл на вывод вопросов и проверку ответов
    for question in questions:
        print(question.build_question())
        question.answer_user = input("Введите ваш ответ:\n").strip()
        print(question.build_feedback())

    print(get_statistics(questions))


if __name__ == '__main__':
    main()
