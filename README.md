# callforecast Hackathon

Sponsored by Weber State University and Clear View Live Data  Analytics

Originally developed for a statistical modeling competition, which placed **3rd** overall. This repo demonstrates how to forecast call-center volume and average handle time (AHT) in 30-minute intervals using machine-learning and statistical methods.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Data](#data)
- [ ] 3.  TODO [Modeling Approach](#modeling-approach)
- [ ] 4.  TODO [Results](#results)     

---

## Project Overview

Call centers require accurate predictions of:
1. **Call Volume (CV):** How many inbound calls arrive in each 30-minute interval.
2. **Average Handle Time (AHT):** The average agent time spent on each call.

By forecasting these metrics, companies can:
- **Optimize staffing schedules** to reduce costs and wait times.
- **Identify performance trends** to guide agent training.
- **Improve infrastructure planning** and reduce idle agent time.

This codebase implements multiple models (including linear regression, GAM, and gradient boosting) to predict call volume and AHT using historical call-center data.

---

## Data
The dataset (`training.csv` and `test.csv`) contains:
- Timestamps of each call (`Call Start`)
- The length of time an agent spent on each call (`Agent seconds`)
- Other potential features like day of week, time of day, etc.

Data coverage:
- [ ] TODO 

> **Note:** For AHT, calls with 0 agent seconds were excluded from modeling (as these likely represent hangups before agent interaction).

---
