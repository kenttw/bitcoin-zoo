.. _tutorial.rst


*************************
Brief Sphinx Walk through
*************************

How to add .rst file
====================

Our directory look like this:

.. code-block:: none

   +-- tests/
   +-- bitcoin-zoo/
   +-- docs/
       +-- _static/
       +-- _templates/
       +-- _themes/
       +-- conf.py
       +-- index.rst
       +-- README.rst
       +-- tutorial.rst
   ++  simplelib
       +-- useful_1.py

Highlight Code
==============

Use:

.. code-block:: none

   .. code-block:: python
      def hello_world:
          print("Hell World!!")

will generate:

.. code-block:: python

   def hello_world:
       print("Hell World!!")


Include File
============

Pus the file ``tox.ini`` in ``_static/``:

.. code-block:: none

   .. literalinclude:: _static/tox.ini
      :language: ini


will be:

.. literalinclude:: _static/tox.ini
   :language: ini

Lists
=====

Use::

   * A thing.
   * Another thing.

   or

   1. Item 1.
   2. Item 2.
   3. Item 3.

   or

   - Some.
   - Thing.
   - Different.


wil be:

* A thing.
* Another thing.

or

1. Item 1.
2. Item 2.
3. Item 3.

or

- Some.
- Thing.
- Different.

Tables
======


Use::

   
   +------------+------------+-----------+
   | Header 1   | Header 2   | Header 3  |
   +============+============+===========+
   | body row 1 | column 2   | column 3  |
   +------------+------------+-----------+
   | body row 2 | Cells may span columns.|
   +------------+------------+-----------+
   | body row 3 | Cells may  | - Cells   |
   +------------+ span rows. | - contain |
   | body row 4 |            | - blocks. |
   +------------+------------+-----------+

   SIMPLE TABLE:

   =====  =====  ======
   Inputs     Output
   ------------  ------
     A      B    A or B
   =====  =====  ======
   False  False  False
   True   False  True
   False  True   True
   True   True   True
   =====  =====  ======


Will be:

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+

SIMPLE TABLE:

=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ======


Notes
=====

Use ::

   .. note::
      Hello World


   .. warning::
      dont do this


will generate:

.. note::
   Hello World


.. warning::
   dont do this


Autodoc
=======

We can autodoc the ``simplelib`` module::

   .. automodule:: simplelib.useful_1
      :members:


Will generate:

.. automodule:: simplelib.useful_1
   :members:










