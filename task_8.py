# import logging

# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

# handler_error = logging.FileHandler('error.log', encoding='UTF-8')
# handler_error.setLevel(logging.ERROR)
# logger.addHandler(handler_error)

# def task7(companies: dict[str, tuple[list[int], list[int]]]) -> bool:
#     return all(sum(income) - sum(expense) > 0 for income, expense in companies.values())

# def main():
#     companies = {
#         "Сбербанк": ([2, 4, 2, 6, 1, 5], [1, 5, 1, 3, 5]),
#         "Банк ВТБ": ([2, 4, 2, 5, 2, 1, 5], [2, 3, 1, 6, 7]),
#         "Газпромбанк": ([2, 5, 1, 6, 2, 3], [2, 5, 1, 3, 7])
#     }

#     try:
#         result = task7(companies)
#         logger.info(f"Result of task7: {result}")
#     except Exception as e:
#         logger.exception("An exception occurred")

# if __name__ == "__main__":
#     main()



import logging


logger = logging.getLogger(name)
handler_error = logging.FileHandler('error.log', encoding='UTF-8')
handler_error.setLevel(logging.ERROR)
logger.addHandler(handler_error)

handler_info = logging.FileHandler('info.log', encoding='UTF-8')
handler_info.setLevel(logging.INFO)
logger.addHandler(handler_info)

if task7(companies= dict[str, tuple[list[int], list[int]]]) -> bool:
    return all(sum(income) - sum(expense) > 0 for income, expense in companies.values())

def main():
companies = {
"Сбербанк": ([2, 4, 2, 6, 1, 5], [1, 5, 1, 3, 5]),
"Банк ВТБ": ([2, 4, 2, 5, 2, 1, 5], [2, 3, 1, 6, 7]),
"Газпромбанк": ([2, 5, 1, 6, 2, 3], [2, 5, 1, 3, 7])
}

try:
    result = task7(companies)
    logger.info(f"Result of task7: {result}")
except Exception as e:
    logger.exception("An exception occurred")

if name == "main":
main()