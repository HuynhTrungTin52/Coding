import matplotlib.pyplot as plt 
import numpy as np
import re
from collections import Counter
import itertools as it
fig,ax=plt.subplots(3,3,figsize=(10,10))

ax[0,0].set_xlabel("Sepal length")
ax[0,0].set_ylabel("Sepal width")
x,y = np.loadtxt("Probability/lab09_524k0033/iris.csv", delimiter=",", unpack=True,skiprows=1,usecols=(0,1))
ax[0,0].scatter(x,y)
ax[0,0].set_title("1a")

ax[0,1].hist(x,bins=20)
ax[0,1].set_title("1b")

ax[0,2].remove()


ax[1,0].set_xlabel("Months")
ax[1,0].set_ylabel("Total profits")
x,y=np.loadtxt("Probability/lab09_524k0033/company-sales_data.csv", delimiter=",", unpack=True,skiprows=1,usecols=(0,7))
ax[1,0].plot(x,y)
ax[1,0].set_title("2a")

ax[1,1].set_ylabel("Shampoo Sales")
ax[1,1].set_xlabel("Months")
x,y=np.loadtxt("Probability/lab09_524k0033/company-sales_data.csv", delimiter=",", unpack=True,skiprows=1,usecols=(0,5))
ax[1,1].scatter(x,y)
ax[1,1].set_title("2b")


ax[1,2].set_xlabel("Months")
ax[1,2].set_ylabel("Profits")
x,y,z=np.loadtxt("Probability/lab09_524k0033/company-sales_data.csv", delimiter=",", unpack=True,skiprows=1,usecols=(0,1,2))
#y=cream,z=wash
ax[1,2].bar(x,y,color='pink',width=0.25)
ax[1,2].bar(x+0.25,z,color='b',width=0.25)
ax[1,2].legend(labels=["Facecream","Facewash"])
ax[1,2].set_title("2c")


ax[2,0].remove()
ax[2,2].remove()
gs = ax[2,1].get_gridspec()
ax[2,1].remove()
ax[2,1] = fig.add_subplot(gs[2, :])

text="As a Martial Art hunter, the majority of Ari's work revolves around (re)discovering forgotten martial arts, especially ones with historical and cultural value, or identifying smaller schools with potential. Additionally, Ari maintains the world's most comprehensively elaborate timeline regarding the heritage and parenting of martial arts, one that encompasses both general and specific successions dating back to estimates of possible hunting patterns used by Paleo-Sahertian Clovis hunter-gatherers. Art of Fist, or, more veridically, The Way of the Fist, is the most quotidian appellation of a martial artist's modus vivendi; and, as such, many have seen it fit to partake in the term's usage to denominate a particular fistic “style” of their own conception, which often than not seeks to avow its nature as a complete martial form, an art that delineates every facet of martial arts as a whole. I, Yoshitake Aritomo, declare these “styles” to be nothing more than a fraudulent endeavor, borne from the fruit of their creator's zeal, impudence, or, on occasion, both. No matter the “completeness” of a style, that is to say, the modern definition of completeness being the encapsulation of a vast variety of techniques that account for every possible situation, no singular art can totally capture “The Way of the Fist.” Before I prompt outrage in whoever may be reading this, and consequently trigger your putting down of this book prior to acquiring any of the information present within it, I feel the need to elaborate on my previous statement; I do not seek to either debate or contest the veracity of those styles' “completeness” within the aforementioned definition of the word, rather, I can attest to the fact that, when formed through the efforts of a reputed master, they most certainly fulfill the purpose for which they were created. Rather, the problem lies within the pursuit of a compilation of techniques therein which The Way can be defined; for technique is but one aspect of The Way, and can never truly capture its entire essence."
words=re.sub(r'[^\w\s]', '', text).lower().split()
dictionary = {}
for word in words:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary.update({word: 1})

sortedDict = dict(Counter(dictionary).most_common())
first_30 = dict(it.islice(sortedDict.items(), 30))
print(first_30)
ax[2,1].set_xlabel("Words")
x=list(first_30.keys())
ax[2,1].set_ylabel("Occurences")
y=list(first_30.values())
ax[2,1].plot(x,y)
ax[2,1].set_title("3")
ax[2,1].tick_params(axis='x', which='major', labelsize=5)
plt.tight_layout(pad=2.5)
plt.show()