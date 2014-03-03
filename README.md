# MCX Setting Comparison

## Purpose

Managed Client for OS X (MCX) is a tool we use for managing our Mac system preferences as well as other settings.
Sometimes these get corrupted, and this is a tool for indentifying which settings are not matched to other comptuers.

## Usage

1. Use Apple Remote Desktop to send
     mcxquerty -computerOnly
2. Export the results as a text file
3. Call the compare_mcx_printing.py file with the text file as the first argument
     python compare_mcx_printing.py a_list_of_mcx_settings.txt