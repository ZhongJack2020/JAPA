# JAPA

**J**ack's  
**A**rtificial immune system  
**P**ython  
**A**lgorithm

JAPA is an implementation of the clonal selection algorithm CLONALG described in [*Learning and Optimization Using the Clonal Selection Principle (2001)*](http://www.dca.fee.unicamp.br/~vonzuben/research/lnunes_dout/artigos/ieee_tec01.pdf).

## Requirements
- Python 3.10
- Matplotlib

## Installation

1. Install Python 3.10
2. Install Matplotlib using `pip install matplotlib`

## Usage
JAPA is written as a library, so you could instead `import japa` and then run `japa.japa()`, specifying the antibodies, antigens and your preferred parameters for the algorithm.

JAPA comes with `h1_evaluation.py` and `h2_evaluation.py`. They run JAPA with different parameters and save the results to a CSV file for analysis. 

To run demo `h1_evaluation.py`, use following command in the terminal:

`python ./h1_evaluation.py`

after run the demo, `output.csv` and `graph.png` will be generated. They show the result.

*In this demo, I modify the computational formula of affenity to make it easy to understand, which equal 1 means full affenity*

