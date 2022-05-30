from config import MODUL

import json

import random

from faker import Faker
fake_ru = Faker("ru_RU")


def main():
    """

    :return: создает список словарей
    """

    for i in range(100):
        dict_[i] = [{'model': MODUL,
                     "fields": {"title": title_(), "year": year(), "pages": pages(), "isbn13": isbn(), "rating": rate(),
                                "price": price(), "author": name()}}]
        with open("result.txt", "w", encoding='utf-8') as f:
            json.dump(dict_, f, indent=4, ensure_ascii=False)


def title_() -> list:
    """

    :return: выбирает название книги из файла books.txt случайным образом
    """

    f = open('books.txt', encoding='utf-8')
    line = [m.strip() for m in f]
    line = random.choices(line)
    # print(line)
    return line

# title()


def year() -> int:
    """

    :return: случайноым орбазом выбирает год издания в заданных пределах
    """

    y = random.randint(1918, 2022)
#    print(y)
    return y

# year()


def pages() -> int:
    """

    :return: случайноым орбазом выбирает количество страниц в книге в заданных пределах
    """

    p = random.randint(100, 1000)
#    print(p)
    return p

# pages()


def isbn() -> list:
    """

    :return: случайноым орбазом выбирает isbn
    """

    # print(fake_ru.isbn13())
    return fake_ru.isbn13()

# isbn()


def rate() -> int:
    """

    :return: случайноым орбазом выбирает рейтинг издания в заданных пределах
    """

    r = random.randint(0, 5)
    # print(r)
    return r

# rate()


def price() -> float:
    """

    :return: случайноым орбазом выбирает цену издания в заданных пределах
    """

    pr = random.uniform(100, 1000)
    # print(pr)
    return round(pr,2)

# price()


def name() -> list:
    """

    :return: случайноым орбазом выбирает от одного до трех авторов для книги
    """
    list_ =[]
    nn = random.randint(1, 3)
    # print(nn)
    for i in range(0, nn):
        list_ += [fake_ru.name()]
    # print(line)
    return list_

# name()


if __name__ == "__main__":

    dict_ = {}
    main()



