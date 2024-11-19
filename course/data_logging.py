# #Create a New File and Log Entries with Timestamps: Write a script that creates a new file named journal.txt.
# # type: ignore Prompt the user to enter a few lines of text as 'journal entries.'
# # For each entry, log the current date and time (using the datetime module) and the entry into journal.txt.
# # Each line in the file should have the format: [YYYY-MM-DD HH:MM:SS] Entry Text

# import datetime
# with open("journal.txt", "a") as file:
#     while True:
#         entry = input("Enter a journal entry: ") 
#         if entry.lower() == 'exit':
#             break
        
#         current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         file.write("[{current_time}] [{entry}]\n")
#         print("new entry log added into journal.txt file!")

# # f= open("journal.txt", "r")
# # for x in f:
# #     print(x)

# # f= open("journal.txt", "a")
# # import datetime
# # while True:
# #     entry = input("Enter a journal entry: ") 
# #     if entry.lower() == 'exit':
# #         break
# #     current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# #     f.write(f"[{current_time}] [{entry}]\n")
# #     print("new entry log added into journal.txt file!")

#count words and lines:
def counting_entries_and_lines():
    with open("journal.txt", "r") as file:
        lines = file.readlines()
    total_entries = len(lines)
    print(f"You have {total_entries} entries in your journal.")
    total_words = sum(len(line.split()) for line in lines)
    print(f"You have {total_words} words in your journal.") 

#add entries:
def add_entry():
    with open("journal.txt", "a") as file:
        import datetime
        while True:
            entry = input("Enter a journal entry: ") 
            if entry.lower() == 'exit':
                break
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{current_time}] [{entry}]\n") 
            print("new entry log added into journal.txt file!")
#add entries after yes or no:
# def add_entry_after_yes_or_no():
#     if more_entries.lower() == 'yes':
#         add_entry()
#     elif more_entries.lower() == 'no':
#         print("see you next time!")
#         break
#     else: 
#         print("please write yes or no")
          
counting_entries_and_lines()
add_entry()
import datetime
while True:
    more_entries = input("Do you want to add additional entries? (yes/no): ")
    if more_entries.lower() == 'yes':
        add_entry()
        print("new entry log added into journal.txt file! see you next time!")
        break
    
    elif more_entries.lower() == 'no':
        print("see you next time! \nlast time modified: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        break
    else:
        print("please write yes/no.")

