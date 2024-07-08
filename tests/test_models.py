"""Tests for statistics functions within the Model layer."""

import pandas as pd
import pytest

def test_max_mag_integers():
    # Test that max_mag function works for integers
    from lcanalyzer.models import max_mag

    test_input_df = pd.DataFrame(data=[[1, 5, 3], 
                                       [7, 8, 9], 
                                       [3, 4, 1]], columns=list("abc"))
    test_input_colname = "a"
    test_output = 7

    assert max_mag(test_input_df, test_input_colname) == test_output

def test_max_mag_zeros():
    # Test that max_mag function works for zeros
    from lcanalyzer.models import max_mag

    test_input_df = pd.DataFrame(data=[[0, 0, 0], 
                                       [0, 0, 0], 
                                       [0, 0, 0]], columns=list("abc"))
    test_input_colname = "b"
    test_output = 0

    assert max_mag(test_input_df, test_input_colname) == test_output
    
def test_min_mag_integers():
    # Test that the min_mag function works for integers
    from lcanalyzer.models import min_mag
    
    test_input_df = pd.DataFrame(data=[[1,5,3],
                                       [7,8,9],
                                       [3,4,1]], columns=list("abc"))
    test_input_colname = "b"
    test_output = 4
    
    assert min_mag(test_input_df, test_input_colname) == test_output
    
def test_mean_mag_integers():
    # Test that the min_mag function works for integers
    from lcanalyzer.models import mean_mag
    
    test_input_df = pd.DataFrame(data=[[1,5,2],
                                       [7,8,9],
                                       [3,4,1]], columns=list("abc"))
    test_input_colname = "c"
    test_output = 4
    
    assert mean_mag(test_input_df, test_input_colname) == test_output
    
def test_calc_stat():
    # Test that calc stat works
    from lcanalyzer.models import calc_stat
    
    test_input_dict = {'u':pd.DataFrame(data=[[1,5,2],
                                       [7,8,9],
                                       [3,4,1]], columns=list("abc")),
                       'g':pd.DataFrame(data=[[1,5,8],
                                       [8,8,9],
                                       [3,4,1]], columns=list("abc"))}
    test_input_bands = "ug"
    test_input_magcol = "a"
    test_output = {'u_max':7,'g_max':8}
    
    assert calc_stat(test_input_dict, test_input_bands, test_input_magcol)==test_output
    
def test_max_mag_strings():
    # Test for TypeError when passing a string
    from lcanalyzer.models import max_mag

    test_input_colname = "b"
    with pytest.raises(TypeError):
        error_expected = max_mag('string', test_input_colname)