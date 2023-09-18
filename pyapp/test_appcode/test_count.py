from appcode import count

def test_count():
	assert count.count([0,1,2],0)== 1
	
def test_count_dup():
	assert count.count([1,1,1],1)== 3

def test_count_lotslNum():
	assert count.count([1,2,3,4,5,1,2,3,3,1,1], 1)==4

def test_count_minus():
	assert count.count([-1,-2,-3], -1)==1

def test_count_string():
	assert count.count(["cat","dog","pig"],"dog")==1

def test_count_string_dup():
	assert count.count(["cat","pig","pig"],"pig")==2



