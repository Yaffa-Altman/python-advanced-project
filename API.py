import os
import string
import uvicorn
from pydantic import BaseModel
from starlette.responses import JSONResponse

from test import open_dir, problems_per_file
from graghs import all_graghs
from fastapi import FastAPI, HTTPException, UploadFile, File

app = FastAPI()

class File(BaseModel):
    path: str


# Create a new item
@app.post('/alerts')
def create_item(file: File):
    if not os.path.exists(file.path):
        raise HTTPException(status_code=400, detail="The path does not exist.")
    open_dir(file.path)
    return JSONResponse(content={"problems": problems_per_file}, status_code=200)

# Create a new item
@app.post('/analyze')
def create_item(file: File):
    if not os.path.exists(file.path):
        raise HTTPException(status_code=400, detail="The path does not exist.")
    all_graghs(file.path)
    images = [f'./images/number_of_issues_per_file.png',f'./images/pie_chart_number_of_issues.png',f'./images/histogram_functions_lengths.png']
    return JSONResponse(content={"images": images}, status_code=200)

# Run the server
if __name__ == '__main__':
    #app.run(debug=True)
    uvicorn.run('main:app', host='localhost', port=8000)
