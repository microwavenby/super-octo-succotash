# Robustification

## Option 1: Retries

There are some pretty straightforward libraries that allow retrying with backoffs with only a decorator; refactoring
the method that posts the data to the given URL and decorating it with [Retrying](https://pypi.org/project/retrying/)
could be as simple as that... 

This assumes that the remote system is idempotent and can update existing rows or will not error if a measure_id value already
exists.

## Option 2: Retry state files

It'd also be pretty straightforward to serialize the parsed data to JSON as a list of POST bodies that 
need to be re-posted. Perhaps a pattern like "./partial-data/$DATAFILENAME.partial-DATE.json" or something akin to that 
could allow re-POSTING partial data later after downtime.

This is a non-destructive option; of course, if modifying the TXT files in place is somehow acceptable, we could drop the successful lines from the TXT file as we receive successes back from the remote server. This is pretty sketchy though.

## Option 3: Combine JSON bodies with an external job service

If you had an asynchronous job queue, you could queue the failed requests up for later attempts by the wall-clock; "Send $JSON in 3 hours to URL" or the like

## Caveats to the above

One, I'm assuming that the schemas do not frequently change as a part of the above as I am discussing only using in-flight parsed TXT into JSON in these solutions. If the schema can change and needs to reflect changes, then other solutions would more likely be suitable -- such as writing the raw TXT data back out in a way that could be replayed from the latest iteration of the CSV schema.

Two, I'm assuming that the URL doesn't change and/or we do not need to follow redirects.

