import pickle
from recommend import get_recommendations_1
import pandas as pd

def pred(title,n):
    df = pd.read_csv('Processed_Dataframe.csv')

    indices = pd.Series(df.index, index=df['Course Name']).drop_duplicates()

    with open('cosine_sim.pkl', 'rb') as file:
        # Call load method to deserialze
        similarity = pickle.load(file)
    
    course_name,course_id = get_recommendations_1(title, similarity,indices,df,n)
    print(course_name)
    print(course_id)
    json_dic = {}
    json_final_dic = {}
    c=1
    for i in course_id:
        json_dic = {}
        json_dic['Course Name'] = df['Course Name'].iloc[i] 
        json_dic['Course Description'] = df['Course Description'].iloc[i] 
        json_dic['Course URL'] = df['Course URL'].iloc[i] 
        json_dic['Skills'] = df['Skills'].iloc[i] 
        json_dic['University'] = df['University'].iloc[i] 
        json_dic['Course Rating'] = df['Course Rating'].iloc[i] 
        json_dic['Difficulty Level'] = df['Difficulty Level'].iloc[i] 
        json_dic['Rank'] = c
        c+=1
        json_final_dic[i] = json_dic
    
    return json_final_dic