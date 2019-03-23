# Data Cleaning

This repository shows off regularly encountered **Data Cleaning** tasks in the context of Data Science and Machine Learning projects. I want to expose a set of techniques I found out while learning Data Science throughout my personnal experience, and illustrate them thanks a randomly generated dataset, intentionally inserting errors and wrong data format.  
The following code in written in Python and mainly uses [Pandas](https://pandas.pydata.org/) and [Numpy](http://www.numpy.org/) libraries.

## 1) Dataset generation

In order to show a few Data Cleaning techniques, I needed to find a *"messy"* dataset, but messy in the way I could apply all the cleaning methods I wanted, while being sure I could show all of them, and explain them in an understandable way. Thus, I tried to look for an appropriate dataset but I could not find one of my taste. Therefore, I decided to **create my own dataset**, combining randomly generated elements with randomly introduced errors inside it.

Here is a subset of my randomly generated messy dataset, with its set of inherent problems :
![Initial messy dataset](images/initial_messy_dataset.png)

As you can see in this portion of the dataset, there are simply a lot of problems, missing values, wrong formats, useless data, etc. Thus I am going to use this awful dataset to illustrate some methods in my Data Cleaning process to cleanse it, and make it more appropriate for further use.

## 2) Data Cleaning pipeline

My Data Cleaning pipeline will consist in a tenth or less steps to mainly : delete useless observations or features, consider missing values differently, fill numerical features with the mean or the median of the corresponding feature, correct spelling mistakes, fix bad formatting, and so on... I am then describing below the errors or inconveniences I could face with this data, and how to solve them.

## 3) Dataset transformation

---

### TODO list

1. Handling missing values  
   - Deletion
     - [ ] Deleting useless observations (name : `useless_observation_deletion`)
     - [ ] Deleting useless features (missing : `useless_feature_deletion`)
   - Completion
     - Categorical
       - [ ] Treating missing values as a special category (category : `missing_value_as_special_category`)
     - Numerical
       - [ ] Filling with feature mean value (height : `mean_value_filling`)
       - [ ] Filling with feature median value (salary : `median_value_filling`)
2. Handling erroneous values
   - Spelling errors
     - [ ] Fixing with well formatted values (date : `good_format_spelling_correction`)
     - [ ] Fixing with known correct values (country : `known_value_spelling_correction`)
   - Value errors
     - [ ] Deleting strange observations (email : `strange_observation_deletion`)
     - [ ] Deleting strange features (useless : `strange_feature_deletion`)
