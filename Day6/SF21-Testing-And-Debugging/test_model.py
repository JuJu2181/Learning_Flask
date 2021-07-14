import pytest
from model import FruitDB, FruitSalad


def test_apple():
    db = FruitDB()
    db.connect('data.json')
    apple_data = db.get_data('Apple')
    assert apple_data['id'] == 1
    assert apple_data['name'] == 'Apple'

def test_banana():
    db = FruitDB()
    db.connect('data.json')
    apple_data = db.get_data('Banana')
    assert apple_data['id'] == 2
    assert apple_data['name'] == 'Banana'

####------------------------------------------------------------###

"""
    1. Arrange : Preparation
    2. Act : Methods Call
    3. Assert : Checking Results
    4. Cleanup : Wrap up test
"""

####------------------------------------------------------------###
###--------------SETUP AND TEARDOWN-----------------------------###
###-------------------------------------------------------------###

####-----------------------------------------------------------####

# db = None
# def setup_module(module):
#     print('-----------setup---------')
#     global db
#     db = FruitDB()
#     db.connect('data.json')

# def teardown_module(module):
#     print('------------teardown-------')
#     db.close()

# def test_apple():
#     apple_data = db.get_data('Apple')
#     assert apple_data['id'] == 1
#     assert apple_data['name'] == 'Apple'

# def test_banana():
#     apple_data = db.get_data('Banana')
#     assert apple_data['id'] == 2
#     assert apple_data['name'] == 'Banana'

####-----------------------------------------------------------####

####------------------------------------------------------------###
###-----------------PYTEST FIXTURES-----------------------------###
###-------------------------------------------------------------###

####---------------------INTRO---------------------------------####

# @pytest.fixture
# def db():
#     db = FruitDB()
#     db.connect('data.json')
#     return db

# @pytest.fixture
# def locus_salad():
#     locus_salad = FruitSalad()
#     return locus_salad

# def test_salad_contain(db, locus_salad):
#     apple = db.get_data('Apple')
#     locus_salad.add(apple)
    
#     banana = db.get_data('Banana')
#     assert locus_salad.contain(apple)
#     assert not locus_salad.contain(banana)

# def test_salad_remove(db, locus_salad):
#     apple = db.get_data('Apple')
#     locus_salad.add(apple)
    
#     banana = db.get_data('Banana')
#     locus_salad.add(banana)
#     assert locus_salad.contain(apple)

#     locus_salad.remove(banana)
#     assert not locus_salad.contain(banana)
#     with pytest.raises(NameError):
#         locus_salad.remove(banana)

####-----------------------------------------------------------####

####----------FIXTURES REQUESTING ANOTHER FIXTURES-------------####

####-----------------------------------------------------------####

# @pytest.fixture
# def db():
#     # print('-----------setup---------')
#     db = FruitDB()
#     db.connect('data.json')
#     return db
#     # yield db
#     # print('-------------------teardown--------------')
#     # db.close

# @pytest.fixture
# def apple(db):
#     apple = db.get_data('Apple')
#     return apple

# @pytest.fixture
# def banana(db):
#     banana = db.get_data('Banana')
#     return banana

# @pytest.fixture
# def locus_salad(apple):
#     locus_salad = FruitSalad()
#     locus_salad.add(apple)
#     return locus_salad

# def test_salad_contain(apple, banana, locus_salad):   
#     assert locus_salad.contain(apple)
#     assert not locus_salad.contain(banana)

# def test_salad_remove(apple, banana, locus_salad):
#     locus_salad.add(banana)
#     assert locus_salad.contain(banana)
#     locus_salad.remove(banana)
#     assert not locus_salad.contain(banana)
#     with pytest.raises(NameError):
#         locus_salad.remove(banana)

####--------------------------SCOPE----------------------------####
"""

    function: the default scope, the fixture is destroyed at the end of the test.
    class: the fixture is destroyed during teardown of the last test in the class.
    module: the fixture is destroyed during teardown of the last test in the module.
    package: the fixture is destroyed during teardown of the last test in the package.
    session: the fixture is destroyed at the end of the test session.

"""