from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 
import urllib
import requests
import numpy as np
#from PIL import Image
import imageio
      
comment_words = 'LOVE LOVE LOVE LOVE LOVE LOVE LOVE LOVE PYAAR ISHQ  ISHQ LOVE LOVE LOVE ISHQ CHAHAT ANPU AEJONG PREM PREM AEJONG LYUBOV LYUBOV PRITI PRITI TRESNA TRESNA AMOUR AMORE AMOR MOHABBAT MOHABBAT AFFECTION PREET AASHIQUI PYAAR CHAHAT PREM DILLAGI SNEH DILLAGI AFFECTION AASHIQUI LOVE PYAAR CHAHAT SNEH MOHABBAT AFFECTION AASHIQUI'
mask = np.array(Image.open(requests.get('http://www.clker.com/cliparts/3/d/9/1/11949847661568287344heart_jon_phillips_01.svg.med.png', stream=True).raw))

wordcloud = WordCloud(background_color ='black', 
                contour_width=0.1,
                contour_color='red',
                font_path='Roboto-Light.ttf',
                stopwords = STOPWORDS, 
                colormap='Reds_r',
                mask = mask).generate((comment_words)) 
  
# plot the WordCloud image                        
plt.figure(figsize=(8,6))

plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0.1) 
plt.savefig('python_heart.png')
