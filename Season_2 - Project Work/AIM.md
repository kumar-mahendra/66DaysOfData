# Disease-Predictor Application 

## Objective 
- Creating a ML Product which will help user to predict his/her disease solely on basis of his symptoms and not medical information that might be available all around. 

## Hypothesize Solution

### Visualize 
- solution will be a web-app which will provide relevent symptoms(options)  and user will select from those options to find his/her disease

### Understand 
- Currently I have seen only solution on github that just predict the disease by using ml model. Problem is it is of no use to user if user is not able to understand how to use model. also symptoms given in most of dataset are very medically oriented which if is available to user then why will he come of our platform. So we are trying to predict disease based on solely the signs/symptoms visible. 

### Design 

- **Automate Or Augment ?**  since we have only small dataset so we are planning to keep augmented model. 
- **UX constraints**  No of options to display is currently 10 . but it may change in future.
- **Technical constraints** we need to maintain low latency (< 100 ms) when providing our generated symptoms as options to user.


### Evaluation

- We are using accuracy as evalutaion criterion of model. 

## Iteration 
 
* Create a minimal viable product that satisfies a baseline performance [currently in progress ]
* Iterate solution by feedback 
* constantly reassess to ensure your objective hasn't changed.

* In our model we have initially started with random forest classifier model with some rule-based approach wherever possible.

* during montioring and iteration we are planning to look at overall performance of model as well as performance of particular classes . we will also try to find the optimum no of symptoms to be shown to user.










