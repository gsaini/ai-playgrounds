# Optimizing Food Delivery Operations in New York

## Context

The number of food orders in New York is increasing daily. Many students and busy professionals rely heavily on food delivery services. A food aggregator company provides access to multiple restaurants through a single smartphone app. This app allows customers to browse restaurants, place orders, and track deliveries. Restaurants receive direct online orders through the app, and once an order is confirmed, a delivery person is assigned to pick up the order and deliver it to the customer.

The delivery process involves the following steps:
1. The delivery person receives the order details after confirmation.
2. They use the map to navigate to the restaurant to pick up the order.
3. After picking up the order, they use the map again to deliver the food to the customer.

This seamless process ensures that customers receive their food efficiently and on time.

## Objective

The food aggregator company has stored data for various online orders in their portal. They aim to analyze this data to gain insights into customer demand and restaurant performance. These insights will help the company enhance the overall customer experience by addressing key operational challenges and optimizing delivery services.

As a Data Scientist in this company, you have been tasked with analyzing the data to answer critical business questions shared by the Data Science team.

## Data Dictionary

The dataset contains the following fields:

- **`order_id`**: Unique identifier for each order.
- **`customer_id`**: Unique identifier for the customer who placed the order.
- **`restaurant_id`**: Unique identifier for the restaurant that received the order.
- **`cuisine_type`**: Type of cuisine ordered by the customer (e.g., Italian, Chinese, Indian).
- **`order_amount`**: Total monetary value of the order.
- **`day_of_week`**: Indicates whether the order was placed on a weekday (Monday to Friday) or a weekend (Saturday and Sunday).
- **`rating`**: Rating (out of 5) given by the customer for the order.
- **`food_preparation_time`**: Time (in minutes) taken by the restaurant to prepare the food. This is calculated as the difference between the timestamps of order confirmation and the restaurant's pickup confirmation.
- **`delivery_time`**: Time (in minutes) taken by the delivery person to reach the restaurant and deliver the food. This is calculated as the difference between the timestamps of the delivery person's pickup confirmation and the delivery of the order.

---

This detailed problem statement and data dictionary will guide your analysis and help you address the key questions posed by the Data Science team.