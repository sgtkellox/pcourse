import numpy as np


def dropCol(table, thresh):
    expec_df_flt = table.T[table.var() > thresh].T
    return expec_df_flt


def calcCorrelationMatrix(data):
    corr_data = data.corr(method="pearson", min_periods=1, numeric_only=False)
    return corr_data


def filterCorrelationMatrix(corr_matrix):
    corr_data_flt = corr_matrix.where(
        (np.triu(np.ones(corr_matrix.shape)).astype("bool"))
        & (~(np.tril(np.ones(corr_matrix.shape)).astype("bool")))
    )
    corr_data_flt = corr_data_flt.drop("time")

    corr_data_stacked = corr_data_flt.stack().reset_index()
    corr_data_stacked.columns = ["Cor_Row", "Cor_Column", "Correlation"]
    corr_data_stacked
    return corr_data_stacked


def euclideanDist(df1, df2, col1=["x_coord"], col2=["y_coord"]):
    return np.linalg.norm(df1[col1].fillna(0).values - df2[col2].fillna(0).values)
