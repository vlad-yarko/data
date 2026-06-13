import re

def find_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    return re.findall(pattern, text)

text = """
Contact us at support@example.com or sales@company.org.
For issues, email john.doe@test.co.uk or admin+tag@domain.io.
Invalid emails: user@, @domain.com, test@domain
"""

emails = find_emails(text)
print("Found emails:")
for email in emails:
    print(f"  {email}")
