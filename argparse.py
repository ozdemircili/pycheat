import argparse
parser.add_argument("echo")     # naming it "echo"
args = parser.parse_args()  # returns data from the options specified (echo)
print(args.echo) 
