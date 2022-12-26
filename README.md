# **Course Recommendation System**


### **A Brief Introduction...**
A single platform that provides online educational content recommendations for all professional requirements with recommendations including courses from multiple sites
Problems with the Current recommendation system:
- Single platform
- General preferences
- Limited dataset, resulting in 
	- Inappropriate content
	- Inaccurate recommendation system
	- Ineffective in recommending
- Bad interaction, no good front page display


### **The Data**
Data is a small open dataset with courses from coursera found on kaggle. For additional metadata information, please refer to the dataset [**here**](https://www.kaggle.com/datasets/khusheekapoor/coursera-courses-dataset-2021).


### **Architecture & Design**
The application combines the use of Tailwind CSS, React, Bert, Flask API to provide real-time recommendation of courses.

![flowchart](common process_map.PNG)

Data is extracted from various online learning websites, pre-processed and then encoded using pre-trained BERT model. This matrix of vector represenation is saved and used to recommend similar courses based on cosine similarity. The matrix is stored so that ecoding doesn't need to be repeatedly performed again every time wewant to predict similar courses. The result is then fed to the front-end via a Flask API and shown to user. User enters course name or a keyword which is used to recommend similar courses with ranking given alongside it.


### **Functions & Components**
The following functions/components are available in the application:
- Users can enter a course from a list or a keyword to get recommended similar courses
- Data input is taken in and cosine simialrity is calculated from saved matrix represneation of encoded courses
- Courses are ranked based on similairty score and fed to front-end through Flask API as a json input
- Recommended courses are shown to user with their rankings and other details


### **Software & Tools**
The following software and tools were used to create this application:

**Software and Libraries**
- React 
- Tailwind CSS
- Python
    - Pandas
    - Numpy
    - Matplotlib
    - Seaborn
    - Requests
    - Flask
    - Hugging Face Bert

- Tools
    - Github
    - Git
    - Jupyter Notebook


## ***To view a demo of the application, click [here](https://drive.google.com/file/d/1hB8RYxFXCXPB5-pG7UXwCKUV-_z8JEYn/view?usp=sharing).***