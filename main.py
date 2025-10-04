

from fastapi import FastAPI 
# from database import engine 
# import models 


# # Create tables 
# models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Interview Prep API")


@app.get("/")
def get(): 
    return { 
        "message": "Hello world", 
    }

@app.post("/")
def post(): 
    return { 
        "message": "Hello, this is the post command"
    }

@app.put("/")
def put(): 
    return { 
        "message": "Hello this is the put command"
    }


@app.delete("/")
def delete(): 
    return { 
        "message": "Hello this is the delete command"
    }