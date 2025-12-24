from pydantic import BaseModel

class ABTestResponse(BaseModel):
    control_mean: float
    test_mean: float
    lift_percent: float
    t_test_p_value: float
    mann_whitney_p_value: float
    decision: str
    statistically_significant: bool
