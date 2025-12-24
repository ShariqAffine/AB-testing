def business_decision(control_mean, test_mean, p_value, alpha=0.05):
    if p_value < alpha:
        decision = "ROLL OUT TEST"
    else:
        decision = "KEEP CONTROL"

    return {
        "control_mean": round(control_mean, 4),
        "test_mean": round(test_mean, 4),
        "lift_percent": round(
            (test_mean - control_mean) / control_mean * 100, 2
        ),
        "decision": decision,
        "significant": p_value < alpha
    }
