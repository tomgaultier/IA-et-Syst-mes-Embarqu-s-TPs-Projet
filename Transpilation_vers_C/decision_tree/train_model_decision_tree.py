def build_model():
    
    import pandas as pd 
    from sklearn.tree import DecisionTreeClassifier
    import joblib
    
    df = pd.read_csv('predictive_maintenance.csv')
    
    X = df.drop(columns="has_break_three_month_later")
    y = df['has_break_three_month_later']
    
    model = DecisionTreeClassifier(random_state=42, max_depth=20)
    
    model.fit(X, y)
    
    joblib.dump(model, "decision_tree.joblib")
    
build_model()