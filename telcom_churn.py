import pandas as pd
import math


def information_gain(feature, dataset):

    if feature == "tenure" or feature == 'MonthlyCharges' or\
            feature == 'TotalCharges' or feature=='Churn':
        return 0

    values = dataset[feature].unique()

    # Parent Entropy

    true_values = sum(dataset['Churn'] == True)

    total_obs = dataset.shape[0]

    p_positive = true_values / total_obs
    p_negative = 1 - p_positive

    entropy_parent = -(p_positive * math.log2(p_positive) + p_negative * math.log2(p_negative))

    # Information Gain

    IG = entropy_parent

    for i in values:
        temp_df = dataset[dataset[feature] == i]

        p_child = temp_df.shape[0]/total_obs

        true_values = sum(temp_df['Churn'] == True)

        p_positive = true_values / temp_df.shape[0]
        p_negative = 1 - p_positive

        # Entropy Calc
        entropy_child = -(p_positive * math.log2(p_positive) + p_negative * math.log2(p_negative))

        # Information Gain Calc
        IG = IG - (entropy_child*p_child)

    return IG

def load_clean_data():
    dataset = pd.read_csv("Data/Telco-Customer-Churn.csv")
    dataset = dataset.drop(["customerID"], axis=1)

    maping_Y_N = {'No': False, 'Yes': True}
    maping_list = ['Churn', 'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling']
    for i in maping_list:
        dataset[i] = dataset[i].map(maping_Y_N)

    data_top = dataset.columns
    for head in data_top:
        print("-------{}----------".format(head))
        print(dataset[head].unique())
        print('IG: {}'.format(information_gain(head,dataset)))
        print("\n")

    x = 1


if __name__ == '__main__':
    load_clean_data()
