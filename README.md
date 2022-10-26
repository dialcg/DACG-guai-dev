# Pair of numbers 

## Approach
Used the `permutations` function from `itertools` to generate a list of pairs `(List[(int, int)])` from all the possible combinations from the input list. Then, validated the sum of each combination that is equal to the given int from the query param. Once the condition is fulfilled, it returns the resulting pair. If the condition is not fulfilled, the execution of the loop will end and then will return a `None` result.

## Usage

- Create and activate your venv  
- Install requirements 
- Run the server with `uvicorn app:app --reload`

You can test the code using FastAPI docs:

```sh
http://localhost:8000/docs
```


## Lambda implementation steps

For simple projects, it's better to use the .zip approach to upload the code to lambda instead of using a container, to avoid unnecesary implementations and avoid the usage of AWS' container registry as well.

For this case, I'd create a pipeline with the next steps:
- Run quality check (pre-commit, PEP8, etc)
- Run tests 
- Create/update requirements file 
- Create the deployment package via pip and zip
- Updload to lambda via aws-cli





