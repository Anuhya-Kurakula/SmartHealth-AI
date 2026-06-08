import requests


def search_web(query):

    try:

        # remove "who is"
        query = query.lower().replace("who is", "").strip()

        url = (
            "https://en.wikipedia.org/api/rest_v1/page/summary/"
            + query.replace(" ", "_")
        )

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            return data.get(
                "extract",
                "No information found."
            )

        return "No results found."

    except Exception as e:

        return str(e)