import uvicorn

def run_app():
    uvicorn.run("main:app", reload=True)

if __name__ == "__main__":
    run_app()