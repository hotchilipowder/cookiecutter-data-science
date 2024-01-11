=======
Dockers
=======


For the current project, we will always include some docker service for our data crawling, management, query, and visualization. Some parts can be well integrated with Python, some will not. So we may include other well-built services like Postgresql or Mongodb for our project.

.. note::
   
   We suppose our project in on the port ranging from 18100-18110.

   Some admin will block the ports for safety.
   We can use \ :code:`iptables`\ to release some ports:

   .. code-block:: bash
   
      #!/bin/bash

      start_port=18100
      end_port=18120
      for ((port=$start_port; port<=$end_port; port++))
      do
          iptables -A INPUT -p tcp --dport $port -j ACCEPT
          ip
   
   



Docker-compose
==============


Playwright with django
----------------------

.. csv-table:: Docker ports
   :header: "Container", "ports", "Notes"
   :widths: 15, 10, 30
   
   django-web, 18100, 
   postgres, 18111,
   redis, 18112
   

Just use \ :code:`docker-compose up`\


.. dropdown:: Dockerfile

   .. literalinclude:: ../../{{ cookiecutter.repo_name }}/dockers/playwrights_with_postgresql/Dockerfile


.. dropdown:: docker-compose.yml

   .. literalinclude:: ../../{{ cookiecutter.repo_name }}/dockers/playwrights_with_postgresql/docker-compose.yml


