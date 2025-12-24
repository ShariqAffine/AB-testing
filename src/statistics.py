import numpy as np
from scipy.stats import ttest_ind, mannwhitneyu


def run_stat_tests(control, test):
    # Guard clause: not enough data
    if len(control) < 2 or len(test) < 2:
        return {
            "t_test_p_value": None,
            "mann_whitney_p_value": None
        }

    # Welch's t-test
    t_stat, p_t = ttest_ind(
        test,
        control,
        equal_var=False
    )

    # Mann–Whitney U test
    _, p_mw = mannwhitneyu(
        test,
        control,
        alternative="two-sided"
    )

    return {
        "t_test_p_value": float(p_t) if not np.isnan(p_t) else None,
        "mann_whitney_p_value": float(p_mw) if not np.isnan(p_mw) else None
    }
