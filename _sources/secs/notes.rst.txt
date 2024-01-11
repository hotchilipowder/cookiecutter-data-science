
=====
Notes
=====


Why this project
========================

First, I have this project based on \ `cookiecutter-data-science <https://drivendata.github.io/cookiecutter-data-science/>`_ .
I have added some common tools used in my research projects, like :doc:`dockers </secs/dockers>`, \ `sphinx doc <https://hotchilipowder.github.io/my_config/docs/sphinx.html>`_

I have following notes for the source prject(2024-01-09):

* Data is immutable: by default, the data folder is included in the \ :code:`.gitignore`\ file 

* Notebooks are for exploration and communication: :code:`<step>-<ghuser>-<description>.ipynb` (e.g., :code:`0.3-bull-visualize-distributions.ipynb`)

  .. code-block:: bash
  
     # OPTIONAL: Load the "autoreload" extension so that code can change
     %load_ext autoreload

     # OPTIONAL: always reload modules so that as you change code in src, it gets loaded
     %autoreload 2

     from src.data import make_dataset
  
* Build from the environment up: just use \ :code:`virtualenv`\

  .. code-block:: bash
  
     virutalenv venv
     source venv/bin/activate
     pip install -r requirements.txt
     pip freeze > requirements.txt

* Keep secrets and configuration out of version control: just use \ :code:`.env`\ to keep your key and secrets

 .. code-block:: bash
 
    DATABASE_URL=postgres://username:password@localhost:5432/dbname
    AWS_ACCESS_KEY=myaccesskey
    AWS_SECRET_ACCESS_KEY=mysecretkey
    OTHER_VARIABLE=something
 
 \ `python-dotenv <https://github.com/theskumar/python-dotenv>`_ to  load up all the entries in this file as environment variables so they are accessible with os.environ.get

 .. code-block:: python
 
    # src/data/dotenv_example.py
    import os
    from dotenv import load_dotenv, find_dotenv
    
    # find .env automagically by walking up directories until it's found
    dotenv_path = find_dotenv()
    
    # load up the entries as environment variables
    load_dotenv(dotenv_path)
    
    database_url = os.environ.get("DATABASE_URL")
    other_variable = os.environ.get("OTHER_VARIABLE")
   
   
  
  

