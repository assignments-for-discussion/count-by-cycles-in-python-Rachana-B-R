def count_batteries_by_usage(cycles):
  lowcount=0
  mediumcount=0
  highcount=0
  for i in cycles:
    if(i<150):
      lowcount+=1
    elif(i>=150 and i<650):
      mediumcount+=1
    elif(i>649):
      highcount+=1
  return {"lowCount":lowcount,"mediumCount":mediumcount,"highCount":highcount}


