{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "570 6\n",
      "OH NO\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import math\n",
    "import random\n",
    "\n",
    "v0=100\n",
    "theta=0.5\n",
    "g=9.8\n",
    "a=2*v0*math.sin(theta)/g\n",
    "b=2*v0*math.sin(theta)/g*v0*math.cos(theta)\n",
    "t=np.arange(0,a,0.01)\n",
    "x=v0*(np.cos(theta))*t\n",
    "y=v0*(np.sin(theta))*t+1/2*(-g)*t**2\n",
    "aa=int(a)\n",
    "bb=int(b)\n",
    "pigx=random.randint(0,bb)\n",
    "pigy=random.randint(0,aa)\n",
    "plt.plot(x,y)\n",
    "plt.plot(pigx,pigy,\"o\")\n",
    "print(pigx,pigy)\n",
    "\n",
    "if pigx in x and pigy in y:\n",
    "    print('HITS')\n",
    "else:\n",
    "    print('OH NO')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.         0.87758256 1.75516512 2.63274769]\n",
      "4\n",
      "Hits!\n"
     ]
    }
   ],
   "source": [
    "pig_size = 3\n",
    "y = x[x<pig_size]\n",
    "print(y)\n",
    "print(np.shape(y)[0])\n",
    "if np.shape(y)[0]>0 :\n",
    "    print(\"Hits!\")"
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
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
