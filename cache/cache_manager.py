query_cache = {}


def get_cached_answer(question):

    return query_cache.get(question)


def save_to_cache(question, answer):

    query_cache[question] = answer