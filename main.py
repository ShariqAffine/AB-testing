import json
from src.data_loader import load_data
from src.preprocessing import clean_data
from src.runner import run_ab_test

import logging

if __name__ == "__main__":
    print('loading control')
    control = clean_data(load_data("data/control_group.csv"))
    print('loaded control\n')
    print('\n loading test')
    test = clean_data(load_data("data/test_group.csv"))
    print('loaded test')

    result = run_ab_test(control, test)

    with open("outputs/ab_test_result.json", "w") as f:
        json.dump(result, f, indent=4)

    print("A/B test completed successfully")



logging.basicConfig(
    filename="logs/ab_test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
