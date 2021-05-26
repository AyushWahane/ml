{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[76.6]])"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#importing pandas and LinearRegression\n",
    "import pandas\n",
    "from sklearn.linear_model import LinearRegression\n",
    "#reading database form xl file \n",
    "db = pandas.read_excel('Book.xlsx')\n",
    "#separating data\n",
    "mks = db[\"Marks\"]\n",
    "hrs = db[\"Hours\"]\n",
    "#creation of model\n",
    "mind = LinearRegression()\n",
    "mks = mks.values\n",
    "hrs = hrs.values\n",
    "mks = mks.reshape(4,1)\n",
    "hrs = hrs.reshape(4,1)\n",
    "#fitting data\n",
    "mind.fit(hrs, mks)\n",
    "#prediction\n",
    "mind.predict([[7]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
