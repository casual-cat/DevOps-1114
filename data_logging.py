#Create a New File and Log Entries with Timestamps: Write a script that creates a new file named journal.txt.
# type: ignore Prompt the user to enter a few lines of text as 'journal entries.'
# For each entry, log the current date and time (using the datetime module) and the entry into journal.txt.
# Each line in the file should have the format: [YYYY-MM-DD HH:MM:SS] Entry Text

# import datetime
# with open("journal.txt", "a") as file:
#     while True:
#         entry = input("Enter a journal entry: ") 
#         if entry.lower() == 'exit':
#             break
        
#         current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         file.write(f"[{current_time}] [{entry}]\n")
#         print("new entry log added into journal.txt file!")

# f= open("journal.txt", "r")
# for x in f:
#     print(x)

# f= open("journal.txt", "a")
# import datetime
# while True:
#     entry = input("Enter a journal entry: ") 
#     if entry.lower() == 'exit':
#         break
#     current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     f.write(f"[{current_time}] [{entry}]\n")
#     print("new entry log added into journal.txt file!")

f= open("journal.txt", "r")
