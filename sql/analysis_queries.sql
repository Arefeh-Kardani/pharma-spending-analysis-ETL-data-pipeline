--Top pharmaceutical spending countries
SELECT location,
ROUND(SUM(total_spend)::NUMERIC, 2) AS total_spending
FROM cleaned_data
GROUP BY location
ORDER BY total_spending DESC
LIMIT 10;

--Spending trends over time
SELECT time,
ROUND(AVG(usd_cap)::NUMERIC, 2) AS avg_capital
FROM cleaned_data
GROUP BY time
ORDER BY time
LIMIT 10;

--Countries with highest pharma spending share of GDP
SELECT location,
ROUND(pc_gdp::NUMERIC, 2) AS percent_gdp
FROM cleaned_data
ORDER BY percent_gdp DESC
LIMIT 10;