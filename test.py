import argparse

# create an argument parser
parser = argparse.ArgumentParser()
parser.add_argument('--foo', type=int)
parser.add_argument('--bar', type=str)
parser.add_argument('--baz', type=bool)

# parse some arguments
args = parser.parse_args()

# create a dictionary with some new values for only some arguments
new_args = {'foo': 42, 'baz': True}

args_dict = vars(args)
args_dict.update(new_args)

# update the args object with the new values
args = argparse.Namespace(**args_dict)

# print the new values of the 'foo', 'bar', and 'baz' arguments
print(args.foo)
print(args.bar)
print(args.baz)