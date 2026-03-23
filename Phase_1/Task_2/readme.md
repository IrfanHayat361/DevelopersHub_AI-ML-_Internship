# Task-02: Short-Term Stock Price Prediction

## Objective
Build a machine learning model to predict the **next day’s closing stock price** using historical market data.

---

## Dataset
- Source: Yahoo Finance
- Accessed via: `yfinance` Python library
- Stock selected: Apple Inc. (AAPL)
- Features used:
  - Open
  - High
  - Low
  - Volume
- Target variable:
  - Next day Close price

---

## Tools & Technologies
- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- yfinance

---

## Workflow
1. Fetch historical stock data using the Yahoo Finance API
2. Perform data cleaning and preprocessing
3. Shift closing prices to create a next-day prediction target
4. Train a Linear Regression model
5. Evaluate model performance using MAE, MSE, and RMSE
6. Visualize actual vs predicted closing prices

---

## Results
- The model captures short-term price trends reasonably well
- Performance degrades during high market volatility
- Suitable for educational and analytical purposes only

---

## Key Learnings
- Handling time-series financial data
- Regression modeling for continuous targets
- Working with real-world APIs
- Visualizing prediction performance

---

## Limitations
- Does not account for market sentiment or external events
- Not suitable for real trading or financial decision-making
- Assumes historical price patterns will repeat

---

## Conclusion
This project demonstrates a complete machine learning pipeline for time-series regression using real-world financial data. While not a production-ready trading system, it effectively showcases applied ML skills relevant to industry-level internships.

---

## Author
**Irfan Hayat**  
AI/ML Intern — DevelopersHub

