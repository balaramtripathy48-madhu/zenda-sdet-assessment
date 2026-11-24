import logging
from pytest_bdd import scenarios

logger = logging.getLogger(__name__)

scenarios("../features/add_to_cart.feature")
