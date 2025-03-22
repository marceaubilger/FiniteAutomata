
import menu_tracer as m
import os
import sys


# Redirect stdout to tamer.txt
sys.stdout = open('Traces\Trace.txt', 'w', encoding='utf-8')

# Redirect stdin to inputs.txt
sys.stdin = open('Traces\inputs.txt', 'r')

# Call the menu function to start the interaction
m.Menu()

# Close the stdout redirection
sys.stdout.close()

# Close the stdin redirection
sys.stdin.close()