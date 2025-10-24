# 🧮 Tech Layoffs Analysis Using Python

This project analyzes **global technology sector layoffs** to uncover patterns, trends, and underlying factors behind workforce reductions. The analysis explores variables such as **company size**, **location**, **industry type**, **layoff percentage**, and **funding stage** to derive meaningful insights into global tech downsizing events.

---
**App link**`
## 📘 Project Overview

- **Notebook:** `Techlayoff.ipynb`  
- **Dataset:** `tech_layoffs.csv`

### Objective
To understand and visualize the layoff patterns across different companies, regions, and industries, and identify potential factors contributing to large-scale layoffs.

### Key Highlights
- Performed **data cleaning and preprocessing**
- Handled **missing values** and **removed duplicates**
- Conducted **exploratory data analysis (EDA)** with rich visualizations
- Analyzed **trends over time and by geography**
- Identified **key insights** about tech layoffs globally

---

## 🧰 Technologies & Libraries Used

| Library | Purpose |
|----------|---------|
| **Pandas** | Data loading, cleaning, and manipulation |
| **NumPy** | Numerical computations |
| **Matplotlib & Seaborn** | Data visualization |
| **Plotly** | Interactive visualizations |
| **Scikit-Learn** | (Optional) Modeling or preprocessing tasks |
| **Jupyter Notebook** | Development and analysis environment |

---

## 🗃️ Dataset Description

| Column | Description |
|---------|-------------|
| **company** | Name of the company that conducted layoffs |
| **location** | Company’s headquarters or layoff location |
| **industry** | Sector or domain of the company |
| **total_laid_off** | Number of employees laid off |
| **percentage_laid_off** | Percentage of total employees affected |
| **date** | Date of layoff occurrence |
| **stage** | Company funding stage (e.g., Startup, Series A, Public) |
| **country** | Country where layoffs occurred |
| **funds_raised_millions** | Total amount of funds raised (in millions) |

---

## 🪜 Steps Performed

### 1. Data Preprocessing
- Loaded the dataset using **Pandas**
- Checked for **missing values** and **duplicates**
- Converted **date** column to proper `datetime` format
- Filled missing values appropriately
- Removed outliers and handled inconsistent categorical entries

### 2. Exploratory Data Analysis (EDA)
- Examined **total layoffs by year and month**
- Compared layoffs across **industries and countries**
- Identified **top 10 companies** with the highest layoffs
- Explored relationship between **percentage_laid_off** and **funds_raised_millions**
- Visualized data using **bar plots, line graphs, and heatmaps**

### 3. Visualization & Insights
- **Layoffs over time:** Detected spikes and recession periods in layoffs  
- **Industry-wise trends:** Highlighted sectors most affected by job cuts  
- **Geographical analysis:** Mapped countries/regions with highest layoffs  
- **Funding correlation:** Explored how financial backing impacts layoffs

---

## 📈 Key Insights

- Layoffs increased during periods of **economic slowdown** or **funding scarcity**  
- **Startups and early-stage companies** faced higher layoff rates due to funding constraints  
- **North America and Asia** experienced the most significant layoff waves  
- Industries like **Fintech, Cloud, and E-commerce** showed the largest fluctuations  

---

## 📊 Visualizations

Visualizations include:
- **Yearly Layoffs Trends**
- **Top 10 Companies by Layoffs**
- **Industry-Wise Comparison**
- **Layoffs by Country**
- **Funding vs Layoff Percentage Scatterplot**
- **Heatmap of Correlations**

---

## 🧠 Conclusion

This project provides data-driven insights into the dynamics of tech-sector layoffs worldwide.  
Findings indicate that global financial conditions, funding rounds, and industry cycles significantly influence workforce reductions. Companies at earlier funding stages tend to be more vulnerable, highlighting the importance of sustainable growth strategies in volatile markets.

---

## 🚀 How to Run the Project

1. Clone the repository:

