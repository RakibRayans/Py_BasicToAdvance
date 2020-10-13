'''
import ecommerce.shipping
ecommerce.shipping.calc_shipping()
'''
# another way to import the function
'''
from ecommerce.shipping import calc_shipping  #we can also umport cal_shipping, text_shipping
calc_shipping()            #now we can call it multiple time
calc_shipping()
calc_shipping()
'''

#also we can import full module

from ecommerce import shipping, manufacture

shipping.calc_shipping()
shipping.text_shipping()
manufacture.manufacture_cost()