# potato-leaf-diseases
## Dataset Content
(The dataset)[https://www.kaggle.com/datasets/warcoder/potato-leaf-disease-dataset/data] contains 3076 images taken in different conditions. Each image is in one of 7 health conditions: fungi, viruses, pests, bacteria, Phytophthora, nematodes and healthy.
For this Project we will be focussing on the 3 categories that are most important for Agriplex Farms (bacteria, Phytophthora and healthy)


## Business Requirements
Agriplex Farms is a mid-sized agricultural company specializing in growing and supplying potatoes to local and international markets. Over the past few years, the farm has faced significant challenges in maintaining the health of its crops due to various diseases affecting their potato plants, Caused by bacteria and phytophthora. These diseases, if left untreated, can devastate yields, resulting in financial losses and disrupted supply chains.

Currently, disease detection is carried out manually by agronomists walking through fields to inspect crops. This process is time-intensive and prone to human error. As a result, Agriplex Farms has identified an urgent need for a faster, more accurate, and scalable solution to detect diseases early, enabling timely interventions.

Agriplex Farms envisions leveraging Machine Learning (ML) to revolutionize their disease detection process. By deploying an ML-powered solution, the farm aims to:

- The client is interested in conducting a study to visually differentiate a healthy potato leaf from both disease causes.
- The client is interested in predicting whether a potato leaf is healthy or diseased, and if diseased, identifying the specific disease present.


## Hypothesis and how to validate?
* List here your project hypothesis(es) and how you envision validating it (them) 


## The rationale to map the business requirements to the Data Visualizations and ML tasks

### Business Requirement 1: Data Visualization
- We will display the mean and standard deviation images for healthy and diseased potato leaves.
- We will display the visual difference between average healthy and diseased potato leaves.
- We will create an image montage showcasing various healthy and diseased leaves, including examples of different disease types.

### Business Requirement 2: Classification
- We want to predict if a given potato leaf is healthy or diseased.
- We want to identify specific diseases if a potato leaf is classified as diseased.
- We will build a multi-class classifier to identify if a leaf is healthy or identify the disease.


## ML Business Case

### PotatoDiseaseDetection
- We want an ML model to predict whether a potato leaf is healthy or diseased. If diseased, the model should classify the specific type of disease.
- This is a supervised, multi-class, single-label classification problem.
- Our ideal outcome is to provide farm managers and agronomists with a faster and more reliable method for detecting potato diseases, enabling timely interventions and reducing crop losses.
- The model success metrics are:
    - F1-score of 85% or above for each class in multi-class classification.
    - A weighted average of 90% or better on the test set
- The model output is defined as a multiclass indicating the disease (or healthy) and the associated probabilities for each class. The prediction should enable real-time analysis of field images, therefore not in batches.

- Heuristics: Currently, disease identification relies on manual inspection by agronomists walking through fields. This process involves collecting leaf samples, visually examining them for discoloration, spots, or texture changes, and identifying diseases based on expertise. This method is time-intensive, error-prone, and not scalable across thousands of acres, leading to delayed responses and increased crop losses.

- Training Data:
The training data to fit the model comes from kaggle. This dataset contains images of potato leaves, labeled with the disease. Augmented versions of these images (e.g., flipped, rotated, adjusted brightness) are used to improve model robustness.

- Train data
    - target: healthy or disease type (multi-class label).
    - Features: images of potato leaves, including variations due to lighting, angles, and field conditions.


## Dashboard Design
### Page 1: Project Summary

- Project Summary
    - General Information
        - Potato diseases such as late blight, early blight, and bacterial black spot significantly threaten global potato production.
        - These diseases can cause discoloration, spotting, and texture changes in potato leaves, leading to reduced crop yield and financial losses for farmers.
        - Currently, disease detection involves manual inspection by agronomists, which is time-consuming, error-prone, and not scalable across large plantations.
        - Early and accurate detection of these diseases is crucial to reduce crop losses and optimize resource use, such as pesticides.
    - Project Dataset
        - The dataset contains thousands of labeled images of potato leaves, each image is labeled as healthy or a specific disease category.
        - Augmentation techniques (e.g., flipping, rotation, brightness adjustments) are applied to enhance the dataset’s variability and improve model robustness.
    - Business Requirements
        - The client is interested in conducting a study to visually differentiate between healthy and diseased potato leaves.
        - The client is interested in building a machine learning model to predict if a potato leaf is healthy or diseased and if diseased, the specific type of disease.


### Page 2: Cells Visualizer

- It will answer business requirement 1
    - input to choose a disease.
    - Checkbox 1 - Difference between average and variability image
    - Checkbox 2 - Differences between average healthy leaf and average leaf of the chosen disease
    - Checkbox 3 - Image Montage

### Page 3: Malaria Detector

- Business requirement 2 information - "The client is interested in predicting if a leaf is infected with a disease and if so, what disease"
- Link to download a set of potato leaf images for live prediction.
- User Interface with a file uploader widget. The user should upload multiple images. It will display the image and a prediction statement, indicating if the plant is healthy or what disease the plant is infected with and the probability associated with this statement.
- Table with the image name and prediction results.
- Download button to download table.

### Page 4: Project Hypothesis and Validation

- Block for each project hypothesis, describe the conclusion and how you validated it.

### Page 5: ML Performance Metrics

- Label Frequencies for Train, Validation and Test Sets
- Model History - Accuracy and Losses
- Model evaluation result




## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* Thank the people that provided support through this project.


https://stackoverflow.com/questions/73971025/how-to-do-data-augmentation-and-save-it-to-another-folder