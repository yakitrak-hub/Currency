"""
Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange.

Kartikay Jain kj295
09/17/2017
"""
def before_space(s):
    """Returns: Substring of s; up to, but not including, the first space

    Parameter s: the string to slice
    Precondition: s has at least one space in it"""
    x=s.find(" ")
    return s[:x]


def after_space(s):
    """Returns: Substring of s after the first space

    Parameter s: the string to slice
    Precondition: s has at least one space in it"""
    x=s.find(" ")
    return s[x+1:]


def first_inside_quotes(s):
    """
    Returns: The first substring of s between two (double) quote characters
    A quote character is one that is inside a string, not one that delimits it.
    We typically use single quotes (') to delimit a string if want to us a double
    quote character (") inside of it.
    
    Example: If s is 'A "B C" D', this function returns 'B C'
    Example: If s is 'A "B C" D "E F" G', this function still returns 'B C'
    because it only picks the first such substring.
    
    Parameter s: a string to search
    Precondition: s a string with at least two (double) quote characters.
    """
    
    start=s.index('"')
    tail=s[start+1:]
    end=tail.index('"')
    return tail[:end]


def get_lhs(json):
    """
    Returns: The the LHS value in the response to a currency query.

    Given a JSON response to a currency query, this returns the string inside
    double quotes (") immediately following the keyword "lhs". For example,
    if the JSON is
    '{"success":true, "lhs":"2 United States Dollars", "rhs":"1.825936 Euros", "error":""}'
    then this function returns '2 United States Dollars' (not '"2 United States Dollars"').
    It returns the empty string if the JSON is the result of on invalid query.
    
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    x=json.index("h")
    y=json.index(":",x)
    s=json[y:]
    result=first_inside_quotes(s)
    return result


def get_rhs(json):
    """
    Returns: The RHS value in the response to a currency query.
    
    Given a JSON response to a currency query, this returns the string
    inside double quotes (") immediately following the keyword "rhs".
    For example, if the JSON is
    '{"success":true, "lhs":"2 United States Dollars", "rhs":"1.825936 Euros", "error":""}'
    then this function returns '1.825936 Euros' (not '"1.825936 Euros"').
    It returns the empty string if the JSON is the result of on invalid query.
    
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    x=json.index(",")
    y=json.index(",",x+1)
    z=json.index(':',y)
    s=json[z:]
    result=first_inside_quotes(s)
    return result


def has_error(json):
    """
    Returns: True if the query has an error; False otherwise.
    
    Given a JSON response to a currency query, this returns the opposite of the
    value following the keyword "success". For example, if the JSON is
    '{"success":false, "lhs":"", "rhs":"", "error":"Source currency code is invalid."}'
    then the query is not valid, so this function returns True
    (It does NOT return the message 'Source currency code is invalid').
    
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """
    result="false" in json 
    return result 


def currency_response(currency_from, currency_to, amount_from):
    """
    Returns: a JSON string that is a response to a currency query.
    
    A currency query converts amount_from money in currency currency_from 
    to the currency currency_to. The response should be a string of the form
    
    '{"success":true, "lhs":"<old-amt>", "rhs":"<new-amt>", "error":""}'
    
    where the values old-amount and new-amount contain the value and name for the 
    original and new currencies. If the query is invalid, both old-amount and 
    new-amount will be empty, while "success" will be followed by the value false.
    
    Parameter currency_from: the currency on hand (the LHS)
    Precondition: currency_from is a string
    
    Parameter currency_to: the currency to convert to (the RHS)
    Precondition: currency_to is a string
    
    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float
    """
    import cornell
    return cornell.urlread('http://cs1110.cs.cornell.edu/2017fa/a1server.php?src='
    +currency_from+'&dst='+currency_to+'&amt='+str(amount_from))


def iscurrency(currency):
    """
    Returns: True if currency is a valid (3 letter code for a) currency. 
    It returns False otherwise.
    
    Parameter currency: the currency code to verify
    Precondition: currency is a string.
    """
    x=currency_response(currency, currency, 2.5)
    y=not has_error(x)
    return y


def exchange(currency_from, currency_to, amount_from):
    """
    Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in currency 
    currency_from to the currency currency_to. The value returned represents the 
    amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand (the LHS)
    Precondition: currency_from is a string for a valid currency code
    
    Parameter currency_to: the currency to convert to (the RHS)
    Precondition: currency_to is a string for a valid currency code
    
    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float
    """
    s=currency_response(currency_from, currency_to, amount_from)
    x=get_rhs(s)
    y=before_space(x)
    return float(y)



