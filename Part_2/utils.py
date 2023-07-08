import json
import os.path
from questions_class import Question


def load_questions(PATH):
    """
    Загружаем список заданий
    :param PATH: путь к json файлу
    :return: список экземпляров.
    """
    # переводим json file в python
    with open(PATH, encoding='utf-8') as file:
        data = json.load(file)

    # пустой список для записи списка экземпляров
    questions = []
    for element in data:
        questions.append(Question(element['q'], element['d'], element['a']))

    return questions


def get_statistics(questions):
    """
    Выводим статистику по игре
    :param questions: список экземпляров класса
    :return: статистику пользователя за игру
    """
    # счетчики
    score = 0
    count = 0

    # цикл на проверку корректности ответов
    for question in questions:
        if question.is_correct():
            score += question.score
            count += 1

    return f"Вот и всё!\n" \
           f"Отвечено {count} вопроса из {len(questions)}\n" \
           f"Набрано баллов: {score}"
