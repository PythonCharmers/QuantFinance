
def prior_postcode_given_state(postcode, state):
    postcodes = postcodes_by_state[state]
    return 1 / len(postcodes) if postcode in postcodes else 0

prior_postcode_given_state(3122, 'Victoria')

prior_postcode(3122)
