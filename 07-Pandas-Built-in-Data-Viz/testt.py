import pandas as pd
import matplotlib.pyplot as plt

# Create a dataframe using three lists
df = pd.DataFrame(
	{'List1': [ 1 , 2 , 3 , 4 , 5 , 6 ],
	'List2': [ 5 , 10 , 15 , 20 , 25 , 30 ],
	'List3': [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' ]})

# print(df)
#    List1  List2 List3
# 0      1      5     a
# 1      2     10     b
# 2      3     15     c
# 3      4     20     d
# 4      5     25     e
# 5      6     30     f


# use plot() method on the dataframe.
# List3 is in the x-axis and List2 in the y-axis
df.plot( 'List3' , 'List2' )

plt.show()