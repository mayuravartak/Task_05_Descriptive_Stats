
This project explores how accurately a Large Language Model (LLM) such as **ChatGPT** can interpret and reason over small structured datasets.

The goal is to:

1. Ask the LLM natural-language questions about the dataset.
2. Observe how it interprets the data and provides answers.
3. Verify the correctness of responses using manually computed descriptive statistics.
4. Reflect on its strengths, weaknesses, and reasoning process.

Dataset

The dataset comes from the public SU Women’s Lacrosse statistics page:  
[Cuse.com Women’s Lacrosse Stats](https://cuse.com/sports/2013/1/16/WLAX_0116134638)

All prompts are included in the `prompts_used.txt`.

The Python script `verification_code.py` calculates key metrics from a CSV file version of the dataset and the output is saved as `python_response.csv`

It’s used to **cross-check** whether the LLM’s answers match the actual computed results which are saved in `llm_response.txt`.

You can find the synthesized LLM response analysis in `llm_python_comparison.txt`
