import itertools
import random

class MarkovGenerate(object):
    """
    Response for constructing the kth order Markov chain.
    """

    def _form_graph(self, words, order):
        """
        Takes the input words and builds the Markov chain.
        """
        for i in xrange(len(words) - order):
            key = tuple(words[i : i + order])
            if key in self.markov_chain:
                self.markov_chain[key].add(words[i + order])
            else:
                self.markov_chain[key] = set([words[i + order]])
        
        for key in self.markov_chain:
            self.markov_chain[key] = list(self.markov_chain[key])

    def _full_stop(self, sentence):
        """
        Helper function for added a full stop at the en
        of a sentence.
        """
        last_word = sentence.pop()
        if last_word[-1] != ".":
            sentence.append(last_word + ".")
        else:
            sentence.append(last_word)
        return sentence

    def __init__(self, input, order):
        lines = [line.rstrip('\n') for line in open(input)]
        lines = filter(lambda x : len(x) > 0, lines)
        lines = map(lambda x : x.split(), lines)
        words = map(lambda x : x.lower(), list(itertools.chain(*lines)))
        self.markov_chain = {}
        self._form_graph(words, order)
        #randomness = 0.0
        
        # The following lines measure the randomness of the 
        # words generated per key.
        #for key in self.markov_chain:
        #    randomness += len(self.markov_chain[key])
        #print randomness / len(self.markov_chain)
        
        self.order = order    
        #sentence = self.generate(200)
        #sentence = " ".join(self._full_stop(sentence))

        #print sentence.decode('unicode_escape').encode('ascii','ignore')

    def generate(self,  limit = 30):
        """
        Generates a random sentence based on the model 
        built in the constructor.
        """
        seed = random.choice(self.markov_chain.keys())
        sentence = []
        for word in seed:
            sentence.append(word)
        sentence[0] = sentence[0].capitalize()
        count = self.order
        while count < limit:
            next_word = random.choice(self.markov_chain.get(seed))
            sentence.append(next_word)
            next_seed = tuple(sentence[-self.order:])
            if next_seed not in self.markov_chain:
                sentence = self._full_stop(sentence)
                seed = random.choice(self.markov_chain.keys())
                for word in seed:
                    sentence.append(word)
            else:
                seed = next_seed
            count += 1
        sentence = " ".join(self._full_stop(sentence))
        return sentence.decode('unicode_escape').encode('ascii','ignore')

