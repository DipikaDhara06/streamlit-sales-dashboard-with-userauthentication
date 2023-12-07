import streamlit as st
import yaml
import os
import streamlit_authenticator as stauth
from streamlit_authenticator import Authenticate
from yaml import SafeLoader

#####

cwd = os.getcwd()
with open(cwd + '\\' + 'config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

##### Some defs #####

if authentication_status:
  authenticator.logout('Logout', 'main')
  with st.sidebar:
      st.write("HI")
    ### UI ELEMENTS
elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')