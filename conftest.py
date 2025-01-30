import pytest 

def pytest_addoption(parser) : 
    parser.addoption('--email' , action = "store"  , default="alitalebishahroodi@gmail.com"  , help="email of user for login to quera  ")
    parser.addoption('--password' , action="store" , default="13781378ALI#t" , help="password to login to quera ")


