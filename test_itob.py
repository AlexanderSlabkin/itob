import pytest
from itob import Explorer
from sqltables import InfoSite, Domen
from domenrequest import parse

@pytest.fixture
def empty_site():
    '''Returns an InfoSite instance with all fields empty'''
    return InfoSite()

@pytest.fixture
def full_site():
    '''Returns an InfoSite instance with all fields filled'''
    return InfoSite(url='https://itob.com', title='ITOB', description='Best company', keywords='dog cat bicycle')


@pytest.fixture
def domen():
    '''Returns a InfoSite instance with all fields filled'''
    return Explorer(last_id=3)

@pytest.fixture
def explorer():
    '''Returns a InfoSite instance with all fields filled'''
    return Explorer(last_id=3)

def test_default_initial(empty_site):
    assert empty_site.url == None

def test_job_done(correct_domen):
    job()
