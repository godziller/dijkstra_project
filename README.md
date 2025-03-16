# Dijkstra Project

## System Requirements

- This project requires python 3.6 or greater to run. Note for printing it uses the f-string feature, which was introduced in the mentioned version.
- If you want to run the test harness, please ensure you have `pytest` installed.
- A pretty beef machine is required, especially for `run_question4.py` and `run_question6.py`

## Setting up the project.

The easiest way to run this project is to `git clone https://github.com/godziller/dijkstra_project.git`

If you choose to install manually, via zip download, please ensure the directory/file structure is as described below.

## Project Structure

```
The file and directory structure is as follows:
├── dijkstra_algos                  # My Dijksta Algorithm
│   └── dijkstra.py
├── graph                           # Graph Implemenation
│   ├── graph_dijkstra.py
│   ├── graph.py
│   └── __init__.py
├── pq                              # Various Priority queue implementations
│   ├── apq_binary_heap.py
│   ├── apq_unsorted_list.py
│   ├── __init__.py
│   ├── priority_queue_binary_heap.py
│   └── priority_queue_unsorted.py
├── report                          # Project report. Archived evaluation runs for convienence
│   ├── Binary_Heap_Vs_Unsorted_List.png
│   ├── evaluation_q1.txt
│   ├── evaluation_q2.txt
│   ├── evaluation_q3.txt
│   ├── evaluation_q4.txt
│   ├── evaluation_q5.txt
│   ├── evaluation_q6.txt
│   ├── question4.png
│   ├── question6.png
│   ├── REPORT.md                   # Project report
│   └── REPORT.pdf                  # PDF of project report
└── tests                           # Test Folder
    ├── __init__.py
    ├── test_apq_binary_heap.py
    ├── test_apq_unsorted_list.py
    ├── test_graph.py
    └── test_priority_queue.py
├── README.md                       # This readme
├── run_question1.py                # All the evaluation runs
├── run_question2.py
├── run_question3.py
├── run_question4.py
├── run_question5.py
└── run_question6.py
```

## Running the Evaluations

To make it easier, I tried to follow the same pattern for running each evaluation from Part 1 -> 6. 

Simply execute `python3 run_question[VER].py` where VER is 1 to 6, matching assignment question 1 to 6.

Each outputs to terminal. But you can redirect to a file, name of your choosing using the standard linux `>` mechanism.

Inside `report/` you will find a set of file, `evaluation_q[VER].txt` where VER is as described immediately above.

## The Evaluation

The Project evaluation can be found in `report/` in both markdown format `REPORT.md` and pdf `REPORT.pdf` 

