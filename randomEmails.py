import streamlit as st
from faker import Faker # can create fake names etc

fake = Faker()

def generate_emails(number_of_emails):
    emails = []
    for i in range(number_of_emails):
        email = fake.email()
        emails.append(email)
    return emails

#emails = generate_emails(10)
#print(emails)

st.title("Random Emails Generator")
num_of_emails = st.number_input("Please Enter The Number of Emails To Generate",
                                min_value=1, max_value=999, value=1, step=1)
button = st.button("Generate Emails")
if button:
    emails = generate_emails(num_of_emails)
    st.subheader('Generated Emails')
    for email in emails:
        st.write(email)

# libraries pip install streamlit faker
# to run please use terminal streamlit run randomEmails.py