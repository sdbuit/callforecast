# Statistical Hackathon

## Part 1

`training.csv` contains information on the volume of
inbound phone calls into the call center between 
April 1st and August 31st 2018. 

Project
    * Model the **call volume** (number of calls) and 
    * **Average Handle Time** (AHT)
        * average amount of time it takes an agent to handle the call.
        * Handle time is “Agent Seconds”

* **Call Volume** and **AHT** forecast should be broken out into 30 minute intervals.
  * Columns needed for this are `Call Start` and `Agent seconds`

* explanations for your model and analysis will be for the non-expert and aimed for an executive business meeting. 
 
* explain how you model the data (materials & methods) in a way that makes sense to non-experts, and you need to have a practical implication for the company.

**Other Details**

Complete the following predicted values for call volume and handle time for the following csv files: `answers_handletime.csv` Download answers_handletime.csv and `answers_volume.csv` Download answers_volume.csv. You need to fill the column Call.Volume and Handletime.

---

## Part 2: Statistical Analysis

Using `test.csv` and `training.csv`

**Task 1**

* why a transformation was used on the y-variable
* Explain why I created a variable called prime time for the input.
* Improve the model and consider interaction terms
* Calculate test MSE for your improved regression model
* Create a random forest (or a bag or boosted regression) for handle time
* Calculate MSE for the random forest

**Task 2**

Explain why I created a variable called prime time for the input.
Improve the model and consider interaction terms
State your final regression model and why interactions helped.
Calculate your test MSE for the call volume regression model
Create a regression tree
Prune your regression tree
Calculate your test MSE for your regression tree

---

**Environment Setup**

`uv init --name callforecast --python-preference only-managed -p 3.12`

`uv venv -p 3.12 --python-preference only-managed --system-site-packages`
