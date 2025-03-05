from corner import corner
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

def plot_relational_plot(df):
    """Generate a pair plot showing relationships between numerical features, colored by species."""
    sns.pairplot(df,hue='Species')
    plt.savefig('relational_plot.png')
    plt.close()
    return

def plot_categorical_plot(df):
    """Generate box plots for numerical features grouped by species."""
    numerical_cols = df.select_dtypes(include=np.number).columns
    df_melt = df.melt(id_vars='Species',value_vars=numerical_cols)
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='variable',y='value',hue='Species',data=df_melt)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('categorical_plot.png')
    plt.close()
    return

def plot_statistical_plot(df):
    """Generate a corner plot showing distributions and correlations of numerical features."""
    numerical_cols=df.select_dtypes(include=np.number).columns
    data = df[numerical_cols].values
    corner(data, labels=numerical_cols)
    plt.savefig('statistical_plot.png')
    plt.close()
    return

def statistical_analysis(df,col: str):
    """Calculate statistical moments for a specified column."""
    mean=df[col].mean()
    stddev=df[col].std()
    skew=ss.skew(df[col])
    excess_kurtosis=ss.kurtosis(df[col],fisher=True)
    return mean,stddev,skew,excess_kurtosis

def preprocessing(df):
    """Preprocess data by dropping the 'Id' column."""
    df.describe()
    df=df.drop('Id',axis=1)
    df.columns
    df.head()
    df.tail()
    return df

def writing(moments, col):
    """Print statistical results and interpret skewness/kurtosis."""
    print(f'For the attribute {col}:')
    print(f'Mean={moments[0]:.2f}, '
          f'Standard Deviation={moments[1]:.2f}, '
          f'Skewness={moments[2]:.2f}, and '
          f'Excess Kurtosis={moments[3]:.2f}.')
    
    skew=moments[2]
    if skew<-0.5:
        skew_dir='left'
    elif skew>0.5:
        skew_dir='right'
    else:
        skew_dir='not'
    
    kurt=moments[3]
    if kurt<-2:
        kurt_type='platykurtic'
    elif kurt>2:
        kurt_type='leptokurtic'
    else:
        kurt_type='mesokurtic'
    
    print(f'The data was {skew_dir} skewed and {kurt_type}.')
    return

def main():
    df=pd.read_csv(r'C:\Users\Lenovo\data.csv')  # Load dataset
    df=preprocessing(df)
    col='PetalLengthCm'  # Column chosen for analysis
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
    moments=statistical_analysis(df, col)
    writing(moments, col)
    return

if __name__ == '__main__':
    main()
