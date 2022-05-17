{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "2062675e",
   "metadata": {},
   "source": [
    "#### This tutorials is totally based on https://www.sharpsightlabs.com/blog/pandas-iloc/\n",
    "\n",
    "* Studying rapidly is good to go through this notebook, But Please have a look of this really good blog."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "51017c0f",
   "metadata": {},
   "source": [
    "#### 1. Importing Pandas a pd\n",
    "#### 2.  Setting up Data set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "23cdf70c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "country_data_dict = {\n",
    "    'country':['USA', 'China', 'Japan', 'Germany', 'UK', 'India']\n",
    "    ,'continent':['Americas','Asia','Asia','Europe','Europe','Asia']\n",
    "    ,'GDP':[19390604, 12237700, 4872137, 3677439, 2622434, 2597491]\n",
    "    ,'population':[322179605, 1403500365, 127748513, 81914672, 65788574, 1324171354]\n",
    "}"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b5a15a38",
   "metadata": {},
   "source": [
    "#### Converting Dict to Pandas DataFrame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4aff6ae2",
   "metadata": {},
   "outputs": [],
   "source": [
    "country_data_df = pd.DataFrame(country_data_dict, columns = ['country', 'continent', 'GDP', 'population'])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b86a3432",
   "metadata": {},
   "source": [
    "#### 1. Pandas Accessores\n",
    "```python\n",
    "   df.iloc[row:col]\n",
    "```\n",
    "\n",
    "* <strong>Example</strong>: Below, I am accessing 0 row all columns."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "62733698",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "country             USA\n",
       "continent      Americas\n",
       "GDP            19390604\n",
       "population    322179605\n",
       "Name: 0, dtype: object"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "country_data_df.iloc[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "071c905c",
   "metadata": {},
   "source": [
    "#### Accessing 5th Row by passing \n",
    "\n",
    "```python\n",
    "    df.iloc[row]\n",
    "```\n",
    "\n",
    "<b>Example</b>: Here <em>row</em> is 5."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "fb5bf509",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "country            India\n",
       "continent           Asia\n",
       "GDP              2597491\n",
       "population    1324171354\n",
       "Name: 5, dtype: object"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "country_data_df.iloc[5]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7e6b97c7",
   "metadata": {},
   "source": [
    "#### Accessing 0th row with little different way."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "1e4307ae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "country             USA\n",
       "continent      Americas\n",
       "GDP            19390604\n",
       "population    322179605\n",
       "Name: 0, dtype: object"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "country_data_df.iloc[0, :]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "01d3e7e6",
   "metadata": {},
   "source": [
    "#### Accessing first columns\n",
    "\n",
    "\n",
    "```python\n",
    "\n",
    "df.iloc[row:col]\n",
    "\n",
    "```\n",
    "\n",
    "```python\n",
    "df.iloc[:, col]\n",
    "```\n",
    "\n",
    "\n",
    "1. Here <em>row</em> have additional &quot;:&quot; to point out specific element in row."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "46c1ff8b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0        USA\n",
       "1      China\n",
       "2      Japan\n",
       "3    Germany\n",
       "4         UK\n",
       "5      India\n",
       "Name: country, dtype: object"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "country_data_df.iloc[:,0]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "031d82f3",
   "metadata": {},
   "source": [
    "#### Accessing 2nd row's 0th element."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "d38749d6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Japan'"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "country_data_df.iloc[2,0]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a38b182b",
   "metadata": {},
   "source": [
    "#### Subsetting: <span>Accessing 0 to 2nd row </span>\n",
    "1. Here \n",
    "\n",
    "```python\n",
    "df.iloc[start:end]\n",
    "```\n",
    "\n",
    "start - inclusive\n",
    "\n",
    "end - exclusive\n",
    "\n",
    "* 0th - element will be part of resulting dataset.\n",
    "* 3rd - element will be excluded from resulting data.\n",
    "\n",
    "* It will have elements from 0-2nd row only 3rd is excluded."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "7c1fb226",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>country</th>\n",
       "      <th>continent</th>\n",
       "      <th>GDP</th>\n",
       "      <th>population</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>USA</td>\n",
       "      <td>Americas</td>\n",
       "      <td>19390604</td>\n",
       "      <td>322179605</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>China</td>\n",
       "      <td>Asia</td>\n",
       "      <td>12237700</td>\n",
       "      <td>1403500365</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Japan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>4872137</td>\n",
       "      <td>127748513</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  country continent       GDP  population\n",
       "0     USA  Americas  19390604   322179605\n",
       "1   China      Asia  12237700  1403500365\n",
       "2   Japan      Asia   4872137   127748513"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "country_data_df.iloc[0:3]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3529ba20",
   "metadata": {},
   "source": [
    "#### Subsetting: Column\n",
    "\n",
    "1. Selecting all rows with subsetting in column.\n",
    "\n",
    "* Select 0th and 1st column from dataset.\n",
    "\n",
    "* Here also, second parameter which is <em>2</em> is exclusive."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "b266818d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>country</th>\n",
       "      <th>continent</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>USA</td>\n",
       "      <td>Americas</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>China</td>\n",
       "      <td>Asia</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Japan</td>\n",
       "      <td>Asia</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Germany</td>\n",
       "      <td>Europe</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>UK</td>\n",
       "      <td>Europe</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>India</td>\n",
       "      <td>Asia</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   country continent\n",
       "0      USA  Americas\n",
       "1    China      Asia\n",
       "2    Japan      Asia\n",
       "3  Germany    Europe\n",
       "4       UK    Europe\n",
       "5    India      Asia"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "country_data_df.iloc[:,0:2]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "76804a13",
   "metadata": {},
   "source": [
    "#### Even specific data subsetting\n",
    "\n",
    "1. Let's rewise once again.\n",
    "\n",
    "```python\n",
    "df.iloc[row:col]\n",
    "```\n",
    "\n",
    "```python\n",
    "df.iloc[start_row:end_row_exclusive, start_column: end_column_exclusive]\n",
    "```\n",
    "\n",
    "* Here we are selecting 1st to 4th rows and 0th to 2nd column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "3389e510",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>country</th>\n",
       "      <th>continent</th>\n",
       "      <th>GDP</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>China</td>\n",
       "      <td>Asia</td>\n",
       "      <td>12237700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Japan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>4872137</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Germany</td>\n",
       "      <td>Europe</td>\n",
       "      <td>3677439</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>UK</td>\n",
       "      <td>Europe</td>\n",
       "      <td>2622434</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   country continent       GDP\n",
       "1    China      Asia  12237700\n",
       "2    Japan      Asia   4872137\n",
       "3  Germany    Europe   3677439\n",
       "4       UK    Europe   2622434"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "country_data_df.iloc[1:5,0:3]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2057c7e3",
   "metadata": {},
   "source": [
    "#### Printing complete DataFrame."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "9c987ec1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>country</th>\n",
       "      <th>continent</th>\n",
       "      <th>GDP</th>\n",
       "      <th>population</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>USA</td>\n",
       "      <td>Americas</td>\n",
       "      <td>19390604</td>\n",
       "      <td>322179605</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>China</td>\n",
       "      <td>Asia</td>\n",
       "      <td>12237700</td>\n",
       "      <td>1403500365</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Japan</td>\n",
       "      <td>Asia</td>\n",
       "      <td>4872137</td>\n",
       "      <td>127748513</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Germany</td>\n",
       "      <td>Europe</td>\n",
       "      <td>3677439</td>\n",
       "      <td>81914672</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>UK</td>\n",
       "      <td>Europe</td>\n",
       "      <td>2622434</td>\n",
       "      <td>65788574</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>India</td>\n",
       "      <td>Asia</td>\n",
       "      <td>2597491</td>\n",
       "      <td>1324171354</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   country continent       GDP  population\n",
       "0      USA  Americas  19390604   322179605\n",
       "1    China      Asia  12237700  1403500365\n",
       "2    Japan      Asia   4872137   127748513\n",
       "3  Germany    Europe   3677439    81914672\n",
       "4       UK    Europe   2622434    65788574\n",
       "5    India      Asia   2597491  1324171354"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "country_data_df"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
