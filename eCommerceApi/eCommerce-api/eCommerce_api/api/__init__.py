__author__ = 'eCommerceApi'
__version__ = '1.0'


from .namespaces.user_ns import user_ns
from .namespaces.inventory_ns import inventory_ns
from .namespaces.purchase_ns import purchase_ns

namespaces = [user_ns,inventory_ns,purchase_ns]