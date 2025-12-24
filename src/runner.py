from src.metrics import add_conversion_rate
from src.statistics import run_stat_tests
from src.decision import business_decision

def run_ab_test(control_df, test_df):
    control_df = add_conversion_rate(control_df)
    test_df = add_conversion_rate(test_df)

    stats = run_stat_tests(
        control_df['conversion_rate'],
        test_df['conversion_rate']
    )

    decision = business_decision(
        control_df['conversion_rate'].mean(),
        test_df['conversion_rate'].mean(),
        stats['t_test_p_value']
    )

    return {
        "statistics": stats,
        "decision": decision
    }
