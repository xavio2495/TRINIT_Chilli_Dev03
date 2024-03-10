import uuid
import csv

def generate_unique_id():
   return uuid.uuid4().hex[:16]  # Truncate to 16 characters for 64 bits

def store_data_in_csv(user_id,question_id,subject,tags,question,avail_ans,answer):
   with open('question_data.csv', 'a', newline='') as csvfile:
       csv_writer = csv.writer(csvfile)
       csv_writer.writerow([user_id,question_id,subject,tags,question,avail_ans,answer])

while True:
   user_id = input("Enter a user_id (or 'q' to quit): ")
   if user_id == "q":
       break
   subject = input("Enter a subject (Maths,Phy,Chem...): ")
   tags = input("Enter a subject tags (integral,trignometry,semiconductor): ")
   question = input("Type your question here: ")
   avail_ans=True if input("Do you know the solution for the above answer: (yes/no)")=='yes' else False
   answer=False
   if avail_ans ==True:
      answer=input("Type your solution: ")
   question_id = generate_unique_id()
   store_data_in_csv(user_id,question_id,subject,tags,question,avail_ans,answer)
