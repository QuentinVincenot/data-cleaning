# Data Cleaning

This repository shows off regularly encountered **Data Cleaning** tasks in the context of Data Science and Machine Learning projects. I want to expose a set of techniques I found out while learning Data Science throughout my personnal experience, and illustrate them thanks a randomly generated dataset, intentionally inserting errors and wrong data format.  
The following code in written in Python and mainly uses [Pandas](https://pandas.pydata.org/) and [Numpy](http://www.numpy.org/) libraries.

## 1) Dataset generation

In order to show a few Data Cleaning techniques, I needed to find a *"messy"* dataset, but messy in the way I could apply all the cleaning methods I wanted, while being sure I could show all of them, and explain them in an understandable way. Thus, I tried to look for an appropriate dataset but I couldn't find one of my taste. Therefore, I decided to **create my own dataset**, combining randomly generated elements with randomly introduced errors inside it.

## 2) Data cleaning pipeline

## 3) Dataset transformation

---

### TODO list

1. Dataset generation
   - Normal data
     - [ ] Create name column
     - [ ] Create missing column
     - [x] Create category column
     - [x] Create height column
     - [ ] Create salary column
     - [x] Create date column
     - [x] Create country column
     - [ ] Create email column
     - [x] Create useless column
   - Errors introduction
     - [ ] Generate null values in name column (`useless_observation_deletion`)
     - [ ] Generate lots of missing values in missing column (`useless_feature_deletion`)
     - [x] Generate null values in category column (`missing_value_as_special_category`)
     - [x] Generate null values in height column (`mean_value_filling`)
     - [ ] Generate null values in very heterogeneous salary column (`median_value_filling`)
     - [ ] Generate strangely formatted values in date column (`good_format_spelling_correction`)
     - [x] Generate miswritten country names in country column (`known_value_spelling_correction`)
     - [ ] Generate strange email suffixes in email column (`strange_observation_deletion`)
     - [x] Generate randomly generated text sequence in useless column (`strange_feature_deletion`)
2. Handling missing values  
   - Deletion
     - [ ] Deleting useless observations
     - [ ] Deleting useless features
   - Completion
     - Categorical
       - [ ] Treating missing values as a special category
     - Numerical
       - [ ] Filling with feature mean value
       - [ ] Filling with feature median value
3. Handling erroneous values
   - Spelling errors
     - [ ] Fixing with well formatted values
     - [ ] Fixing with known correct values
   - Value errors
     - [ ] Deleting strange observations
     - [ ] Deleting strange features
