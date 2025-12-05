print(sum([x*x for x in range(1, 10)]))

jobtext = 'anacron'
all_lines = (line for line in open('/var/log/cron', 'r'))
job = (line for line in all_lines if line.find(jobtext) != -1)
text = next(job)
text