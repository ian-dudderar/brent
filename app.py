import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

path = os.getenv('FILE_PATH')

df = pd.read_csv(fr'{path}')

print(df.to_string())