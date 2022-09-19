from pydantic import BaseModel
# we will have description of the object that will be used for
# creation and reading of objects that will be either read of written in the database

'''
for writing to the database:
    1- we get the input from the api client
    2- we process this data to write it to the database
    3- use the creation schema to create the data to be written in the database
    4- write the data to database
    5- if we want to return the record we created,
    we return a schema that should be returned and not a schema for creation

for reading from the database:
    1- we get a specific request of data from the api client
    2- we get the data from the database
    3- we use the reading schema for the data that have to be return the client
    4- return the schema that describe the schema that have to be returned to the client

    *** important note:
    we should have a base schema. and two other schemas, one for reading and one for creation of records. They both inherit from base schema can have additional attributes.

    BaseSchema: this schema will fields that the other schemas have to inherit

    CreationSchema: fieds like the passoword or maybe a secret key have to be kept in the database not returned to the user.

    ReadingSchema: doesn't contain the secret attributes. It's the finale schema that have to be returned to the user.
    ***
'''


class RecommendationBase(BaseModel):
    nitrogen: int
    phosphorous: int
    potassium: int
    temperature: float
    humidity: float
    ph: float
    rainfall: float
    label: str
