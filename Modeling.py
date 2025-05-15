from sklearn.model_selection import KFold, GridSearchCV
from sklearn.preprocessing import FunctionTransformer, MinMaxScaler, StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error, r2_score
from sklearn.utils.validation import check_is_fitted
from sklearn.utils.multiclass import type_of_target
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.api.types import is_object_dtype
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from sklearn.utils.validation import check_is_fitted
from sklearn.utils.multiclass import type_of_target
import os
import re

visualization_result_dir = 'regression_plots'
os.makedirs(visualization_result_dir, exist_ok=True)


def plot_model_diagnostics(y_true, y_pred, degree, root_dir, model_name):
    residuals = y_true - y_pred

    model_dir = os.path.join(root_dir, model_name)
    os.makedirs(model_dir, exist_ok=True)

    fig, axs = plt.subplots(1, 3, figsize=(18, 5))
    # Regression Plot (Phi tuyến cho bậc > 1)
    x_plot = np.linspace(min(y_true), max(y_true), 500)
    coefficients = np.polyfit(y_true, y_pred, degree)
    poly_model = np.poly1d(coefficients)
    y_fit = poly_model(x_plot)

    axs[0].scatter(y_true, y_pred, alpha=0.6, label='Data')
    axs[0].plot(x_plot, y_fit, color='red', label=f'Degree {degree} Fit')
    axs[0].set_title(f"Regression Plot of {model_name}")
    axs[0].set_xlabel("Actual Values")
    axs[0].set_ylabel("Predicted Values")
    axs[0].legend()

    # Residual Plot
    sns.residplot(x=y_pred, y=residuals, lowess=True, ax=axs[1], line_kws={"color": "red"})
    axs[1].set_title(f"Residual Plot of {model_name}")
    axs[1].set_xlabel("Predicted Values")
    axs[1].set_ylabel("Residuals")

    # Distribution Plot
    sns.kdeplot(y_true, label='Actual', ax=axs[2])
    sns.kdeplot(y_pred, label='Predicted', ax=axs[2])
    axs[2].set_title(f"Distribution Plot of {model_name}")
    axs[2].set_xlabel("Value")
    axs[2].legend()
    plt.tight_layout()

    save_path = os.path.join(model_dir, f"{model_name}_diagnostics.png")
    plt.savefig(save_path)
    plt.show()


def build_models(df):
    label_encoders = {}
    for col in df.columns:
        if is_object_dtype(df[col]):
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str))
            label_encoders[col] = le
    df.columns = [re.sub(r'\W+', '_', col) for col in df.columns]
    X = df.drop(columns=['price'])
    y = df['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    models = {
        'linear_regression': LinearRegression(),
        'xgboost': XGBRegressor(objective='reg:squarederror', random_state=42),
        'random_forest': RandomForestRegressor(random_state=42),
        'lightgbm': LGBMRegressor(random_state=42)
    }

    result_rows = []

    for model_name, model in models.items():
        pipeline = Pipeline([('model', model)])

        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_test)

        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        mape = mean_absolute_percentage_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        plot_model_diagnostics(y_test, y_pred, 1, visualization_result_dir, model_name)

        result_rows.append({
            'model': model_name,
            'mse': mse,
            'rmse': rmse,
            'mape': mape,
            'r2': r2
        })

    result_df = pd.DataFrame(result_rows)
    return result_df

df = pd.read_csv("dataset.csv")
result = build_models(df)
print(result)

result.to_csv("model_result.csv")