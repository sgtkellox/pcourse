import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def linePlot(data, path):
    data.plot()
    plt.savefig(path, mat="pdf", bbox_inches="tight")


def relPlot(data, path):
    npop_wide = pd.wide_to_long(df=data, j="id", i=["time"], stubnames="MO")
    sns.relplot(data=npop_wide, x="time", y="MO")
    plt.savefig(path)


def writeToFile(data, path):
    data.to_csv(path_or_buf=path)


def plotEuklidian(data, path):
    data.plot.bar()
    plt.savefig(path, format="pdf", bbox_inches="tight")
