from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
import math

from src.runner import run_ab_test
from app.schemas import ABTestResponse

app = FastAPI(
    title="A/B Testing Service",
    description="Production-ready A/B testing API",
    version="1.0.0"
)


def safe_float(value):
    """
    Ensures JSON-safe numeric values.
    Converts NaN / Inf to None.
    """
    if value is None:
        return None
    if isinstance(value, float) and (math.isnan(value) or math.isinf(value)):
        return None
    return value


@app.post("/ab-test", response_model=ABTestResponse)
async def ab_test(
    control_file: UploadFile = File(...),
    test_file: UploadFile = File(...)
):
    # -----------------------------
    # 1. Read uploaded CSV files
    # -----------------------------
    try:
        control_df = pd.read_csv(control_file.file, delimiter=";")
        test_df = pd.read_csv(test_file.file, delimiter=";")
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid CSV file format"
        )

    # -----------------------------
    # 2. Validate required columns
    # -----------------------------
    required_cols = {"# of Purchase", "# of Website Clicks"}

    if not required_cols.issubset(control_df.columns):
        raise HTTPException(
            status_code=400,
            detail="Control file missing required columns"
        )

    if not required_cols.issubset(test_df.columns):
        raise HTTPException(
            status_code=400,
            detail="Test file missing required columns"
        )

    # -----------------------------
    # 3. Run A/B test logic
    # -----------------------------
    try:
        result = run_ab_test(control_df, test_df)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"A/B test execution failed: {str(e)}"
        )

    # -----------------------------
    # 4. Return JSON-safe response
    # -----------------------------
    return {
        "control_mean": safe_float(result["decision"]["control_mean"]),
        "test_mean": safe_float(result["decision"]["test_mean"]),
        "lift_percent": safe_float(result["decision"]["lift_percent"]),
        "t_test_p_value": safe_float(result["statistics"]["t_test_p_value"]),
        "mann_whitney_p_value": safe_float(result["statistics"]["mann_whitney_p_value"]),
        "decision": result["decision"]["decision"],
        "statistically_significant": result["decision"]["significant"]
    }
