def analyze_plan(df, name="DF"):
    print(f"\n===== {name} EXECUTION PLAN =====")
    df.explain(True)