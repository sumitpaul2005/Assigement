"""
Q1. List three apps you use daily (such as Zomato, Instagram, or Flipkart) and describe one feature in each app that likely uses machine learning. For each, state whether it is an example of supervised, unsupervised, or reinforcement learning.

Three Daily-Use Apps and Their Machine Learning Features

| App       | ML Feature                                                              | Learning Type          |
| --------- | ----------------------------------------------------------------------- | ---------------------- |
| Instagram | Recommends posts and reels based on our likes, interests, and activity. | Reinforcement Learning |
| YouTube   | Recommends videos based on watch history and user preferences.          | Supervised Learning    |
| Flipkart  | Recommends products based on previous searches and purchases.           | Unsupervised Learning  |

Explanation

1. Instagram: Learns which content users interact with and improves recommendations based on feedback.
2. YouTube: Uses user activity and viewing patterns to predict which videos users may like.
3. Flipkart: Groups users and products based on similar interests and shopping patterns.

Note: Real-world apps often combine supervised, unsupervised, and reinforcement learning in different features. These are simplified examples.

Q2. Given the following scenarios, classify each as supervised, unsupervised, or reinforcement learning: 1) Netflix recommending movies based on your watch history, 2) Spotify grouping similar songs into playlists, 3) A self-driving car learning to park by trial and error. Write your answers with a one-line explanation for each choice.

1\. Netflix recommending movies – Supervised Learning: Uses your watch history and preferences to predict which movies you may like.

2\. Spotify grouping similar songs – Unsupervised Learning: Groups songs based on similar features such as genre, rhythm, and tempo.

3\. Self-driving car learning to park – Reinforcement Learning: Learns through trial and error using rewards and penalties to improve parking.

Q3. Draw a simple diagram (hand-drawn or digital) showing the basic ML workflow: Data → Preprocessing → Modeling → Evaluation → Deployment. Under each step, write a one-line example of what happens at that stage for a food delivery app like Swiggy.

      DATA
        |
        v
  PREPROCESSING
        |
        v
    MODELING
        |
        v
   EVALUATION
        |
        v
   DEPLOYMENT
   
Explanation with Examples
1. Data: Collect customer orders, food preferences, ratings and delivery times from Swiggy.
2. Preprocessing: Remove duplicate records, handle missing values and clean the collected data.
3. Modeling: Train an ML model to recommend food based on customer preferences.
4. Evaluation: Check whether the model recommends relevant food correctly.
5. Deployment: Add the trained model to the Swiggy app so customers receive food recommendations.
Conclusion: Machine Learning helps Swiggy understand customer preferences and provide better food recommendations.

Q4. Imagine you are building a spam filter for WhatsApp messages. Write a short paragraph explaining how traditional programming would approach this problem versus how machine learning would approach it.<br><br><em><strong>Hint:</strong> Focus on rules vs learning from data.</em>

Traditional Programming: In traditional programming, we create fixed rules to identify spam messages, such as messages containing suspicious links, repeated words, or certain keywords. The computer follows these rules to detect spam.

Machine Learning: In machine learning, we provide the computer with many examples of spam and non-spam messages. The model learns patterns from the data and automatically predicts whether a new WhatsApp message is spam or not.

Main Difference: Traditional programming uses predefined rules, whereas machine learning learns patterns from data.
"""