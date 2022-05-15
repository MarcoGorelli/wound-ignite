# How to submit

1. delete all files in cache/*: `rm cache/*.csv`
2. run example_submission: `python examples_m6/example_m6_entry.py`
3. upload those files to Kaggle (precise-cache): `kaggle datasets version -p cache -m '2ndround'`
4. before the saturday when the period ends, run: `python submit_10_notebooks.py`, 3 times (modifying the ports index: `PORTS[0]`, then `PORTS[1]`, then `PORTS[2]`)
   check status with:  `for i in $(seq 0 22); do kaggle kernels status marcogorelli/f-999-port-$i; done;`
5. update yfinance cache: `kaggle kernels push -p yfinance-data`
6. check cv-results: `kaggle kernels push -p cv-results` (update the kernel_metadata sources if notebook inputs have changed)
7. put 8 best from each category into the combine notebook
8. run the combine notebook: `kaggle kernels push -p combine`
9. run the submit notebook: `kaggle kernels push -p submit`
10. final check: `kaggle kernels push -p final-check`
11. submit the output of that notebook

Today: just gonna go with last years' ones
Start with ports 0-20, if there's time, repeat steps 6 - 11 once the last notebook has finished.
