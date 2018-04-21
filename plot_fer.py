import os
import indicoio
import pandas as pd
import matplotlib.pyplot as plt

indicoio.config.api_key = os.environ.get('API_KEY')

# Batch request facial emotional recognition
res = indicoio.fer([
    '../../faces/alice-sad.jpg',
    '../../faces/alice-happy.jpg',
    '../../faces/aos-sad.jpg',
    '../../faces/aos-angry.jpg',
    '../../faces/aos-neutral.jpg',
    '../../faces/aos-happy.jpg'
])

# Pull each emotion separately
#angry, sad, neutral, surprise, fear, happy = [res[k] for k in ('Angry',
#                          'Sad',
#                          'Neutral',
#                          'Surprise',
#                          'Fear',
#                          'Happy')]

print(res)
# Plot data
p_df = pd.DataFrame(res)
p_df.plot()
plt.show()
