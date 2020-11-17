"""
Unit test for module a1

When run as a script, this module invokes several procedures that 
test the various functions in the module a1.

Kartikay Jain kj295
09/17/2017
"""
import cornell
import a1
def testA():
     """Test procedure for Part A"""
     cornell.assert_equals("Hello",a1.before_space("Hello World"))
     cornell.assert_equals("Hello",a1.before_space("Hello World World"))
     cornell.assert_equals("Hello",a1.before_space("Hello  "))
     cornell.assert_equals("",a1.before_space(" "))
     cornell.assert_equals("",a1.before_space(" df"))
     cornell.assert_equals("World",a1.after_space("Hello World"))
     cornell.assert_equals("World World",a1.after_space("Hello World World"))
     cornell.assert_equals(" ",a1.after_space("Hello  "))
     cornell.assert_equals("",a1.after_space(" "))
     cornell.assert_equals("df",a1.after_space(" df"))


def testB():
     """Test procedure for Part B"""
     cornell.assert_equals("B C",a1.first_inside_quotes('A "B C" D'))
     cornell.assert_equals("B C",a1.first_inside_quotes('A "B C" D "E F" G'))
     cornell.assert_equals("B",a1.first_inside_quotes('"B"'))
     cornell.assert_equals("",a1.first_inside_quotes('A "" D'))
     cornell.assert_equals('2 United States Dollars',a1.get_lhs(
     '{"success":true, "lhs":"2 United States Dollars", "rhs":"1.67619 Euros", \
     "error":""}'))
     cornell.assert_equals('',a1.get_lhs(
     '{"success":false, "lhs":"", "rhs":"", "error":"Source currency code is inv\
     alid."}'))
     cornell.assert_equals('1.67619 Euros',a1.get_rhs(
     '{"success":true, "lhs":"2 United States Dollars", "rhs":"1.67619 Euros", \
     "error":""}'))
     cornell.assert_equals('',a1.get_rhs(
     '{"success":false, "lhs":"", "rhs":"", "error":"Source currency code is inv\
     alid."}'))
     cornell.assert_equals(True,a1.has_error(
     '{"success":false, "lhs":"", "rhs":"", "error":"Source currency code is inv\
     alid."}'))
     cornell.assert_equals(True,a1.has_error(
     '{"success":false, "lhs":"", "rhs":"", "error":"Exchange currency code is i\
     nvalid."}'))
     cornell.assert_equals(True,a1.has_error(
     '{"success":false, "lhs":"", "rhs":"", "error":"Currency amount is invalid.\
     "}'))
     cornell.assert_equals(False,a1.has_error(
     '{"success":true, "lhs":"2 United States Dollars", "rhs":"1.67619 Euros", \
     "error":""}'))


def testC():
     """Test procedure for Part C"""
     cornell.assert_equals('{ "success" : true, "lhs" : "2.5 United States Dolla\
rs",\
 "rhs" : "2.0952375 Euros", "error" : "" }',\
 a1.currency_response('USD', 'EUR', 2.5))
     cornell.assert_equals('{ "success" : true, "lhs" : "2.5 United Arab \
Emirates \
Dirhams", "rhs" : "0.57046204638433 Euros", "error" : "" }',a1.currency_response\
('AED', 'EUR', 2.5))
     cornell.assert_equals('{ "success" : true, "lhs" : "2.5 United Arab Emirate\
s Dirhams",\
 "rhs" : "75.982649028909 Albanian Leks", "error" : "" }',a1.currency_response\
('AED', 'ALL', 2.5))
     cornell.assert_equals('{ "success" : false, "lhs" : "", "rhs" : "", "error"\
 :\
 "Source currency code is invalid." }',a1.currency_response('AAA', 'EUR', 2.5))
     cornell.assert_equals('{ "success" : false, "lhs" : "", "rhs" : "", "error"\
 :\
 "Exchange currency code is invalid." }',a1.currency_response('USD', 'AAA', 2.5))


def testD():
     """Test procedure for Part D"""
     cornell.assert_equals(True,a1.iscurrency('EUR'))
     cornell.assert_equals(False,a1.iscurrency('AAA'))
     cornell.assert_floats_equal(2.0952375,a1.exchange('USD','EUR',2.5))


testA()


testB()


testC()


testD()
print("Module a1 passed all tests")