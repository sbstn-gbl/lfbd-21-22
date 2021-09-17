# GitHub Repository for Course "Learning from Big Data"

## Content

```
.
├── Makefile                  # run `make help` to see make targets
├── README.md                 # this readme file
├── requirements.txt          # virtualenv requirements file
├── lectures                  # lecture notebooks
├── preparation               # course preparation notebooks
└── source                    # sources, e.g., images for notebooks
```

Please consider the following instructions and the material in this repository carefully. The repository content is designed to make participation in Learning from Big Data as easy and enjoyable for you as possible.

## Requirements

1. Python 3.8
1. `virtualenv`

Optional:
1. `graphviz` (install with `brew install graphviz`)

Please familiarize yourselves with `virtualenv` (or a similar tool such as `conda`). Some background information can be found in the [virtualenv docs](https://virtualenv.pypa.io/en/latest/) or [here](https://stackoverflow.com/questions/34398676/does-conda-replace-the-need-for-virtualenv).

In the lectures, we will use Jupyter notebooks to illustrate implementation-related key points. The notebooks will be published in this repository well ahead of the lecture. Please make sure that you can execute the notebooks before joining the class so you can easily follow the coding parts in the lectures.

For the homework assignments, use an [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment) of your choice. IDE choice really depends on personal preferences. A very popular choice is PyCharm (JetBrains offers a [free pro license for students](https://www.jetbrains.com/community/education/#students)). If you are familiar with coding this should be easy to manage. Other people like [Spyder](https://www.spyder-ide.org), [JupyterLab](https://jupyter.org) or [Google Colab](https://colab.research.google.com/notebooks/intro.ipynb?utm_source=scs-index). Do some research to figure out which IDE suits your background and preferences best.

## Setup

### Makefile targets

The [Makefile](./Makefile) included in this repository is purely for convenience (setting up the virtual environment, . It should work on systems running Linux and Mac OS X.

```
$ make help
Make targets:
  build          create virtualenv and install packages
  build-lab      `build` + lab extensions
  freeze         persist installed packaged to requirements.txt
  clean          remove *.pyc files and __pycache__ directory
  distclean      remove virtual environment
  run            run jupyter lab
Check the Makefile for more details
```

### Step-by-step instructions

1. Open a terminal and navigate to the path that you want to clone the repository to
1. Clone the repository
    ```
    $ git clone git@github.com:sbstn-gbl/learning-from-big-data.git
    ```
1. Navigate to repository path, create virtual environment and install required modules with
    ```
    $ cd learning-from-big-data && make build
    ```
    or `make build-lab` to include `jupyterlab` dependencies.
1. Start a notebook server with
    ```
    $ make run
    ```

## Course preparation

Please solve the following three pre-course assignments before the first lecture.

- [Notebook 1: Data Tasks](preparation/notebook-1-data.ipynb)
- [Notebook 2: ML Metrics](preparation/notebook-2-metrics.ipynb)
- [Notebook 3: Gradient Descent](preparation/notebook-3-gradient.ipynb)

Use textbooks or online resources to fill gaps in your skills. The pre-course assignments will prepare you for the materials covered in Learning from Big Data and help you assess whether you are ready for this course. The pre-course assignments are challenging, if you find them ___too___ challenging, you should consider enrolling in this course in the following year. If you are not sure, feel free to contact one of the teachers before starting this course.

Please also study the material covered in the following online courses:

- [Introduction To Python Programming](https://www.udemy.com/course/pythonforbeginnersintro/)
- [Master Data Analysis with Python - Intro to Pandas](https://www.udemy.com/course/master-data-analysis-with-python-intro-to-pandas/)

## Lecture Notebooks

### Module 2
- [Lecture 05-1: Logistic Regression (Motivation)](lectures/l05-1-binary-classification-motivation.ipynb)
- [Lecture 05-2: Missing Data](lectures/l05-2-missing-data.ipynb)
- [Lecture 05-3: Logistic Regression w/ MBGD](lectures/l05-3-binary-classification-mbgd.ipynb)

More notebooks coming soon.

### Module 3

Coming soon.
