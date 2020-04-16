import pandas as pd

def entropy(feature, dataset):

    values = dataset[feature].unique()

    for i in values:
        temp_df = dataset[dataset[feature]==i]

        True_values = dataset['Churn'] == True

        #p_positive =
        p_negative = 1- p_positive

def load_clean_data():
    dataset = pd.read_csv("Data/Telco-Customer-Churn.csv")
    dataset = dataset.drop(["customerID"], axis = 1)

    data_top = dataset.columns

    for head in data_top:
        print("-------{}----------".format(head))
        print(dataset[head].unique())
        print("\n")

    maping_Y_N = {'No':False, 'Yes':True}
    dataset = dataset['Churn'].map(maping_Y_N)

    entropy('gender', dataset)


    x=1

if __name__ == '__main__':
    load_clean_data()