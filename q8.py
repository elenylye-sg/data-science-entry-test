prompt_a = """
I am a marketing manager at a retail company and we have just finished 
a three-month campaign. My team has collected customer feedback through 
an online survey and we now have about 500 responses stored in a 
spreadsheet. Each response includes the customer's age group, the 
product they purchased, their satisfaction rating from 1 to 5, and a 
short written comment. I need to present the findings to our CEO next 
Friday in a way that is easy to understand. Can you analyse this data 
for me, highlight which age groups and products have the lowest 
satisfaction scores, identify the most common complaints from the 
written comments, and summarise everything in a short paragraph I can 
use as an executive summary?
"""

prompt_b = """
Role: You are a data analyst helping a retail marketing team.
Task: Analyse customer survey data from a 3-month campaign.
Data: 500 responses containing age group, product purchased, 
satisfaction rating (1-5), and written comments.
Steps:
1. Identify age groups and products with the lowest satisfaction scores.
2. Extract the most common themes from the written comments.
3. Summarise findings in an executive summary paragraph.
Audience: CEO presentation on Friday.
Constraints: Keep the summary concise and free of technical jargon.
"""

'''
prompt_a
I can do that, but I’ll need the spreadsheet data first.

Please upload the spreadsheet (Excel .xlsx, .csv, or similar), and I can:

Calculate overall satisfaction statistics.
Compare satisfaction scores by age group.
Compare satisfaction scores by product.
Identify the age groups and products with the lowest average ratings.
Analyze the written comments to find the most common complaint themes (for example: pricing, delivery, product quality, customer service, availability, etc.).
Highlight notable positive feedback as well.
Create CEO-friendly visuals and tables if you'd like.
Draft a concise executive summary suitable for your presentation.

Once you upload the file, I'll provide:

Key findings
Lowest-performing age groups
Lowest-performing products
Top complaint categories
Recommended actions
A short executive summary paragraph ready to paste into your presentation

If the data contains multiple sheets, I'll review all relevant sheets and explain how the conclusions were derived.
'''

'''
prompt_b
I can do that analysis, but I’ll need the actual survey data first.

Please upload or paste the data (CSV, Excel file, spreadsheet export, or a sample of the responses). Once I have it, I will:

Identify age groups and products with the lowest satisfaction ratings
Average satisfaction by age group
Average satisfaction by product
Highlight the lowest-performing segments
Extract common themes from written comments
Most frequent positive themes
Most frequent negative themes
Representative customer concerns and compliments
Create a CEO-ready executive summary
Concise, non-technical language
Focused on key findings and business implications
Suitable for a presentation slide

Preferred format: CSV or Excel with columns similar to:

Age Group
Product Purchased
Satisfaction Rating (1–5)
Comment

After you provide the dataset, I’ll return:

A findings table
Key comment themes
A concise executive summary paragraph ready for Friday’s presentation.
'''

# Task 1
# Read both prompts above carefully, then answer the questions below as comments.

# Q8a: Which prompt do you think will get a better response from an AI?
# Your answer:
# I think prompt_b give a better response from AI 

# Q8b: Give TWO reasons to support your choice.

# Your answer (Reason 1): 
# Able to hightlight positve and negative themes

# Your answer (Reason 2):
# Able to hightlight customer concerns

# Q8c: What is ONE strength of the prompt you did NOT choose?
# Your answer:
# Able to provide common complaint themes
# with example(for example: pricing, delivery, product quality)

# Task 2
# Rewrite either prompt by borrowing ONE element from the other
# to make it stronger. Explain what you borrowed and why.
# Your answer:
#
prompt_b = """
Role: You are a data analyst helping a retail marketing team.
Task: Analyse customer survey data from a 3-month campaign.
Data: 500 responses containing age group, product purchased, 
satisfaction rating (1-5), and written comments.
Steps:
1. Identify age groups and products with the lowest satisfaction scores.
2. Extract the most common themes from the written comments.
3. Identify the most common complaints from the written comments
4. Summarise findings in an executive summary paragraph.
Audience: CEO presentation on Friday.
Constraints: Keep the summary concise and free of technical jargon.
"""
#
#
# Borrowed item 3
# The reason being that the task is not just extract but also identify common
# complaints
#