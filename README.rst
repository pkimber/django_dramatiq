KB Software - fork of django_dramatiq
*************************************

.. highlight:: python

https://github.com/pkimber/django_dramatiq
is a fork of ``Bogdanp``:
https://github.com/Bogdanp/django_dramatiq

The issue is:
https://github.com/Bogdanp/django_dramatiq/issues/109

I solved the issue by adding to the ``_resolve_executable`` method in 
``django_dramatiq/django_dramatiq/management/commands/rundramatiq.py``::

  # fall back to default behaviour (from earlier versions)
  return os.path.join(bin_dir, exec_name)

Here is the whole method::

  def _resolve_executable(self, exec_name):
      bin_dir = os.path.dirname(sys.executable)
      if bin_dir:
          for d in [bin_dir, os.path.join(bin_dir, "Scripts")]:
              exec_path = os.path.join(d, exec_name)
              if os.path.isfile(exec_path):
                  return exec_path
          # fall back to default behaviour (from earlier versions)
          # ref https://github.com/Bogdanp/django_dramatiq/issues/109
          return os.path.join(bin_dir, exec_name)
      return exec_name

.. code-block:: bash

  python3 -m venv venv-django-dramatiq
  source venv-django-dramatiq/bin/activate.fish
  pip install -r requirements/local.txt
