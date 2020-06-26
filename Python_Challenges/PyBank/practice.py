# Open the budget data csv file for reading
with open(input_path, newline='') as csvfile:
    csvread = csv.reader(csvfile, delimiter=',')
​
    # Process the records in the data file
    for record in csvread:
​
        # If the current record is the header, no data can be read and
        # month_count is the only variable that can be initialized
        if record[0] == "Date":
            month_count = 0
​
        # Otherwise the current record has meaningful data to process
        else:
​
            # Since month_count and current amount are updated every month,
            # they don't need to be incremented/read insided any conditional
            # logic that depends on which month it is
            month_count += 1
            current_amt = int(record[1])
​
            # At least two months of data are needed to calculate monthly
            # changes, so only first_amt and total_amt can be initialized
            if month_count == 1:
                first_amt = total_amt = current_amt
​
                # Set the current amount to be next month's previous amount
                # so that monthly differentials can be calculated
                previous_amt = current_amt
​
            # Monthly chages can be calculated after the first month, so
            # initialize the remaining variables and update the rest
            else:
​
                total_amt += current_amt
                amt_diff = current_amt - previous_amt
​
                # Initialize the remaining variables the second month ...
                if month_count == 2:
​
                    max_incr_date = max_decr_date = record[0]
                    max_incr = max_decr = amt_diff
​
                # ... and after the second month, check to see if
                # the max profit/loss stats need to be updated
                else: