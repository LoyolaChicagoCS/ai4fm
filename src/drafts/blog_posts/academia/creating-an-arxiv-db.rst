###############################################
``arXiv DB``: A Vector Database Of arXiv papers
###############################################

`arXiv <https://arxiv.org>`_ is the largest academic pre-print server containing articles from most natural science, mathematics, and computer sciences.
It (and services similar to it) provide a treasure trove of information and early results to researchers, engineers, and the public at the cost of limited peer-review.
Since **XYZ** year, arXiv has rapidly become the go-to destination for publishing techincal reports, methods, and other findings regarding machine and deep learning research; often foregoing a submission to an established conference series or journal.
This has resulted in an average of **XYZ** manuscripts per day being published on arXiv; enough to overwhelm most researchers with the amount of reading they would have to do to keep up with the field.

.. TODO: Add a figure that compares the number of arXiv publications tagged Machine and Deep Learning 3 years prior and up till present as a line chart

As a Ph.D. student, I have found it increasingly difficult to keep up with the latest on-goings in my research field.



.. OLD PROSE
As a Ph.D. student studying Deep Learning (DL) from the perspective of a
Software Engineer, I rely upon academic resources to learn about DL
models, techniques, and methods. `arXiv <https://arxiv.org>`__ is
arguably the largest host of the latest academic (but not peer-reviewed)
DL manuscripts.

However, as it relies upon community donations to support the service,
there are limitations to the service. One of them is that only the last
week of manuscripts are browsable at any given time with the rest being
searchable.

As someone who checks the service often for the latest information, it
can become irritating when I'm casually browsing the site, find an
interesting manuscript, and (for one reason or another) forget to
bookmark it and then not find the paper as I can't nail down the exact
keywords to search for it. Additionally, I'd like to leverage the data
on the site for other projects like testing retrieval augmented
generation (RAG) techniques for finding information from manuscripts.

To support users like me, the arXiv team releases the metadata of all
papers submitted to the platform weekly on `Kaggle
<https://www.kaggle.com/datasets/Cornell-University/arxiv>`__ as JSON.
So for today's blog post, let's convert the JSON file into a queriable
SQLite3 database!

###############
 Project Setup
###############

I'll leverage Python 3.10 and bash for this project primarily for the
```pandas`` library <https://pypi.org/project/pandas/>`__. ``pandas``
provides convenient ``read_json`` and ``to_sql`` methods for reading
JSON files and writing to SQL databases respectfully.

To start, I created a GitHub repository based on `my Python template
repo <https://github.com/NicholasSynovic/template_python>`__. You can
find all the project code `here
<https://github.com/NicholasSynovic/tool_arXiv-db>`__.

###############################
 Getting And Cleaning The Data
###############################

As the arXiv Dataset is hosted on Kaggle, we can use their ```kaggle``
<https://pypi.org/project/kaggle/>`__ Python library to download and
unzip the data. Wrapping this as a bash script, we get:

.. code:: bash

   #!/bin/bash

   kaggle datasets download --unzip Cornell-University/arxiv -p $1

Where the ``--unzip`` argument decompresses the data, and the ``-p``
argument specifies a path to download the data. We can improve this
further by leveraging ```optparse``
<https://github.com/nk412/optparse>`__ to provide command-line arguments
for our script. All said and done, we have a download script that looks
like this:

.. code:: bash

   #!/bin/bash

   source optparse.bash
   optparse.define short=p long=path desc="Directory to store dataset" variable=PATH default="."
   source $( optparse.build )

   ABS_PATH=$(realpath $PATH)

   kaggle datasets download --unzip Cornell-University/arxiv -p $ABS_PATH

Now that we have the data in JSON format, we can further optimize it by
converting it into `JSON Lines <https://jsonlines.org/>`__ (JL) format.
JL is a format for storing JSON data where each line is a single object.
This effectively removes top-level arrays of objects which is how the
arXiv Dataset is stored. By converting the data into a JL format, Pandas
can read the file in chunks, thereby reducing the memory overhead by
loading only portions of data into memory.

We can leverage ```jq`` <https://github.com/jqlang/jq>`__ to do the
conversion with this script:

.. code:: bash

   #!/bin/bash

   source optparse.bash

   optparse.define short=i long=input desc="Input JSON file" variable=inputPath
   optparse.define short=o long=output desc="Output JSON Lines file" variable=outputPath

   source $( optparse.build )

   if [[ -z $inputPath ]]; then
       echo "No input provided."
       exit 1
   fi

   if [[ -z $outputPath ]]; then
       echo "No output provided."
       exit 1
   fi

   absInputPath=$(realpath $inputPath)
   absOutputPath=$(realpath $outputPath)

   jq -c . $absInputPath > $absOutputPath

With that, our data is finally in a format where we can start loading it
into a database!

#######################
 Creating The Database
#######################

We will define our database schema using `SQLAlchemy
<https://www.sqlalchemy.org/>`__. First, we will store a subset of the
information in a single table called ``documents``. This is to test that
our database configuration is correct and avoid storing nested data now.
The code is fairly simple to create a SQLite3 database with SQLAlchemy:

.. code:: python

   from pathlib import Path

   from sqlalchemy import (
       Column,
       Engine,
       MetaData,
       PrimaryKeyConstraint,
       String,
       Table,
       create_engine,
   )


   class DB:
       def __init__(self, path: Path) -> None:
           self.path: Path = path
           self.engine: Engine = create_engine(url=f"sqlite:///{path}")
           self.metadata: MetaData = MetaData()

           self.documentTable: str = "documents"

           self.createTables()

       def createTables(self) -> None:
           _: Table = Table(
               self.documentTable,
               self.metadata,
               Column("id", String),
               Column("title", String),
               Column("submitter", String),
               Column("comments", String),
               Column("journal-ref", String),
               Column("doi", String),
               Column("report-no", String),
               Column("categories", String),
               Column("license", String),
               Column("abstract", String),
               Column("update_date", DateTime),
               PrimaryKeyConstraint("id"),
           )

           self.metadata.create_all(bind=self.engine, checkfirst=True)

Running this code and checking the database schema we see that the table
and columns have been created successfully:

|image1|

We will extend this later by adding tables and relationships between
nested values and the documents table.

##################################
 Inserting Data Into The Database
##################################

With Pandas, we can read the data in from the JL file as chunks:

.. code:: python

   from pathlib import Path
   from typing import Iterator

   import pandas
   from pandas import DataFrame


   def readJSON(fp: Path, chunksize: int = 10000) -> Iterator[DataFrame]:
       return pandas.read_json(
           path_or_buf=fp,
           lines=True,
           chunksize=chunksize,
           engine="ujson",
       )

This ``Iterator[DataFrame]`` object lazily reads the file into memory
which we can do with a ``for`` loop.

.. code:: python

   def loadData(dfs: Iterator[DataFrame], db: DB) -> None:
       df: DataFrame
       for df in dfs:
           print(df.columns)
           quit()

As our current database schema doesn't take all of the fields captured
in the JSON objects, we need to parse our DataFrame for the columns that
are captured:

.. code:: python

   def getDocuments(df: DataFrame) -> DataFrame:
       documentsDF: DataFrame = df[
           [
               "id",
               "title",
               "submitter",
               "comments",
               "journal-ref",
               "doi",
               "report-no",
               "categories",
               "license",
               "abstract",
               "update_date",
           ]
       ].copy()

       documentsDF["update_date"] = pandas.to_datetime(
           arg=documentsDF["update_date"],
       )

       return documentsDF

Then we can load the document data into the database:

.. code:: python

   def loadData(dfs: Iterator[DataFrame], db: DB) -> None:
       df: DataFrame
       for df in dfs:
           documentsDF: DataFrame = getDocuments(df=df)
           documentsDF.to_sql(
               name=db.documentTable,
               con=db.engine,
               if_exists="append",
               index=False,
           )
           quit()

Checking our testing database, we can see that the first set of
documents was loaded correctly:

|image2|

However, when we try to import the entire dataset into the database, we
get a ``sqlalchemy.exc.IntegrityError`` because some of the primary keys
are duplicated in the JL file. Rather than handling this when converting
the data, we can extend our ``DB`` class to support reading DataFrames
into a table while checking for duplicates should an error arise:

.. code:: python

   ...

   from pandas import DataFrame
   import pandas
   from sqlalchemy.exc import IntegrityError

   from typing import List


   class DB:
       ...

       def toSQL(self, tableName: str, df: DataFrame) -> int:
           try:
               df.to_sql(
                   name=tableName,
                   con=self.engine,
                   if_exists="append",
                   index=False,
               )

           except IntegrityError as error:
               ids: List[str] = [param[0] for param in error.params]
               df = df[~df["id"].isin(values=ids)]

               df.to_sql(
                   name=tableName,
                   con=self.engine,
                   if_exists="append",
                   index=False,
               )

           return df.shape[0]

If an error occurs, a unique DataFrame is created from the list of
primary keys not reported by the ``IntegrityError``, another attempt is
made to reinsert them into the database. Additionally, we now return the
number of rows committed to the database.

So our updated ``loadData`` method now looks like this (with a Spinner
object to help report progress from the ```progress``
<https://pypi.org/project/progress/>`__ library):

.. code:: python

   def loadData(dfs: Iterator[DataFrame], db: DB) -> None:
       with Spinner(f"Loading data into {db.path}... ") as spinner:
           df: DataFrame
           for df in dfs:
               documentsDF: DataFrame = getDocuments(df=df)
               db.toSQL(tableName=db.documentTable, df=documentsDF)
               spinner.next()

#############
 Wrapping Up
#############

Now that the basic structure of the application has been created, all
that's left is to add the other tables.

For example, we can create a table called ``authors`` to store each
author of a document:

.. code:: python

   _: Table = Table(
       self.authorTable,
       self.metadata,
       Column("id", Integer),
       Column("document_id", String),
       Column("author", String),
       PrimaryKeyConstraint("id"),
       ForeignKeyConstraint(
           columns=["document_id"],
           refcolumns=["documents.id"],
       ),
   )

And then access only the authors from the DataFrame with this method:

.. code:: python

   def getAuthors(df: DataFrame, idIncrement: int = 0) -> DataFrame:
       authorsDF: DataFrame = df[["id", "authors_parsed"]]
       authorsDF = authorsDF.explode(column="authors_parsed", ignore_index=True)
       authorsDF["author"] = authorsDF["authors_parsed"].apply(
           lambda x: ", ".join(x),
       )

       authorsDF = authorsDF.drop(columns="authors_parsed")
       authorsDF.index += idIncrement
       authorsDF = authorsDF.reset_index()
       authorsDF = authorsDF.rename(columns={"id": "document_id", "index": "id"})

       return authorsDF

Then we can use the ``DB.toSQL()`` method to write it to the database.

The final database schema is as follows (generated with `SchemaCrawler
<https://www.schemacrawler.com/>`__):

.. figure:: https://dev-to-uploads.s3.amazonaws.com/uploads/articles/elvuus7uhhg49tsov9hh.png
   :alt: Image description

   Image description

As seen here, there is additional complexity in storing this data. The
versions table undergoes similar transformations as well.

If you are interested in how the ``versions`` table is created and to
leverage this tool, please visit the `GitHub project page
<https://github.com/NicholasSynovic/tool_arXiv-db>`__.

Thanks for taking the time to read this post. I hope to be posting more
in the future.

.. |image1| image:: https://dev-to-uploads.s3.amazonaws.com/uploads/articles/f6ofhguzzn00nf2ei1lq.png

.. |image2| image:: https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5biwn7c5jxkklplrjrof.png
