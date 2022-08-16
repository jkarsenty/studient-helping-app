# studient-helping-app
Dashboard Application that allows School to help student in a better way. 

## Folder 
- data : contains data files
- infos : contains information files like the dataset description and goal of the application

## How to start

- To install the dependencies run :  
```
python -m pip install requirements.txt
```

- To build the app run :
```
docker build . -t school-app:0.1
```

- To start the app you run :  
```
docker run -p 8501:8501 school-app:0.1
```
