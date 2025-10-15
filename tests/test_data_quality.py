import pandas as pd
import os

def run_tests(data_dir='data'):
    base = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base, data_dir)
    trans = pd.read_csv(os.path.join(data_path,'transactions.csv'))
    # no negative revenue
    assert (trans['revenue'] >= 0).all(), 'Negative revenue found'
    # quantities positive ints
    assert (trans['quantity'] > 0).all(), 'Non-positive quantity found'
    # unique transaction ids
    assert trans['transaction_id'].nunique() == len(trans), 'Duplicate transaction_id found'
    print('All tests passed.')

if __name__ == '__main__':
    run_tests()
