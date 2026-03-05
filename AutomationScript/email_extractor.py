# I developed a Python automation script that extracts valid email addresses 
# from a text file using regular expressions.
#The script removes duplicate emails and saves the cleaned data
#  into a separate output file automatically.
import re 
def extract_emails(input_file,output_file):
    try:
        with open(input_file, "r") as file:
            content = file.read()
        
        #regex pattern for valid emails
        pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+'

        # pattern = r'[a-ZA-Z0-9.%+-]z+@[a-XA-Z0-9.-]+\.[a-ZA-Z]+'
        emails =re.findall(pattern,content)

        unique_emails = list(set(emails))

        with open(output_file, "w") as file:
            for email in unique_emails:
                file.write(email + "\n")
        
        print("Emails extracted successfully")
        print(f"Total Unique Emails Found: {len(unique_emails)}")
        print("saved to:",output_file)

    except FileNotFoundError:
        print("Input file not found.")

if __name__ == "__main__":
    extract_emails("input.txt","extracted_emails.txt")
