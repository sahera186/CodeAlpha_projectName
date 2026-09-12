import re

def extract_emails(input_filename, output_filename):
    # Regex pattern to match standard email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    try:
        # 1. Read the input text file
        with open(input_filename, 'r') as file:
            content = file.read()

        # 2. Find all matching email addresses
        extracted_emails = set(re.findall(email_pattern, content))

        if not extracted_emails:
            print("No email addresses found in the file.")
            return

        # 3. Write extracted unique emails to an output file
        with open(output_filename, 'w') as file:
            for email in sorted(extracted_emails):
                file.write(email + '\n')

        print(f"Success! Extracted {len(extracted_emails)} unique email(s).")
        print(f"Saved results to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found. Make sure it is in the same folder.")

if __name__ == "__main__":
    # Specify your file names
    input_file = "sample_text.txt"
    output_file = "extracted_emails.txt"
    
    extract_emails(input_file, output_file)