# Monopoly

Monopoly game simulator.

## Description

The aim of this project is to test four player strategies in a series of games with a maximum number of turns.

The player strategies are:

* **Impulsive**: buys any property that is available;
* **Demanding**: buys properties that have a rent higher than 50;
* **Careful**: buys a property when the resulting balance is at least 80 after purchase;
* **Random**: buys a property with 50% chance.

## Prerequisites

* `Python 3.7`

## Run
In a terminal at the root folder run:

```
pip install -r requirements.txt
```

After the requirements are installed, run:

```
python program.py <number_of_simulations> <max_number_of_turns>
```

The parameters are optional and must be integers with:

* _number_of_simulations_ > 0 
* _max_number_of_turns_ >= 4  

The results will be printed in the terminal.