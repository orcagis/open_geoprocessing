from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get('/')
async def root():
    return{'message': 'Hello Bash!'}

# shapefiles and geodatabase feature classes require zip files
@app.post("/upload-file/")
async def create_upload_file(uploaded_file: UploadFile = File(...)):
    file_location = f"input/{uploaded_file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())
    return {"info": f"file '{uploaded_file.filename}' saved at '{file_location}'"}
