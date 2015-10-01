# Markov chain random sentence generator.

An implementation of a `kth` Markov chain that generates a random sentence based on training data.

# Usage

* Clone the repository. 
```
git clone https://github.com/adijo/markov-random-sentence-generator.git
```
* Enter the directory.
```
cd markov-random-sentence-generator
```

* The package comes with a sample training corpus called `jokes.txt`. 

* To run the code, simply type the following in the terminal. Here, `filename` is the location of the input 
training corpus. `order` is the order of the Markov model and `limit` denotes the length of the sentence to be 
generated.

```python
python main.py -filename jokes.txt -order 1 -limit 20

$ "sure. ten miles to a thousand others break up. ""number 53!" says "i just trampling and four!".
```


