# potato-leaf-diseases
## [Live Dashboard](https://potato-disease-detector-3dc8759c2d32.herokuapp.com)
## Dataset Content
[The dataset](https://www.kaggle.com/datasets/warcoder/potato-leaf-disease-dataset/data) contains 3076 images taken in different conditions. Each image is in one of 7 health conditions: fungi, viruses, pests, bacteria, Phytophthora, nematodes and healthy.
For this Project we will be focussing on the 3 categories that are most important for Agriplex Farms (bacteria, Phytophthora and healthy)


## Business Requirements
Agriplex Farms is a mid-sized agricultural company specializing in growing and supplying potatoes to local and international markets. Over the past few years, the farm has faced significant challenges in maintaining the health of its crops due to various diseases affecting their potato plants, Caused by bacteria and phytopthora. These diseases, if left untreated, can devastate yields, resulting in financial losses and disrupted supply chains.

Currently, disease detection is carried out manually by agronomists walking through fields to inspect crops. This process is time-intensive and prone to human error. As a result, Agriplex Farms has identified an urgent need for a faster, more accurate, and scalable solution to detect diseases early, enabling timely interventions.

Agriplex Farms envisions leveraging Machine Learning (ML) to revolutionize their disease detection process. Their main needs are:

- The client is interested in conducting a study to visually differentiate a healthy potato leaf from both disease causes.
- The client is interested in predicting whether a potato leaf is healthy or infected, and if infected, identifying the specific disease present.


## Hypothesis and how to validate?
- We suspect healthy plants are distinguishable from infected plants.
    - Doing a visual image study with Average Image, Variability Image, Difference between Averages and image montage should help

- We suspect bacteria infected plants have deviations in appearance and are therefore distinguishable from other plants.
    - Doing a visual image study with Average Image, Variability Image, Difference between Averages and image montage should help

- We suspect phytopthora infected plants have deviations in appearance and are therefore distinguishable from other plants.
    - Doing a visual image study with Average Image, Variability Image, Difference between Averages and image montage should help

- We suspect that a NN will be able to learn the differences between when a plant is Healthy, infected by bacteria or infected by phytopthora.
    - The model is able to differentiate these if it can get a weighted accuracy of 90% or more.


## The rationale to map the business requirements to the Data Visualizations and ML tasks

### Business Requirement 1: Data Visualization
- We will display the mean and standard deviation images for healthy and infected potato leaves.
- We will display the visual difference between average healthy and infected potato leaves.
- We will create an image montage showcasing various healthy and infected leaves, including examples of different disease types.

### Business Requirement 2: Classification
- We want to predict if a given potato leaf is healthy or infected.
- We want to identify specific diseases if a potato leaf is classified as infected.
- We will build a multi-class classifier to identify if a leaf is healthy or identify the disease.


## ML Business Case

### Potato infection detection
- We want an ML model to predict whether a potato leaf is healthy or infected. If infected, the model should classify the specific type of disease.
- This is a supervised, multi-class, single-label classification problem.
- Our ideal outcome is to provide farm managers and agronomists with a faster and more reliable method for detecting potato diseases, enabling timely interventions and reducing crop losses.
- The model success metrics are:
    - F1-score of 85% or above for each class in the multi-class classification.
    - A weighted accuracy of 90% or better on the test set.
- The model output is defined as a multiclass indicating the disease (or healthy) and the associated probabilities for each class. The prediction should enable real-time analysis of field images.

- Heuristics: Currently, disease identification relies on manual inspection by agronomists walking through fields. This process involves collecting leaf samples, visually examining them for discoloration, spots, or texture changes, and identifying diseases based on expertise. This method is time-intensive, error-prone, and not scalable across thousands of acres, leading to delayed responses and increased crop losses.

- Training Data:
The training data to fit the model comes from kaggle. This dataset contains images of potato leaves, labeled with the disease. Augmented versions of these images (e.g., flipped, rotated, adjusted brightness) are used to improve model robustness.

- Train data
    - target: healthy or disease type (multi-class).
    - Features: images of potato leaves, including variations due to lighting, angles, and field conditions.


## Dashboard Design
### Page 1: Project Summary

- Project Summary
    - General Information
        - Potato diseases significantly threaten global potato production.
        - These diseases can cause discoloration, spotting, and texture changes in potato leaves, leading to reduced crop yield and financial losses for farmers.
        - Currently, disease detection involves manual inspection by agronomists, which is time-consuming, error-prone, and not scalable across large plantations.
        - Early and accurate detection of these diseases is crucial to reduce crop losses and optimize resource use, such as pesticides.
    - Project Dataset
        - The dataset contains thousands of labeled images of potato leaves, each image is labeled as healthy or a specific disease category.
        - Augmentation techniques (e.g., flipping, rotation, brightness adjustments) are applied to enhance the dataset’s variability and improve model robustness.
    - Business Requirements
        - The client is interested in conducting a study to visually differentiate between healthy and infected potato leaves.
        - The client is interested in building a machine learning model to predict if a potato leaf is healthy or infected and if infected, the specific type of disease.


### Page 2: Leaves Visualizer

- It will answer business requirement 1
    - input to choose a disease.
    - Checkbox 1 - Difference between average and variability image
    - Checkbox 2 - Differences between average healthy leaf and average leaf of the chosen disease
    - Checkbox 3 - Image Montage

### Page 3: Disease Detector

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


## User stories

### Business Requirements and Hypothesis
#### Epic: Define Business Requirements and Hypothesis
- User Story: As a stakeholder, I want the README.md to include dataset details, business requirements, and the ML business case so that project goals are aligned with business needs.
- User Story: As a stakeholder, I want a project hypothesis page on the Streamlit dashboard to understand the research context and the expected outcomes of the project.

### Data Collection and Visualization
#### Epic: Collect and Visualize Data
- User Story: As a data scientist, I want to collect and clean data using the 01-data-collection.ipynb notebook to ensure high-quality input for modeling.
- User Story: As a data analyst, I want to visualize average variations and differences across diseases using the 02-data-visualization.ipynb notebook to gain insights into disease patterns.
- User Story: As a data analyst, I want to add an image montage so I can study the differences between the categories.

### Create Model and Improve its Performance
#### Epic: Build and Optimize Machine Learning Model
- User Story: As a researcher, I want to run and test early versions of the model (e.g., v1.1 to v1.3) to establish a performance baseline.
- User Story: As a researcher, I want to train and evaluate models iteratively (e.g., versions v2.1 to v2.4) to identify the best-performing version.
- User Story: As a machine learning engineer, I want to save models in .h5 format without the optimizer to improve model portability across environments.

### Design and Implement Streamlit Dashboard
#### Epic: Develop an Interactive Dashboard for Stakeholders
- User Story: As a stakeholder, I want a quick project summary page on the Streamlit dashboard to gain a high-level overview of the project's progress and results.
- User Story: As a user, I want a disease detector page on the dashboard to identify leaf diseases based on the model’s predictions.
- User Story: As a user, I want a leaves visualizer page to explore leaf images and their classifications interactively.
- User Story: As a stakeholder, I want an ML performance metrics page to review how well the model is performing.

## Bugs
### Fixed Bugs
* Large slug size
    - At first I could not upload the project to heroku due to a large slug size
    - After making a dedicated folder for image montage (200 x 200) sized images instead of the (1500, 1500) size and changing tensorflow to tensorflow-cpu in the requirements I was able to get it down to right below the 500mb alllowed size.

* Unbalanced Data
    - To balance the data better I used image augmentation with only horizontal and vertical flip filters to create a more balanced dataset.



## Deployment
### Heroku

* The App live link is: https://potato-disease-detector-3dc8759c2d32.herokuapp.com
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis and Machine Learning Libraries
### matplotlib
- Used to create the average and variability images in 02-data-visualization.ipynb

### numpy
- Used for various tasks in data manipulation such as getting the max value of a np array to determine the result of the prediction

### pandas
- used for its ability to store data in easily manageble dataframes (e.g. for the report in the detector page)

### tensorflow
- Used to create and train the model for Business Requirement 2

### Streamlit
- Used to create a quick and clean dashboard to present the data and model.

## Credits

### Technologies Used

#### Software and Web Applications Used

- [GitHub](https://github.com/): Used to store the project code after pushing from Git.
- [Heroku](https://www.heroku.com/): Used for deployment and hosting of the application.


### Help and Documentation
- Official Documentations: Provided extensive help and documentation on specific cases.
- [W3 Schools](https://www.w3schools.com): Offered documentation on basic concepts, which was very helpful.
- [Stack Overflow](https://stackoverflow.com): A valuable resource for troubleshooting problems and finding similar issues faced by others.
- [MDN Web Docs](https://developer.mozilla.org/en-US/): Provided well-written documentation to understand core concepts.
- [ChatGPT](https://chat.openai.com): Assisted in creating the scenario and textblocks, with all content reviewed and edited as needed.
- Walkthrough projects: provided a lot of demo code to start from.

### Media
- [Kaggle](https://www.kaggle.com/datasets/warcoder/potato-leaf-disease-dataset/data): provided the open-source dataset for the project