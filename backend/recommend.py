def get_recommendations_1(title, cosine_sim,indices,df,n):
    idx = indices[title]
    #print(idx)
    sim_scores = list(enumerate(cosine_sim[idx]))
    #print(sim_scores)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:n+1]
    courses = [i[0] for i in sim_scores]
    
    return df['Course Name'].iloc[courses],courses