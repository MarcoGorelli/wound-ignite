# How to submit

# before Saturday
0. delete all files in cache/*: `rm cache/*.csv`
0b. run `python generate_dre.py`
1. run `python get_tickers.py` to get the latest tickers, and put them in `covarianceforecasting.py`
2. run example_submission: `python examples_m6/example_m6_entry.py`
3. upload those files to Kaggle (precise-cache): `kaggle datasets version -p cache -m '2ndround'`
4. before the saturday when the period ends, run: `python submit_10_notebooks.py`, 3 times (modifying the ports index: `PORTS[0]`, then `PORTS[1]`, then `PORTS[2]`)
   check status with:  `for i in $(seq 0 22); do kaggle kernels status marcogorelli/f-999-port-1-$i; done;`

# on Saturday
1. repeat steps 0-3 from above!
5. update yfinance cache: `kaggle kernels push -p yfinance-data`
6. check cv-results: `kaggle kernels push -p cv-results` (update the kernel_metadata sources if notebook inputs have changed)
   make sure to remove the TODO line if it's there!
6a. run `kaggle kernels push -p check-naive-cv`
6b. to get the best candidates, run the notebook `kaggle kernels push -p find-best-from-cv`
	NOTE: you may want to tighten or loosen the conditions to find final_candidates
8. run the combine notebook: `kaggle kernels push -p combine`
9. run the submit notebook: `kaggle kernels push -p submit`
10. final check: `kaggle kernels push -p final-check`
11. submit the output of the submit notebook

