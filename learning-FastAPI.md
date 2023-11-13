## Resources
- [FastAPI Official Documentation](https://fastapi.tiangolo.com/)
- [Features of FastAPI](https://fastapi.tiangolo.com/features/)
- [Concurrency and async/await](https://fastapi.tiangolo.com/async/)
  - **async def** syntax for path operation functions
  - Concepts of **asynchronous code**, **concurrency**, **parallelism**
- [Python Type Hints](https://fastapi.tiangolo.com/python-types/) -- typing module
  - [Type hints cheat sheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)
- [FastAPI official tutorial](https://fastapi.tiangolo.com/tutorial/)


## Practice - Pre-requisites
1. Install Python 3.8+
2. Activate [Virtual Environment](https://www.tutorialspoint.com/python/python_virtual_environment.htm#:~:text=The%20utilities%20for%20activating%20and,placed%20in%20the%20scripts%20folder.&text=To%20enable%20this%20new%20virtual,bat%20in%20Scripts%20folder.&text=Note%20the%20name%20of%20the%20virtual%20environment%20in%20the%20parentheses.)
   1. For Windows
      - Use venv module available in python To create a new virtual environment
         ```python -m venv venv```
      - Enable the new virtual environment using
         ```cd venv\scripts```
         ``` ./activate```
      - *To deactivate the virtual environment if required
         ```deactivate```
3. Install dependencies from requirements.txt
   ```pip install -r requirements.txt```