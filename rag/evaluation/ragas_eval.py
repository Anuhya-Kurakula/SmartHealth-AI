from datasets import Dataset
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy
)

data = {
    "question": [
        "What is dengue?"
    ],

    "answer": [
        "Dengue is a viral disease transmitted by mosquitoes."
    ],

    "contexts": [[
        "Dengue fever is caused by dengue virus spread by Aedes mosquitoes."
    ]],

    "ground_truth": [
        "Dengue is a mosquito-borne viral disease."
    ]
}

dataset = Dataset.from_dict(data)

result = evaluate(
    dataset,
    metrics=[
        faithfulness,
        answer_relevancy
    ]
)

print(result)