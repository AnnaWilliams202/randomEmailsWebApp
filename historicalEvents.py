import streamlit as st
import requests


def get_events(month,day):
    url = f'http://history.muffinlabs.com/date/{month}/{day}'
    response = requests.get(url)
    data = response.json()
    events = data['data']['Events']
    return events


st.title("Historical Events Viewer")
month = st.number_input("Please Enter The Month ('e.g 7 for July')",
                                min_value=1, max_value=12, value=1, step=1)
day = st.number_input("Please Enter The Day ('e.g 1 for 1st')",
                                min_value=1, max_value=31, value=1, step=1)
button = st.button('Show events')

if button:
    events = get_events(month,day)
    if events:
        st.subheader(f'Event List for {month}/{day}')
        for event in events:
            st.write(f'Year: {event["year"]}') # can be seen in special variables (PyCharm)
            st.write(f'Description: {event["text"]}')
            if event['links']:
                st.write(f"Link: {event['links'][0]['link']}")
            st.divider()

# libraries pip install streamlit requests
# to run please use terminal streamlit run hisoricalEvnts.py


