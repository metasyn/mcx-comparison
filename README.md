# MCX Setting Comparison

## Purpose

Managed Client for OS X (MCX) is a tool we use for managing our Mac system preferences as well as other settings.
Sometimes these get corrupted, and this is a tool for indentifying which settings are not matched to other comptuers.

## Usage

1. Use Apple Remote Desktop to get a list of mcxsettings via the command "mcxquery -computerOnly"
2. Export the results as a text file
3. Call the compare_mcx_printing.py file with the text file as the first argument

## Example

You can use the two text files in the test folder to see what a clean result & result with errors looks like. 
There is a file called comparison_results.txt which will show you what the outputs of the command will look like.