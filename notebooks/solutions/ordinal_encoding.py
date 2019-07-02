1. sklearn.preprocessing.OrdinalEncoder - Takes an array-like of strings or integers and creates an 
#                                         encoder to transform the data into an array of integer categories.
# sklearn.preprocessing.OneHotEncoder - Takes nominal data in an array-like and encodes into a binary array with
#                                       one place per feature.

#Extended Exercise

#1. Unsure, though it looks like if you 'fit()' a dataset and it's NOT already ordered correctly the function
#  will categorise the data, but not necessarily in the order you want?

#2. Using Customer survey data for value of primary residence from University of Michigan.
%run setup.ipy

import quandl
import my_secrets
quandl.ApiConfig.api_key = my_secrets.QUANDL_API_KEY

housing_prices = quandl.get("UMICH/SOC22-University-of-Michigan-Consumer-Survey-Current-Market-Value-of-Primary-Residence")
housing_prices = housing_prices.iloc[:,0:6] #Trim data down to price categories only
housing_prices

from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder

ord_enc = OrdinalEncoder()
ord_enc.fit(housing_prices)
ord_prices = ord_enc.transform(housing_prices)

hot_enc = OneHotEncoder(categories='auto')
hot_enc.fit(housing_prices)
hot_enc.transform(housing_prices).toarray()
